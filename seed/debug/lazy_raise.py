__all__ = 'lazy_raise'.split()
def lazy_raise(Error, *args, **kwargs):
    def lazy_raise():
        raise Error(*args, **kwargs)


from seed.debug.lazy_raise import lazy_raise
