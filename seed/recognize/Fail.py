#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/Fail.py

seed.recognize.Fail
py -m nn_ns.app.debug_cmd   seed.recognize.Fail -x
py -m nn_ns.app.doctest_cmd seed.recognize.Fail:__doc__ -ht
py_adhoc_call   seed.recognize.Fail   @f
#]]]'''
__all__ = r'''
Fail
    ParseFail
    TokenizeFail
        BadFormat

BadFormat
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


######################
class Fail(Exception):pass
class ParseFail(Fail):pass
class TokenizeFail(Fail):pass
class BadFormat(TokenizeFail):pass

__all__
from seed.recognize.Fail import Fail, ParseFail, TokenizeFail, BadFormat
from seed.recognize.Fail import *
