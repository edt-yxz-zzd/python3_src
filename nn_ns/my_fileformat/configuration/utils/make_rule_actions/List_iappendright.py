class List_iappendright:
    # immutable
    def __init__(self, *, __ls = ()):
        # no parameter "iterable"
        self.__ls = __ls
    def iappendright(self, __last):
        return __class__(_List_iappendright__ls = (self.__ls, __last))
    def __iter__(self):
        ls = list(reversed(self))
        return reversed(ls)
    def __reversed__(self):
        init = self.__ls
        while init:
            init, last = init
            yield last

