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


