
r'''
=====
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of the file if it exists
=====
'b' binary mode
't' text mode (default)
=====
'+' open a disk file for updating (reading and writing)
=====


'r'
    [exists]read
'x'
    [not_exists]create_write
    # not readable!!!!!!
'w'
    ([exists]truncate+[not_exists]create) write
    # not readable!!!!!!
'a'
    ([exists]append+[not_exists]create) write
    # not readable!!!!!!
'[rxwa]+'
    [?]read_write
    at most one of 'rwx'
==>>
'r+'
    [exists]read_write
'x+'
    [not_exists]create_read_write
    x+ <!> r+
'w+'
    ([exists]truncate+[not_exists]create) read_write
    w+ <!> r+ # truncate or not
    w+ > x+
'a+'
    ([exists]append+[not_exists]create) read_write
    a+ <!> r+ # append or not
    a+ > x+
    a+ <!> w+
'rx' - error
    [not_exists]create + [exists]read

===============================

>>> mk = make_open_mode__easy
>>> mk(allow_exist=True, allow_read=True)
'rt'
>>> mk(allow_create=True, allow_write=True)
'xt'
>>> mk(allow_create=True, allow_exist=True, allow_write=True, truncate_at_start=True)
'wt'
>>> mk(allow_create=True, allow_exist=True, allow_write=True, append_at_start=True)
'at'
>>> mk(allow_exist=True, allow_read=True, allow_write=True)
'r+t'
>>> mk(allow_create=True, allow_write=True, allow_read=True)
'x+t'
>>> mk(allow_create=True, allow_exist=True, allow_write=True, truncate_at_start=True, allow_read=True)
'w+t'
>>> mk(allow_create=True, allow_exist=True, allow_write=True, append_at_start=True, allow_read=True)
'a+t'

#############make_kwargs_from_open_mode
>>> mk_md = make_kwargs_from_open_mode
>>> mk_kw = make_open_mode_kwargs__easy
>>> mk_md('t+a') == mk_kw(allow_create=True, allow_exist=True, allow_write=True, append_at_start=True, allow_read=True)
True
>>> mk_md('R') == mk_kw(allow_exist=True, allow_read=True)
True


'''





__all__ = '''
    make_kwargs_from_open_mode
    make_open_mode__easy

    make_open_mode
    make_open_mode_from_kwargs
    make_open_mode_kwargs__easy
    '''.split()

import re
_rxwa_rex = re.compile(r'[rxwaRXWA]')
_bt_rex = re.compile(r'[bBtT]')

def make_kwargs_from_open_mode(mode):
    total_plus = mode.count('+')
    rxwa_ls = _rxwa_rex.findall(mode)
    bt_ls = _bt_rex.findall(mode)
    if not total_plus <= 1: raise ValueError
    if not len(bt_ls) <= 1: raise ValueError
    if not len(rxwa_ls) == 1: raise ValueError
    ls = []

    [rxwa] = rxwa_ls
    ls.append(rxwa.lower())
    if total_plus:
        ls.append('+')
    mode = ''.join(ls)
    kwargs = dict(_mode2kwargs[mode])


    if bt_ls:
        [bt] = bt_ls
        bt = bt.lower()
    else:
        bt = 't'
    assert bt in ('t', 'b')
    kwargs['is_binary'] = (bt == 'b')
    return kwargs


F = False
T = True
_kwargs_tpl =\
    {'allow_create':F, 'allow_exist':F, 'allow_read':F, 'allow_write':F
    , 'append_at_start':F, 'truncate_at_start':F
    }
_mode2kwargs = {
'r':
    #[exists]read
    {'allow_create':F, 'allow_exist':T, 'allow_read':T, 'allow_write':F
    , 'append_at_start':F, 'truncate_at_start':F
    }
,'x':
    #[not_exists]create_write
    # not readable!!!!!!
    {'allow_create':T, 'allow_exist':F, 'allow_read':F, 'allow_write':T
    , 'append_at_start':F, 'truncate_at_start':F
    }
,'w':
    #([exists]truncate+[not_exists]create) write
    # not readable!!!!!!
    {'allow_create':T, 'allow_exist':T, 'allow_read':F, 'allow_write':T
    , 'append_at_start':F, 'truncate_at_start':T
    }
,'a':
    #([exists]append+[not_exists]create) write
    # not readable!!!!!!
    {'allow_create':T, 'allow_exist':T, 'allow_read':F, 'allow_write':T
    , 'append_at_start':T, 'truncate_at_start':F
    }
,'r+':
    #[exists]read_write
    {'allow_create':F, 'allow_exist':T, 'allow_read':T, 'allow_write':T
    , 'append_at_start':F, 'truncate_at_start':F
    }
,'x+':
    #[not_exists]create_read_write
    {'allow_create':T, 'allow_exist':F, 'allow_read':T, 'allow_write':T
    , 'append_at_start':F, 'truncate_at_start':F
    }
,'w+':
    #([exists]truncate+[not_exists]create) read_write
    {'allow_create':T, 'allow_exist':T, 'allow_read':T, 'allow_write':T
    , 'append_at_start':F, 'truncate_at_start':T
    }
,'a+':
    #([exists]append+[not_exists]create) read_write
    {'allow_create':T, 'allow_exist':T, 'allow_read':T, 'allow_write':T
    , 'append_at_start':T, 'truncate_at_start':F
    }
}; del F, T
assert len(_mode2kwargs) == len('rxwa')*2

class Global:
    key_set = set(_kwargs_tpl)
    sorted_keys = sorted(key_set)
    @classmethod
    def make_kwargs_name(cls, kwargs):
        sorted_keys = cls.sorted_keys
        key_set = cls.key_set
        if not set(kwargs) == key_set: raise ValueError
        kwargs_name = ''.join(
            ('T' if kwargs[k] else 'F') for k in sorted_keys)
        assert len(kwargs_name) == len(key_set)
        return kwargs_name
    kwargs_name2mode = ...

def _mk(cls):
    kwargs_name2mode = {}
    for mode, kwargs in _mode2kwargs.items():
        assert set(kwargs) == cls.key_set
        kwargs_name = cls.make_kwargs_name(kwargs)
        kwargs_name2mode[kwargs_name] = mode
    if len(kwargs_name2mode) != len(_mode2kwargs):
        raise logic-error
    return kwargs_name2mode
Global.kwargs_name2mode = _mk(Global); del _mk




def make_open_mode_kwargs__easy(*
    , allow_create=False, allow_exist=False
    , allow_read=False, allow_write=False
    , append_at_start=False, truncate_at_start=False
    , is_binary=False
    ):
    return {**locals()}
    kwargs = dict(
        allow_create=allow_create
        ,allow_exist=allow_exist
        ,allow_read=allow_read
        ,allow_write=allow_write
        ,append_at_start=append_at_start
        ,truncate_at_start=truncate_at_start
        ,is_binary=is_binary
        )
    return kwargs

def make_open_mode__easy(*
    , allow_create=False, allow_exist=False
    , allow_read=False, allow_write=False
    , append_at_start=False, truncate_at_start=False
    , is_binary=False
    ):
    kwargs = {**locals()}
    return make_open_mode_from_kwargs(kwargs)

def make_open_mode(*
    , allow_create, allow_exist, allow_read, allow_write
    , append_at_start, truncate_at_start
    , is_binary
    ):
    kwargs = {**locals()}
    return make_open_mode_from_kwargs(kwargs)
    kwargs = dict(
        allow_create=allow_create
        ,allow_exist=allow_exist
        ,allow_read=allow_read
        ,allow_write=allow_write
        ,append_at_start=append_at_start
        ,truncate_at_start=truncate_at_start
        )
    return make_open_mode_from_kwargs(kwargs)
def make_open_mode_from_kwargs(kwargs):
    return _make_open_mode_from_kwargs(**kwargs)
def _make_open_mode_from_kwargs(*, is_binary, **kwargs):
    mode1 = 'b' if is_binary else 't'
    kwargs_name = Global.make_kwargs_name(kwargs)
    mode2 = Global.kwargs_name2mode[kwargs_name]
    mode = f'{mode2}{mode1}'
    return mode




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

if False and __name__ == '__main__':
    classes = [Global
        ]
    excludes = '''
        logic
        error
        '''.split()

    from seed.helper.ongo import main
    main(modules=[__name__], classes=classes, excludes=excludes)

