import logging
from contextlib import contextmanager

"""
Temporarily changing the log level using contextmanager
"""

logging.getLogger().setLevel(logging.WARNING)


@contextmanager
def debug_logging(level):
    """
    Helper function to achieve the above objective.
    This is a definition of a contextmanager
    """
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def swallow_exception(cls):
    try:
        yield
    except cls:
        logging.exception('Swallowing exception')


@contextmanager
def debug_logging_2(level, name):
    """
    This version of context manager allows for a handle to a logger
    which is then used to log messages at the specified level
    """
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


def my_function():
    """
    Sample function which needs to be logged at a different level
    """
    logging.debug('Some debug info')
    logging.error('A real error!')
    logging.debug('More debugging')


def test_debug_logging():
    print("*** With contextmanager ***")
    with debug_logging(logging.DEBUG):
        my_function()

    # without contextmanager
    print("*** Without contextmanager ***")
    my_function()


def test_debug_logging_2():
    print("*** With contextmanager ***")
    with debug_logging_2(logging.DEBUG, 'my_log') as logger:
        # NOTE: will not show as the global level is WARNING
        logging.debug('This is the global logger')
        logger.debug('This is the my_log logger')

    print("*** Without contextmanager ***")
    logger = logging.getLogger('my_log')
    logger.debug('Does not print anything')     # global level = WARNING
    logger.error('This will print')


def test_swallow_exception():
    value = 2
    with swallow_exception(ZeroDivisionError):
        value /= 0


if __name__ == '__main__':
    # test_debug_logging()
    # test_swallow_exception()
    test_debug_logging_2()
    print("Program still running even after zerodivision error")
