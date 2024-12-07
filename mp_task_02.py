import threading
import time
import multiprocessing
import asyncio
import math


# Функции для АТ-05

# запускать с n = 699993
def fibonacci(n):
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    start_time = time.time()

    fibonacci(699993)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)

    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    start_time = time.time()

    result_fibonacci = []
    result_trapezoidal = []

    thread_fib = threading.Thread(target=fibonacci, args=(699993,))
    result_fibonacci.append(thread_fib)

    thread_trap = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    result_trapezoidal.append(thread_trap)

    thread_fib.start()
    thread_trap.start()

    thread_fib.join()
    thread_trap.join()

    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    start_time = time.time()

    with multiprocessing.Pool(processes=2) as pool:
        results = [
            pool.apply_async(fibonacci, (699993,)),
            pool.apply_async(trapezoidal_rule, (math.sin, 0, math.pi, 20000000)),
        ]

        fib_result = results[0].get()
        trap_result = results[1].get()

    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def asyncio_run():
    start_time = time.time()

    fib_task = asyncio.to_thread(fibonacci, 699993)
    trap_task = asyncio.to_thread(trapezoidal_rule, math.sin, 0, math.pi, 20000000)

    fib_result, trap_result = await asyncio.gather(fib_task, trap_task)

    end_time = time.time()
    print(f'asyncio time: {end_time - start_time: 0.2f} \n')

if __name__ == '__main__':
    sequence()
    threads()
    processes()
    asyncio.run(asyncio_run())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):

        fibonacci = 8
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???

        fibonacci = 8
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 

        fibonacci = 8
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """
