import time
from PIL import Image
import numpy as np
import threading
import os
from multiprocessing import Pool

def invert_color(pixel): #функция инвертирования пикселей



def process_image_sequential(image_path, output_path, filter_func):
    """
    image_path - путь до исходного изображения
    output_path - путь, куда сохранить обработанное фото
    filter_func - функция обработчик
    """

def process_image_threading(image_path, output_path, filter_func, num_threads):
    """
        image_path - путь до исходного изображения
        output_path - путь, куда сохранить обработанное фото
        filter_func - функция обработчик
        num_threads - количество используемых потоков
    """

    def process_part(start_row, end_row):
        """
        start_row - индекс строки, с которой начинается обработка в этом потоке
        end_row - индекс строки, где заканчивается обработка
        """

def process_part_multiprocessing(args): # обработки части изображения в отдельном процессе
    """
    start_row, end_row, pixels, filter_func = args
    start_row - индекс строки, с которой начинается обработка в этом процессе
    end_row - индекс строки, где заканчивается обработка
    pixels - пиксель для обработки
    filter_func - функция обработчик
    """

def process_image_multiprocessing(image_path, output_path, filter_func, num_processes):
    """
        image_path - путь до исходного изображения
        output_path - путь, куда сохранить обработанное фото
        filter_func - функция обработчик
        num_processes - количество используемых процессов
    """

def process_image(image_paths): # запуск всех процессов обработки
    """
    image_paths - список с путями к начальным изображениям
    """