from functools import wraps
from timeit import default_timer
from loguru import logger


def timing_dec(func):
    """Синхронный декоратор замера времени"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        func_result = func(*args, **kwargs)
        end_time = default_timer()
        logger.info('Function execution time with args is {:.10f} second.',  end_time - start_time)
        return func_result

    return wrapper
