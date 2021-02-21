


r"""
usage:
        from seed.for_libs.for_logging import disable_logging
        with disable_logging():
            import png
            ...
        with enable_logging():
            ...
        with disable_logger(''):
            ...
    <==>
        logging.disable()
        import png
        logging.disable(logging.NOTSET)


=====
py -m seed.for_libs.for_logging
>>> _test()
ERROR:root:show @free +
ERROR:root:show @enable_logging +
ERROR:root:show @enable_logging +-
ERROR:root:show @enable_logging -
ERROR:root:show @free -

=====
class Logger(Filterer):
class logging.Logger:
    setLevel(level)
    isEnabledFor(level)
    getEffectiveLevel()




logging.getLogger(name=None)
logging.disable(level=CRITICAL)


level=Numeric value
    CRITICAL=50
    ERROR=40
    WARNING=30
    INFO=20
    DEBUG=10
    NOTSET=0
#"""




__all__ = r"""
    disable_logging
    enable_logging
    disable_logger
    """.split()





import logging

assert logging.getLogger() is logging.getLogger('')
assert logging.getLogger() is not logging.getLogger('root')


from contextlib import contextmanager

@contextmanager
def disable_logger(name):
    logger = logging.getLogger(name)
    saved = logger.disabled
    logger.disabled = True
    try:
        yield None
    finally:
        logger.disabled = saved

def enable_logging(*, name=None):
    return disable_logging(name=name, level=logging.NOTSET)

def disable_logging(*, name=None, level=logging.CRITICAL):
    r'''
    since:
        logging.getLogger(name=None)
        logging.disable(level=CRITICAL)
    #'''
    if name is not None:
        raise NotImplementedError
        logger = logging.getLogger(name)
        logger.manager.disable = level
        logger.disabled = True
    else:
        return _disable_logging(level=level)
@contextmanager
def _disable_logging(*, level):
    logger = logging.getLogger()
    saved_level = logger.manager.disable
    logging.disable(level)
    assert logger.manager.disable is level

    try:
        yield None
    finally:
        logging.disable(saved_level)
        assert logger.manager.disable is saved_level

with disable_logging(level=object()):
    with enable_logging():
        pass
    pass


def _test():
    import sys
    _stderr = sys.stderr
    sys.stderr = sys.stdout
    try:
        logging.error('show @free +')
        with disable_logging():
            logging.error('not show @disable_logging +')
            with enable_logging():
                logging.error('show @enable_logging +')
                with disable_logger(''):
                    logging.error('not show @disable_logger +-')
                logging.error('show @enable_logging +-')
                with disable_logging():
                    logging.error('not show @disable_logging +-')
                logging.error('show @enable_logging -')
            logging.error('not show @disable_logging -')
        logging.error('show @free -')
    finally:
        sys.stderr = _stderr

if __name__ == "__main__":
    import doctest
    doctest.testmod()









