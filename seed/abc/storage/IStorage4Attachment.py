#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
IStorage4Attachment vs IStorage4Cache
    eg: cached result
    eg: cached whether checked/check__deep
        * external check input:
            #IStorage4Attachment@input
            def noncached_check_input(sf, input, /):
            def cached_check_input(sf, input, /):
                checked = get-IStorage4Attachment(input, type(sf).noncached_check_input, False)
                if not checked:
                    sf.noncached_check_input(input)
                    setdefault-IStorage4Attachment(input, type(sf).noncached_check_input, True)

        * internal check immutable value obj at readonly attribute yield from overrided API/abstractmethod:
            #IStorage4Cache@sf
            def noncached_check_xxx(sf, xxx, /):
            def ___get_xxx___(sf, /):
            def get_xxx(sf, /):
                xxx = type(sf).___get_xxx___(sf)
                checked = get-IStorage4Cache(sf, type(sf).noncached_check_xxx, False)
                if not checked:
                    sf.noncached_check_xxx(xxx)
                    setdefault-IStorage4Cache(sf, type(sf).noncached_check_xxx, True)



seed.abc.storage.IStorage4Attachment
py -m    seed.abc.storage.IStorage4Attachment
py -m nn_ns.app.debug_cmd   seed.abc.storage.IStorage4Attachment

from seed.abc.storage.IStorage4Attachment import ...

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
r"""
import ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    #(''')
from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.helper.repr_input import repr_helper
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.helper.check.checkers import check_pair, check_type_is
  #from seed.helper.check.checkers import checks, checkers, check_funcs
  #view ../../python3_src/seed/helper/check/checkers.py
if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
#"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


