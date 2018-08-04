
import timeit
from sand import is_main


def main():
    try:
        timeit.timeit(tuple, number=10)
    except:
        print('timeit callable', False)
        raise
    else:
        print('timeit callable', True)

    return


if is_main(__name__):
    main()
    pass
