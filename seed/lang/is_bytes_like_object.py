
__all__ = '''
    is_bytes_like_object
    check_bytes_like_object
    '''.split()

def check_bytes_like_object(obj):
    # -> None or raise TypeError
    memoryview(obj) # may raise TypeError
def is_bytes_like_object(obj):
    try:
        memoryview(obj)
    except TypeError:
        return False
    return True

