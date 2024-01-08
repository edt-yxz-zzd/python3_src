#__all__:goto
r'''[[[
e ../../python3_src/seed/io/continue_io.py
used in:
    view ../../python3_src/seed/math/primality_proving__plain.py


seed.io.continue_io
py -m nn_ns.app.debug_cmd   seed.io.continue_io -x
py -m nn_ns.app.doctest_cmd seed.io.continue_io:__doc__ -ff -v
py_adhoc_call   seed.io.continue_io   @f

#]]]'''
__all__ = r'''
    IncompleteLastLineError
    Setting4LineContinueIO
        setting4LineContinueIO__newline_utf8
    LineContinueIO
        IValidatableLineContinueIO

'''.split()#'''
__all__

from os import SEEK_SET, SEEK_END, SEEK_CUR
#from itertools import repeat

from seed.for_libs.for_io.stream_obj_converter import binary_stream_obj2text_stream_obj
#def binary_stream_obj2text_stream_obj(binary_stream_obj, /,*, encoding, buffered_case, kwargs4buffered_binary_stream, kwargs4text_stream):
    #buffered_cases = ('read', 'write', 'rw_seek')
from seed.tiny import check_type_is
from seed.tiny import check_type_le
from seed.helper.safe_eval import safe_eval
from seed.helper.repr_input import repr_helper

class IncompleteLastLineError(Exception):pass

class Setting4LineContinueIO:
    def __init__(sf, line_sep, /, *, encoding):
        check_type_is(str, line_sep)
        assert line_sep
        sf.line_sep = line_sep
        sf.encoding = encoding
        sf.bytes4line_sep = line_sep.encode(encoding)
    def __repr__(sf, /):
        return repr_helper(sf, sf.line_sep, encoding=sf.encoding)
setting4LineContinueIO__newline_utf8 = Setting4LineContinueIO('\n', encoding='utf8')
class LineContinueIO:
    __default_setting__ = setting4LineContinueIO__newline_utf8
    @classmethod
    def _open_(cls, path, /, *, allow_create):
        if allow_create:
            binary_iofile = open(path, 'a+b')
            binary_iofile.seek(0, SEEK_SET)
        else:
            binary_iofile = open(path, 'r+b')
        binary_iofile
        return binary_iofile
    @classmethod
    def from_path_(cls, may_setting, path, /, *, allow_create):
        #def from_path_(cls, may_setting, path, /, *, allow_create=True):
            #see:IValidatableLineContinueIO
            #   which default: allow_create=False
        binary_iofile = cls._open_(path, allow_create=allow_create)
        sf = line_continue_io = cls(may_setting, binary_iofile)
        return sf

    def __init__(sf, may_setting, binary_iofile, /):
        if may_setting is None:
            setting = type(sf).__default_setting__
        else:
            setting = may_setting
        setting
        ######################
        check_type_le(Setting4LineContinueIO, setting)
        sf.setting = setting
        sf.binary_iofile = binary_iofile
        ######################
        sf.text_iofile = binary_stream_obj2text_stream_obj(sf.binary_iofile, encoding=sf.setting.encoding, buffered_case='io', kwargs4buffered_binary_stream={}, kwargs4text_stream={})
    def __repr__(sf, /):
        return repr_helper(sf, sf.setting, sf.binary_iofile)

    def get_text_iofile_wrapper(sf, /):
        return sf.text_iofile
            # rename mk_--> get_ since auto close file by wrapper

    def read_bytes4last_line(sf, /):
        bfile = sf.binary_iofile
        bsep = sf.setting.bytes4line_sep
        bfile.seek(0, SEEK_END)
        sz = bfile.tell()
        L = len(bsep)
        bk = L<<8
        bss = [b'']
        addr = 0
        for addr in reversed(range(0, sz, bk)):
            bfile.seek(addr, SEEK_SET)
            bs = bfile.read(bk)
            bs_ = bs + bss[-1][:L-1]
            bss.append(bs)
            end = len(bs_)
            if addr+end == sz:
                end -= 1
            imay = bs_.rfind(bsep, 0, end)
            if not imay == -1:
                i = imay
                assert bs_[i:i+L] == bsep
                assert i+L <= len(bs)
                addr += i+L
                if addr < sz:
                    bss[-1] = bs[i+L:]
                    break
                else:
                    raise 000
        else:
            assert addr == 0
        addr
        bss.reverse()
        tail = b''.join(bss)
        bfile.seek(addr, SEEK_SET)

        bytes4last_line = bfile.read()
        assert len(bytes4last_line) == sz-addr
        assert bytes4last_line == tail
        assert sz == bfile.tell()
            #eof
        return bytes4last_line
    def read_last_line(sf, /):
        bytes4last_line = sf.read_bytes4last_line()
        last_line = bytes4last_line.decode(sf.setting.encoding)
        return last_line
    def read_last_line_then_tmay_safe_eval_(sf, /, *, strict_line_end=True):
        '-> tmay result | ^IncompleteLastLineError'
        sep = sf.setting.line_sep
        last_line = sf.read_last_line()
        if strict_line_end:
            if last_line and not last_line.endswith(sep): raise IncompleteLastLineError(last_line)
        if last_line:
            result = sf.safe_eval_(last_line)
            tmay_result = (result,)
        else:
            tmay_result = ()
        return tmay_result



    def safe_eval_(sf, expr, /):
        return safe_eval(expr)
    def iter_read_line_values_(sf, /):
        if not sf.setting.line_sep == '\n':
            # read, buffer, split ...
            raise NotImplementedError
        ifile = sf.text_iofile
        ifile.seek(0, SEEK_SET)
        for line in ifile:
            line_value = sf.safe_eval_(line)
            yield line_value

class IValidatableLineContinueIO(LineContinueIO):
    #@classmethod
    #def from_path_(cls, may_setting, path, /, *, allow_create=False):
    #@optional
    def iter_generate_continuity_infos(sf, /):
        raise NotImplementedError
    #@optional
    def line_value2may_iter_regenerate_continuity_infos_(sf, line_value, /):
        return None
        raise NotImplementedError
    #@optional
    def validate_line_value_payload_(sf, line_value, /):
        raise NotImplementedError
    #@optional
    def validate_line_value_continuity_info_(sf, line_value, continuity_info, /):
        raise NotImplementedError
    def validate_whole_file_(sf, /, *, to_validate_continuity, to_validate_payload):
        if not (to_validate_continuity or to_validate_payload):
            return
        #iter_infos = sf.iter_generate_continuity_infos() if to_validate_continuity else repeat(None)
        if to_validate_continuity:
            iter_infos = sf.iter_generate_continuity_infos()
                #init
            assert iter(iter_infos) is iter_infos
        for line_value in sf.iter_read_line_values_():
            if to_validate_continuity:
                for continuity_info in iter_infos:
                    break
                else:
                    raise Mismatch__line_value_with_no_continuity_info(line_value)
                sf.validate_line_value_continuity_info_(line_value, continuity_info)
                m = sf.line_value2may_iter_regenerate_continuity_infos_(line_value)
                if not m is None:
                    iter_infos = m
                        # regenerate/update/branch
                    assert iter(iter_infos) is iter_infos
            if to_validate_payload:
                sf.validate_line_value_payload_(line_value)

class Mismatch__line_value_with_no_continuity_info(Exception):pass
__all__


from seed.io.continue_io import IncompleteLastLineError
from seed.io.continue_io import LineContinueIO, IValidatableLineContinueIO
from seed.io.continue_io import Setting4LineContinueIO, setting4LineContinueIO__newline_utf8

from seed.io.continue_io import IncompleteLastLineError, Setting4LineContinueIO, LineContinueIO, IValidatableLineContinueIO
from seed.io.continue_io import *
