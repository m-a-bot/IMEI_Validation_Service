from loguru import logger


def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_log_message = f"Started --> function '{func.__name__}'"
        end_log_message = f"Completed --> function '{func.__name__}'"
        logger.info(start_log_message)
        result = func(*args, **kwargs)
        logger.info(end_log_message)
        return result

    return wrapper
