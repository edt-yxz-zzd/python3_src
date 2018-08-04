
#def exceptError(Error, f):
def expectError(Error, f):
    # expectError(Error, f, *args, **kwargs)??
    #   no, to slow
    #   f = lambda: ... is faster
    if Error is None:
        Error = Exception
    try:
        f()
    except Error:
        return True
    except:
        pass
    return False


