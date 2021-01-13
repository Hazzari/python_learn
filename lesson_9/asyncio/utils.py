from functools import wraps
from timeit import default_timer

from loguru import logger


def timing_dec(func):
    """Асинхронный декоратор замера времени"""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = default_timer()
        func_result = await func(*args, **kwargs)
        end_time = default_timer()
        logger.info('Время выполнения функции с аргументами: {} заняло {:.4f} сек.', args, end_time - start_time)
        return func_result

    return wrapper
