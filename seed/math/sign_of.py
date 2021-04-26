
def sign_of(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    elif x > 0:
        return +1
    else:
        raise Exception(f'sign_of({x!r})')

