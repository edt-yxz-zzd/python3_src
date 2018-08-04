
def assert_except(ERROR, f, *args, **kwargs):
    try:
        f(*args, **kwargs)
    except ERROR:
        return
    else:
        raise logic-error

