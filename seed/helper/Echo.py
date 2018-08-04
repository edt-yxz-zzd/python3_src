

'''
theEcho
    - may be use as a module:
        sys.modules['virtual.theEcho'] = theEcho
        from virtual.theEcho import x,y,z, n,m
echo
    - may be use as a key function:
        sorted(iterable, key=echo)


example:
    >>> theEcho.xxxyyy
    'xxxyyy'
    >>> theEcho.__class__
    '__class__'
    >>> theEcho.__dict__
    '__dict__'

    >>> Nothing = []
    >>> echo(Nothing) is Nothing
    True


'''

__all__ = '''
    theEcho
    echo
    '''.split()


echo = lambda x:x
class Echo:
    'theEcho.xxx == "xxx"'
    def __getattribute__(self, name):
        return name

theEcho = Echo()

assert theEcho.__class__ == '__class__'
assert echo(3) == 3

if __name__ == "__main__":
    import doctest
    doctest.testmod()

