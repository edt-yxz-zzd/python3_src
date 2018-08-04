
'''
usage:
    filter(not_dot(pred), ...)
    dot[not_dot(pred), ...](...)
    dot[__not__, pred, ...](...)
'''
__all__ = 'not_dot __not__'.split()
from operator import __not__
def not_dot(f):
    'not_dot(f) ::= not . f'
    return lambda x: not f(x)



