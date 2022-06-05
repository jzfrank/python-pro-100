import time


def speed_calc_decorator(fcn):
    def wrapper():
        start = time.time()
        fcn()
        end = time.time()
        print(f"Time used for {fcn.__name__} is {end - start} secs")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
