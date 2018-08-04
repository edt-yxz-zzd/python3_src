
class SandExcept(Exception):pass
class InternetExcept(SandExcept):pass

class UnknownCaseError(SandExcept):pass
class CheckError(SandExcept):pass
class CheckAssertionError(AssertionError, CheckError):pass
class CheckTypeError(TypeError, CheckError):pass
class CheckValueError(ValueError, CheckError):pass
class FormatError(ValueError, SandExcept):pass

sand_except = SandExcept
unknown_case_except = UnknownCaseExcept = UnknownCaseError
internet_except = InternetExcept

class LogicError(SandExcept):pass
#class NotMatchedError(SandExcept, ValueError):pass
class CodecError(SandExcept):pass
class DecodeError(SandExcept):pass
class EncodeError(SandExcept):pass


class CompileError(SandExcept):pass
class ParseError(CompileError):pass
class TokenizeError(ParseError):pass

