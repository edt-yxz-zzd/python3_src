


from .error import FailAtPos
class TokenizeFail(FailAtPos):pass


class Token:
    def __init__(self, case, begin, end, value):
        assert begin <= end
        self.type = case
        self.begin = begin
        self.end = end
        self.value = value # may be a merged string, skip some characters
        return

    def size(self):
        return self.end - self.begin

    def sub(self, string):
        return string[self.begin : self.end]

    def __repr__(self):
        #raise
        return 'Token({case!r}, {begin!r}, {end!r}, {value!r})'\
               .format(case = self.type, begin = self.begin, \
                       end = self.end, value = self.value)

