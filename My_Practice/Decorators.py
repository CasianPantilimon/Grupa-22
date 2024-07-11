from time import time


def performance(func):
    def wrap_function(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"This function took {t2 - t1} seconds to run.")
        return result

    return wrap_function


@performance
def long_time():
    for i in range(100000):
        i * 5



