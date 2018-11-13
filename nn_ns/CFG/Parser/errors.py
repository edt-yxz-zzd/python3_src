
__all__ = '''
    ParseFailError
        NotExistsError
        NotTreeError
            NotTreeError__recur
            NotTreeError__ambiguous
    '''.split()

from ..errors import ParseFailError


class NotExistsError(ParseFailError):pass
class NotTreeError(ParseFailError):pass
class NotTreeError__recur(NotTreeError):pass
class NotTreeError__ambiguous(NotTreeError):pass

