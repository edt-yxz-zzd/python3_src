class List_iappendleft:
    # immutable
    def __init__(self, *, __ls = ()):
        # no parameter "iterable"
        self.__ls = __ls
    def iappendleft(self, __head):
        return __class__(_List_iappendleft__ls = (__head, self.__ls))
        return __class__(__ls = (__head, self.__ls))
    def __iter__(self):
        tail = self.__ls
        while tail:
            head, tail = tail
            yield head





