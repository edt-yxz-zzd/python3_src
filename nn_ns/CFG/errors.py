
__all__ = '''
    ParseBaseError
    ParseFailError
    '''.split()

class ParseBaseError(Exception):pass
class ParseFailError(ParseBaseError):pass

