r'''
py -m nn_ns.app.debug_cmd   seed.tiny_.str__split_join

seed.tiny_.str__split_join
from seed.tiny_.str__split_join import str_join__list_nonemty, str_split__list_nonemty, str_join__entry_nonemty, str_split__entry_nonemty, str_join__both_list_and_entry_may_be_emty, str_split__both_list_and_entry_may_be_emty



#'''

__all__ = '''
    str_join__list_nonemty
    str_split__list_nonemty

    str_join__entry_nonemty
    str_split__entry_nonemty

    str_join__both_list_and_entry_may_be_emty
    str_split__both_list_and_entry_may_be_emty
    '''.split()

from seed.debug.expectError import expectError
from itertools import chain

assert ','.join([]) == '' == ','.join([''])
    # 碰撞，歧义！
assert ''.split(',') == ['']
assert expectError(ValueError, lambda:''.split(''))
    # ''.split('')
    #   ==>> ValueError: empty separator

def str_join__list_nonemty(sep, iterable, /):
    if not sep: raise TypeError
    ls = [*iterable] if type(iterable) is not list else iterable
    if not ls: raise TypeError
    s = sep.join(ls)
    if not ls == str_split__list_nonemty(sep, s): raise logic-err
    return s
def str_split__list_nonemty(sep, s, /):
    if not sep: raise TypeError
    ls = s.split(sep)
    if not ls: raise logic-err
    return ls
assert str_split__list_nonemty(',', '') == ['']
assert str_split__list_nonemty(',', '1') == ['1']
assert str_split__list_nonemty(',', ',') == ['', '']
assert str_split__list_nonemty(',', ',1') == ['', '1']
assert str_split__list_nonemty(',', '1,') == ['1', '']
assert str_split__list_nonemty(',', '1,1') == ['1', '1']

assert expectError(TypeError, lambda:str_join__list_nonemty(',', []))
assert str_join__list_nonemty(',', ['']) == ''
assert str_join__list_nonemty(',', ['1']) == '1'
assert str_join__list_nonemty(',', ['', '']) == ','
assert str_join__list_nonemty(',', ['', '1']) == ',1'
assert str_join__list_nonemty(',', ['1', '']) == '1,'
assert str_join__list_nonemty(',', ['1', '1']) == '1,1'


def str_join__entry_nonemty(sep, iterable, /):
    if not sep: raise TypeError
    ls = [*iterable] if type(iterable) is not list else iterable
    if not all(ls): raise TypeError
    s = sep.join(ls)
    if not ls == str_split__entry_nonemty(sep, s): raise logic-err
    return s
def str_split__entry_nonemty(sep, s, /):
    if not sep: raise TypeError
    ls = s.split(sep) if s else []
    if not all(ls): raise TypeError
    return ls
assert str_split__entry_nonemty(',', '') == []
assert str_split__entry_nonemty(',', '1') == ['1']
assert expectError(TypeError, lambda:str_split__entry_nonemty(',', ','))
assert expectError(TypeError, lambda:str_split__entry_nonemty(',', ',1'))
assert expectError(TypeError, lambda:str_split__entry_nonemty(',', '1,'))
assert str_split__entry_nonemty(',', '1,1') == ['1', '1']

assert str_join__entry_nonemty(',', []) == ''
assert expectError(TypeError, lambda:str_join__entry_nonemty(',', ['']))
assert str_join__entry_nonemty(',', ['1']) == '1'
assert expectError(TypeError, lambda:str_join__entry_nonemty(',', ['', '']))
assert expectError(TypeError, lambda:str_join__entry_nonemty(',', ['', '1']))
assert expectError(TypeError, lambda:str_join__entry_nonemty(',', ['1', '']))
assert str_join__entry_nonemty(',', ['1', '1']) == '1,1'



def str_join__both_list_and_entry_may_be_emty(sep, iterable, /):
    if not sep: raise TypeError
    ls = [*iterable] if type(iterable) is not list else iterable
    if 0:
        def f(sep, it, /):
            for x in it:
                yield sep
                yield x
        s = ''.join(f(sep, ls))
    else:
        s = sep.join(chain([''], ls))
    if not ls == str_split__both_list_and_entry_may_be_emty(sep, s): raise logic-err
    return s
def str_split__both_list_and_entry_may_be_emty(sep, s, /):
    if not sep: raise TypeError
    ls = s.split(sep)
    if not ls: raise logic-err
    if ls[0]: raise TypeError#==>> (s and not s.startswith(sep))
    del ls[0]
    return ls

assert str_split__both_list_and_entry_may_be_emty(',', '') == []
assert expectError(TypeError, lambda:str_split__both_list_and_entry_may_be_emty(',', '1'))
assert str_split__both_list_and_entry_may_be_emty(',', ',') == ['']
assert str_split__both_list_and_entry_may_be_emty(',', ',1') == ['1']
assert expectError(TypeError, lambda:str_split__both_list_and_entry_may_be_emty(',', '1,'))
assert expectError(TypeError, lambda:str_split__both_list_and_entry_may_be_emty(',', '1,1'))

assert str_join__both_list_and_entry_may_be_emty(',', []) == ''
assert str_join__both_list_and_entry_may_be_emty(',', ['']) == ','
assert str_join__both_list_and_entry_may_be_emty(',', ['1']) == ',1'
assert str_join__both_list_and_entry_may_be_emty(',', ['', '']) == ',,'
assert str_join__both_list_and_entry_may_be_emty(',', ['', '1']) == ',,1'
assert str_join__both_list_and_entry_may_be_emty(',', ['1', '']) == ',1,'
assert str_join__both_list_and_entry_may_be_emty(',', ['1', '1']) == ',1,1'


