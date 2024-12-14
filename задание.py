import time
from PIL import Image
import numpy as np
import threading
import os
from multiprocessing import Pool


def invert_color(pixel): #функция инвертирования пикселей
    return (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])


def process_image_sequential(image_path, output_path, filter_func):
    # открытие фото по пути, преобразование изображения в вид RGB
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image) # преображение изображения в многомерный массив

    # размеры массива
    rows = pixels.shape[0]
    cols = pixels.shape[1]

    for i in range(rows): # проходимся по строкам
        for j in range(cols): # проходимся по столбцам
            # применение функции инвертации к каждому пикселю
            pixels[i, j] = filter_func(tuple(pixels[i, j]))

    result_image = Image.fromarray(pixels) # объект с новыми пикселями
    result_image.save(output_path) # сохранение нового фото
    return result_image


def process_image_threading(image_path, output_path, filter_func, num_threads):
    # открытие фото по пути, преобразование изображения в вид RGB
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image) # преображение изображения в многомерный массив
    height = pixels.shape[0] # количесвто строк пикселей
    threads = [] # список для хранения потоков

    # start_row - индекс строки, с которой начинается обработка в этом потоке
    # end_row - индекс строки, где заканчивается обработка
    def process_part(start_row, end_row):
        for i in range(start_row, end_row): # по строкам
            for j in range(pixels.shape[1]): # по столбцам
                # применение функции инвертации к каждому пикселю
                pixels[i, j] = filter_func(tuple(pixels[i, j]))

    # вычисляет количество строк, которые будут обрабатываться каждым потоком
    rows_per_thread = height // num_threads

    # запускаем каждый поток
    for i in range(num_threads):
        start_row = i * rows_per_thread # начальная строка текущего потока
        end_row = (i + 1) * rows_per_thread if i < num_threads - 1 else height # конечная
        thread = threading.Thread(target=process_part, args=(start_row, end_row)) # создание потока
        threads.append(thread) # добавление потока в список потоков
        thread.start()

    for thread in threads: # ждем выполнение
        thread.join()

    result_image = Image.fromarray(pixels) # объект с новыми пикселями
    result_image.save(output_path) # сохранение нового фото
    return result_image


def process_part_multiprocessing(args): # обработкf части изображения в отдельном процессе
    start_row, end_row, pixels, filter_func = args

    # вырезает часть массива, которую надо обработать в текущем процессе. Копируем!
    # (это важно при использовании multiprocessing, так как каждый процесс работает в своем адресном пространстве.
    # изменения, сделанные в процессе, не должны затрагивать данные в родительском процессе, пока мы это явно не укажем)
    part = pixels[start_row:end_row].copy()

    for i in range(part.shape[0]): # по строкам
        for j in range(part.shape[1]): # по столбцам
            # применение функции инвертации к каждому пикселю
            part[i, j] = filter_func(tuple(part[i, j]))

    return start_row, part


def process_image_multiprocessing(image_path, output_path, filter_func, num_processes):
    # открытие фото по пути, преобразование изображения в вид RGB
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image) # преображение изображения в многомерный массив
    height = pixels.shape[0] # количесвто строк пикселей

    # вычисляет количество строк, которые будут обрабатываться каждым процессом
    rows_per_process = height // num_processes
    args = [] # в этом списке будут храниться кортежи с аргументами для каждого процесса
    for i in range(num_processes): # проходимся по всем процессам
        start_row = i * rows_per_process # вычисляет начальную строку для текущего процесса
        # вычисляет конечную строку для текущего процесса
        end_row = (i + 1) * rows_per_process if i < num_processes - 1 else height
        args.append((start_row, end_row, pixels, filter_func)) # добавляем в картеж аргументы

    with Pool(processes=num_processes) as pool: # создает пул процессов Pool с указанным количеством процессов
        results = pool.map(process_part_multiprocessing, args) # применение функции к каждой разделенной части

    for start_row, part in results: # собираем обработанные части в одно изображение
        pixels[start_row:start_row + part.shape[0]] = part

    result_image = Image.fromarray(pixels)
    result_image.save(output_path)
    return result_image


def measure_time(func, *args): # функция подсчета времени работы кода
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time, result


def process_image(image_paths): # запуск фукнций
    for image_path in image_paths: # проходимся по фотографиям
        image_name = os.path.basename(image_path)
        print(f"вид процесса: последовательный")
        time_seq, result = measure_time(process_image_sequential, image_path,
                                        f"{os.path.splitext(image_name)[0]}_sequential.jpg", invert_color)
        print(f"в процессе фото: {image_name}")
        print(f"время обработки: {time_seq:.2f} секунд")

        for num_threads in [2, 4]:
            print(f"вид процесса: многопоточный ({num_threads} потока)")
            time_thread, result = measure_time(process_image_threading, image_path,
                                               f"{os.path.splitext(image_name)[0]}_threading_{num_threads}.jpg",
                                               invert_color, num_threads)
            print(f"в процессе фото: {image_name}")
            print(f"время обработки: {time_thread:.2f} секунд")

        for num_processes in [2, 4]:
            print(f"вид процесса: многопроцессорный ({num_processes} процесса)")
            time_multi, result = measure_time(process_image_multiprocessing, image_path,
                                              f"{os.path.splitext(image_name)[0]}_multiprocessing_{num_processes}.jpg",
                                              invert_color, num_processes)
            print(f"в процессе фото: {image_name}")
            print(f"время обработки: {time_multi:.2f} секунд")


if __name__ == "__main__":
    image_paths = ["500.jpg", "1000.jpg", "2000.jpg"]

    process_image(image_paths)
    