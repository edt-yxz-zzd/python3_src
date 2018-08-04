
def lazy_raise(Error, *args, **kwargs):
    def lazy_raise():
        raise Error(*args, **kwargs)



