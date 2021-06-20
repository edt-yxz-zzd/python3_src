r'''

nn_ns.filedir.inf_dir
py -m nn_ns.filedir.inf_dir

from nn_ns.filedir.inf_dir import inf_dir_idx2user_data_uint_relative_path, inf_dir_user_data_uint_relative_path2idx
from nn_ns.filedir.inf_dir import move_and_push_into_inf_dir, copy_and_push_into_inf_dir, pop_from_inf_dir_and_move, pop_from_inf_dir_and_push_into_another, inf_dir_remove_tail_empty_dirs, len_inf_dir, inf_dir_end_based_idx2user_data_path_ex
from nn_ns.filedir.inf_dir import bisearch_child_end, len_finite_dir_or_file, inf_dir_idx2user_data_relative_path, inf_dir_end_based_idx2user_data_relative_path_ex, inf_dir_end_based_idx2begin_based_idx
from nn_ns.filedir.inf_dir import open_under_inf_dir, mk_target_path_under_inf_dir




inf_dir
无限目录===stack<(usr_file|usr_dir)>{ordered, no_name}
无限目录 的 子 即是 海量的 用户包（=用户文件/用户文件夹）
    而 实际的 文件系统 的 目录 的 子代 数量 有上限，文件名 的 长度 也有上限
    所以 将 stack 保存成 有偏树状目录


无限目录 = 0级无限目录
用户包 = 用户文件/用户文件夹

紧致数组~[文件]~有偏树状目录
    #x,y #x=y-1
    #n级无限目录 下:x个有序的n级有限目录+1个(n+1)级无限目录
      #==>>本层 最多 含x*y^n个 用户包
      #==>>本层及祖辈累积 最多 含x*sum y^i {i<-[0..n]} = x*(y^(n+1)-1)/(y-1) = (y^(n+1)-1)个 用户包

    #有限目录
        #n级有限目录
          #==>> 最多 含y^n个 用户包

        #（0级有限目录=普通文件或用户文件夹=更新包）

        #n>0:n级有限目录 下:y个有序(n-1)级有限目录




>>> inf_dir_idx2user_data_uint_relative_path(0, dir_size=3)
(0,)
>>> inf_dir_idx2user_data_uint_relative_path(1, dir_size=3)
(1,)
>>> inf_dir_idx2user_data_uint_relative_path(2, dir_size=3)
(2, 0, 0)
>>> inf_dir_idx2user_data_uint_relative_path(3, dir_size=3)
(2, 0, 1)
>>> inf_dir_idx2user_data_uint_relative_path(4, dir_size=3)
(2, 0, 2)
>>> inf_dir_idx2user_data_uint_relative_path(5, dir_size=3)
(2, 1, 0)
>>> inf_dir_idx2user_data_uint_relative_path(6, dir_size=3)
(2, 1, 1)
>>> inf_dir_idx2user_data_uint_relative_path(7, dir_size=3)
(2, 1, 2)
>>> inf_dir_idx2user_data_uint_relative_path(8, dir_size=3)
(2, 2, 0, 0, 0)
>>> inf_dir_idx2user_data_uint_relative_path(9, dir_size=3)
(2, 2, 0, 0, 1)
>>> inf_dir_idx2user_data_uint_relative_path(10, dir_size=3)
(2, 2, 0, 0, 2)
>>> inf_dir_idx2user_data_uint_relative_path(11, dir_size=3)
(2, 2, 0, 1, 0)
>>> inf_dir_idx2user_data_uint_relative_path(12, dir_size=3)
(2, 2, 0, 1, 1)
>>> inf_dir_idx2user_data_uint_relative_path(13, dir_size=3)
(2, 2, 0, 1, 2)
>>> inf_dir_idx2user_data_uint_relative_path(14, dir_size=3)
(2, 2, 0, 2, 0)


#'''

__all__ = '''
    inf_dir_idx2user_data_uint_relative_path
    inf_dir_user_data_uint_relative_path2idx

    move_and_push_into_inf_dir
    copy_and_push_into_inf_dir
    inf_dir_remove_tail_empty_dirs
        pop_from_inf_dir_and_move
        pop_from_inf_dir_and_push_into_another

    inf_dir_end_based_idx2user_data_path_ex
        inf_dir_end_based_idx2user_data_relative_path_ex
            inf_dir_end_based_idx2begin_based_idx
                len_inf_dir
                    bisearch_child_end
                    len_finite_dir_or_file
            inf_dir_idx2user_data_relative_path

    open_under_inf_dir
        mk_target_path_under_inf_dir
            inf_dir_idx2user_data_relative_path

    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.int_tools.repr_uint import iter_reprdigits_BE2uint, uint2reprdigits_BE
from seed.int_tools.int_tools import is_odd

from pathlib import Path, PurePosixPath #as_posix
import os.path
import shutil
#from nn_ns.filedir.relative_path_ops import relative_path_ops, check_relative_path, is_relative_path_empty, relative_path2parts #avoid relative_path.parts
from nn_ns.filedir.filedir_ops import is_dir_empty, remove_dirs, filedir_move_then_remove_dirs, filedir_move, filedir_copy
___end_mark_of_excluded_global_names__0___ = ...


def bisearch_child_end(dir_path, /,*, end, begin=0):
    r''':: dir_path -> (end) -> (begin=0) -> child_end

    assume for mid <- [begin..child_end-1]: exists(dir_path / repr(mid))
    assume for mid <- [child_end..end-1]: not exists(dir_path / repr(mid))

    # end=dir_size
    #'''
    if begin is None:
        begin = 0
    if type(begin) is not int: raise TypeError
    if type(end) is not int: raise TypeError
    if not 0 <= begin <= end: raise ValueError
    while begin < end:
        mid = (begin+end)//2
        assert begin <= mid < end
        mid_child_path = dir_path / repr(mid)
        if mid_child_path.exists():
            begin = mid+1
        else:
            end = mid
    assert begin == end
    child_end = begin
    return child_end

def len_finite_dir_or_file(finite_dir_or_file_path, /,*, dir_size, level, min_len):
    if type(dir_size) is not int: raise TypeError
    if not dir_size >= 2: raise ValueError
    if type(level) is not int: raise TypeError
    if not level >= 0: raise ValueError
    if type(min_len) is not int: raise TypeError
    if not min_len >= 0: raise ValueError

    if not finite_dir_or_file_path.exists(): raise FileNotFoundError(finite_dir_or_file_path)

    def recur(level, finite_dir_or_file_path, /,*, min_len):
        saved_min_len = min_len
        if not (level==0 or finite_dir_or_file_path.is_dir()): raise NotADirectoryError(finite_dir_or_file_path)
        if level==0:
            # user file/dir
            if not 0 <= min_len <= 1: raise ValueError
            return 1
        assert level > 0
        finite_dir_path = finite_dir_or_file_path
        assert finite_dir_path.is_dir()

        child_finite_dir_full_sz = dir_size**(level-1)
        this_finite_dir_full_sz = dir_size*child_finite_dir_full_sz
        if not 0 <= min_len <= this_finite_dir_full_sz: raise ValueError
        begin = min_len//child_finite_dir_full_sz
        assert 0 <= begin <= dir_size
        child_end = bisearch_child_end(finite_dir_path, begin=begin, end=dir_size)
        assert child_end==dir_size or not (finite_dir_path/repr(child_end)).exists()
            #assert not (finite_dir_path/repr(child_end)).exists()
            #in inf_dir logic: ./{dir_size} does not exists
            #but ... user may use this path for another usage
        assert not child_end or (finite_dir_path/repr(child_end-1)).exists()
        assert 0 <= begin <= child_end <= dir_size #==end

        num_children = child_end
            #<<==# ./{child_end} not exists in logic

        #if child_end == 0: return 0
        #elif begin == child_end:
        if begin == child_end:
            # ./{child_end} not exists in logic
            # ==>> [0..begin-1] are all full
            # ==>> [0..child_end-1] are all full
            num_full_children = num_children
            full_sz = num_full_children*child_finite_dir_full_sz
            non_full_sz = 0
            pass
        else:
            assert 0 <= begin < child_end <= dir_size #==end
            # ./{child_end} not exists in logic
            # ==>> [0..child_end-2] are all full
            # ==>> child_end-1 may mot be full
            num_full_children = num_children-1
            child_last = child_end-1
            assert 0 <= num_full_children==child_last < dir_size
            try:
                assert 0 <= begin <= num_full_children==child_last == child_end-1 < child_end <= dir_size
            except AssertionError:
                if 0:#[01_to_turn_off)
                    print(fr'assert 0 <= {begin} <= {num_full_children}=={child_last} == {child_end-1} < {child_end} <= {dir_size}')
                raise
            child_last__may_not_full = child_last

            full_sz = num_full_children * child_finite_dir_full_sz
            min_len = max(0, min_len-full_sz)
            non_full_sz = recur(level-1, finite_dir_path/repr(child_last__may_not_full), min_len=min_len)
                # level-1
            pass
        full_sz
        non_full_sz

        if 0:#[01_to_turn_off)
            #print(fr'x={x}')
            print(fr'len_finite_dir_or_file(level={level}, finite_dir_or_file_path={finite_dir_or_file_path}, min_len={saved_min_len})')
            print(fr'    full_sz={full_sz}')
            print(fr'    non_full_sz={non_full_sz}')
            if begin == child_end:
                print(fr'    begin=child_end={child_end}')
                print(fr'    min_len={saved_min_len}')
                print(fr'    child_finite_dir_full_sz={child_finite_dir_full_sz}')
        whole_sz = full_sz + non_full_sz
        assert whole_sz >= saved_min_len #01_to_turn_off
        return whole_sz

    return recur(level, finite_dir_or_file_path, min_len=min_len)


def len_inf_dir(inf_dir_path, /,*, dir_size, level, min_len):
    if type(dir_size) is not int: raise TypeError
    if not dir_size >= 2: raise ValueError
    if type(level) is not int: raise TypeError
    if not level >= 0: raise ValueError
    if type(min_len) is not int: raise TypeError
    if not min_len >= 0: raise ValueError

    if not inf_dir_path.exists(): raise FileNotFoundError(inf_dir_path)

    def recur(level, inf_dir_path, /,*, min_len):
        saved_min_len = min_len
        if not inf_dir_path.is_dir(): raise NotADirectoryError(inf_dir_path)

        child_finite_dir_full_sz = dir_size**level
        this_level_full_sz = (dir_size-1) * child_finite_dir_full_sz
        next_level_inf_dir_path = inf_dir_path / repr(dir_size-1)
        if next_level_inf_dir_path.exists():
            init_sz4finite = this_level_full_sz
            min_len = max(0, min_len-init_sz4finite)
            tail_sz4inf = recur(level+1, next_level_inf_dir_path, min_len=min_len)
                #level+1
            pass

        else:
            init_sz4finite = len_finite_dir_or_file(inf_dir_path, dir_size=dir_size, level=level+1, min_len=min_len)
                #level+1
            tail_sz4inf = 0
            pass
        init_sz4finite
        tail_sz4inf

        if 0:#[01_to_turn_off)
            #print(fr'x={x}')
            print(fr'len_inf_dir(level={level}, inf_dir_path={inf_dir_path}, min_len={saved_min_len})')
            print(fr'    init_sz4finite={init_sz4finite}')
            print(fr'    tail_sz4inf={tail_sz4inf}')
        whole_sz = init_sz4finite + tail_sz4inf
        assert whole_sz >= saved_min_len #01_to_turn_off
        return whole_sz

    return recur(level, inf_dir_path, min_len=min_len)






def copy_and_push_into_inf_dir(*, from_path, into_inf_dir_path, dir_size, min_len, imay_inf_dir_idx4assert):
    '-> inf_dir_idx'
    def copy_or_move(*, from_path, inf_dir_end_user_data_path):
        filedir_copy(from_path=from_path, to_path=inf_dir_end_user_data_path)

    inf_dir_idx = _copy_or_move_and_push_into_inf_dir(copy_or_move, from_path=from_path, into_inf_dir_path=into_inf_dir_path, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert)
    return inf_dir_idx



def move_and_push_into_inf_dir(*, from_path, into_inf_dir_path, dir_size, min_len, imay_inf_dir_idx4assert):
    '-> inf_dir_idx'
    def copy_or_move(*, from_path, inf_dir_end_user_data_path):
        filedir_move(from_path=from_path, to_path=inf_dir_end_user_data_path)

    inf_dir_idx = _copy_or_move_and_push_into_inf_dir(copy_or_move, from_path=from_path, into_inf_dir_path=into_inf_dir_path, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert)
    return inf_dir_idx

def _copy_or_move_and_push_into_inf_dir(copy_or_move, *, from_path, into_inf_dir_path, dir_size, min_len, imay_inf_dir_idx4assert):
    '-> inf_dir_idx'
    (inf_dir_user_data_path, inf_dir_idx) = inf_dir_end_based_idx2user_data_path_ex(into_inf_dir_path, 0, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert, positive_end_based_idx_ok=False)

    #since inf_dir_end_based_idx==0
    (inf_dir_end_user_data_path, inf_dir_end_idx) = (inf_dir_user_data_path, inf_dir_idx)

    if inf_dir_end_user_data_path.exists():raise logic-err

    copy_or_move(from_path=from_path, inf_dir_end_user_data_path=inf_dir_end_user_data_path)

    return inf_dir_idx

def pop_from_inf_dir_and_move(*, to_path, from_inf_dir_path, dir_size, min_len, imay_inf_dir_idx4assert):
    '-> inf_dir_idx'
    inf_dir_remove_tail_empty_dirs(from_inf_dir_path, dir_size=dir_size, min_len=min_len)

    (inf_dir_user_data_path, inf_dir_idx) = inf_dir_end_based_idx2user_data_path_ex(from_inf_dir_path, -1, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert, positive_end_based_idx_ok=False)

    #since inf_dir_end_based_idx==-1
    (inf_dir_last_user_data_path, inf_dir_last_idx) = (inf_dir_user_data_path, inf_dir_idx)

    if not inf_dir_last_user_data_path.exists():raise logic-err

    filedir_move_then_remove_dirs(to_path=to_path, from_path=inf_dir_last_user_data_path, may_root_dir_path4from=from_inf_dir_path, exist_ok=False)
        #pop? what now len_inf_dir change???
        #   shouldnot concurrent

    return inf_dir_idx
def pop_from_inf_dir_and_push_into_another(*, inf_dir_path4into, inf_dir_path4from, dir_size4into, dir_size4from, min_len4into, min_len4from, imay_inf_dir_idx4assert4into, imay_inf_dir_idx4assert4from):
    '-> (inf_dir_idx4into, inf_dir_idx4from)'
    inf_dir_remove_tail_empty_dirs(inf_dir_path4from, dir_size=dir_size4from, min_len=min_len4from)

    (inf_dir_user_data_path4into, inf_dir_idx4into) = inf_dir_end_based_idx2user_data_path_ex(inf_dir_path4into, 0, dir_size=dir_size4into, min_len=min_len4into, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert4into, positive_end_based_idx_ok=False)

    #since inf_dir_end_based_idx==0
    (inf_dir_end_user_data_path4into, inf_dir_end_idx4into) = (inf_dir_user_data_path4into, inf_dir_idx4into)

    if inf_dir_end_user_data_path4into.exists():raise logic-err

    inf_dir_idx4from = pop_from_inf_dir_and_move(to_path=inf_dir_end_user_data_path4into, from_inf_dir_path=inf_dir_path4from, dir_size=dir_size4from, min_len=min_len4from, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert4from)

    return (inf_dir_idx4into, inf_dir_idx4from)

def inf_dir_remove_tail_empty_dirs(inf_dir_path, /,*, dir_size, min_len):
    'clean up'
    (inf_dir_user_data_path, inf_dir_idx) = inf_dir_end_based_idx2user_data_path_ex(inf_dir_path, 0, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=-1, positive_end_based_idx_ok=False)

    #since inf_dir_end_based_idx==0
    (inf_dir_end_user_data_path, inf_dir_end_idx) = (inf_dir_user_data_path, inf_dir_idx)

    assert not inf_dir_end_user_data_path.exists()
        #inf_dir_end_user_data_path.parent may not exists too!!!
    if 1:
        remove_dirs(inf_dir_end_user_data_path.parent, may_root_dir_path=inf_dir_path, missing_ok=True, target_dir_nonempty_ok2halt=True, target_dir_nonempty_ok2remove=False, target_path_is_file_ok2remove=False, target_path_is_file_ok2halt=False, target_dir_path_is_root_dir_path_ok=True)
            #inf_dir_end_user_data_path.parent may not exists too!!!
                #==>>missing_ok=True
    else:
        remove_dirs(inf_dir_end_user_data_path, may_root_dir_path=inf_dir_path, missing_ok=True, target_dir_nonempty_ok2halt=False, target_dir_nonempty_ok2remove=False, target_path_is_file_ok2remove=False, target_path_is_file_ok2halt=False, target_dir_path_is_root_dir_path_ok=False)
            #inf_dir_end_user_data_path not exists
                #==>>missing_ok=True




#mk_end_path__of_inf_dir_ex
#inf_dir_end_based_idx2user_data_path_ex
def inf_dir_end_based_idx2user_data_path_ex(inf_dir_path, inf_dir_end_based_idx, /,*, dir_size, min_len, imay_inf_dir_idx4assert, positive_end_based_idx_ok):
    '-> (inf_dir_user_data_path, inf_dir_idx)'
    (inf_dir_user_data_relative_path, inf_dir_idx) = inf_dir_end_based_idx2user_data_relative_path_ex(inf_dir_path, inf_dir_end_based_idx, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert, positive_end_based_idx_ok=positive_end_based_idx_ok)

    inf_dir_user_data_path = inf_dir_path / inf_dir_user_data_relative_path
    return inf_dir_user_data_path, inf_dir_idx

#mk_end_relative_path__of_inf_dir_ex
#inf_dir_end_based_idx2user_data_relative_path_ex
def inf_dir_end_based_idx2user_data_relative_path_ex(inf_dir_path, inf_dir_end_based_idx, /,*, dir_size, min_len, imay_inf_dir_idx4assert, positive_end_based_idx_ok):
    '-> (inf_dir_user_data_relative_path, inf_dir_idx)'
    inf_dir_begin_based_idx = inf_dir_end_based_idx2begin_based_idx(inf_dir_path, inf_dir_end_based_idx, dir_size=dir_size, min_len=min_len, imay_inf_dir_idx4assert=imay_inf_dir_idx4assert, positive_end_based_idx_ok=positive_end_based_idx_ok, negative_begin_based_idx_ok=False)

    inf_dir_idx = inf_dir_begin_based_idx

    inf_dir_user_data_relative_path = inf_dir_idx2user_data_relative_path(inf_dir_idx, dir_size=dir_size)
    return (inf_dir_user_data_relative_path, inf_dir_idx)

def inf_dir_end_based_idx2begin_based_idx(inf_dir_path, inf_dir_end_based_idx:'=offset_from_end', /,*, dir_size, min_len, imay_inf_dir_idx4assert, negative_begin_based_idx_ok, positive_end_based_idx_ok):
    r'''-> inf_dir_idx
    inf_dir_idx==inf_dir_begin_based_idx==inf_dir_end_idx+offset_from_end
    offset_from_end==inf_dir_end_based_idx
    ###
    used scene:
        nn_ns.filedir.backup_util::move_cmd
            pop idx -> push idx
                #required: inf_dir_idx4assert
    #'''
    if type(negative_begin_based_idx_ok) is not bool: raise TypeError
    if type(positive_end_based_idx_ok) is not bool: raise TypeError

    if type(imay_inf_dir_idx4assert) is not int: raise TypeError
    if not imay_inf_dir_idx4assert >= -1: raise ValueError

    if type(inf_dir_end_based_idx) is not int: raise TypeError
    if inf_dir_end_based_idx > 0 and not positive_end_based_idx_ok: raise ValueError

    inf_dir_end_idx = len_inf_dir(inf_dir_path, dir_size=dir_size, level=0, min_len=min_len)
    inf_dir_begin_based_end_idx = inf_dir_end_idx

    offset_from_end = inf_dir_end_based_idx
    inf_dir_begin_based_idx = inf_dir_begin_based_end_idx + offset_from_end

    if inf_dir_begin_based_idx < 0 and not negative_begin_based_idx_ok: raise ValueError

    if imay_inf_dir_idx4assert != -1:
        inf_dir_idx4assert = imay_inf_dir_idx4assert
        inf_dir_idx = inf_dir_begin_based_idx
        try:
            if inf_dir_idx != inf_dir_idx4assert: raise ValueError
        except ValueError:
            if 0:#[01_to_turn_off)
                print(fr'inf_dir_idx4assert={inf_dir_idx4assert}')
                print(fr'inf_dir_idx={inf_dir_idx}')
                print(fr'inf_dir_begin_based_end_idx={inf_dir_begin_based_end_idx}')
                print(fr'offset_from_end={offset_from_end}')
                quit()
            raise

    return inf_dir_begin_based_idx




#relative_to()
def mk_target_path_under_inf_dir(inf_dir_path, inf_dir_idx, may_target_path_relative_to_user_data_dir, /,*, dir_size):
    inf_dir_user_data_relative_path = inf_dir_idx2user_data_relative_path(inf_dir_idx, dir_size=dir_size)
    inf_dir_user_data_path = inf_dir_path / inf_dir_user_data_relative_path

    #the_target_path :=
    if may_target_path_relative_to_user_data_dir is None:
        inf_dir_user_data_path # dir/file
        the_target_path = inf_dir_user_data_path
    else:
        target_path_relative_to_user_data_dir = may_target_path_relative_to_user_data_dir
        user_data_dir_path = inf_dir_user_data_path
        the_target_path = user_data_dir_path / target_path_relative_to_user_data_dir
    the_target_path # dir/file

    return the_target_path

def open_under_inf_dir(dir_size, inf_dir_path, inf_dir_idx, may_target_file_path_relative_to_user_data_dir, open_mode, /, **open_kwargs):
    may_target_path_relative_to_user_data_dir = may_target_file_path_relative_to_user_data_dir
    if 1:
        the_target_path = mk_target_path_under_inf_dir(inf_dir_path, inf_dir_idx, may_target_path_relative_to_user_data_dir, dir_size=dir_size)
    the_target_file_path = the_target_path

    return open(the_target_file_path, open_mode, **open_kwargs)



#mk_relative_path__from_inf_dir_idx
#inf_dir_idx2user_data_relative_path
def inf_dir_idx2user_data_relative_path(inf_dir_idx, /,*, dir_size):
    inf_dir_user_data_uint_relative_path = inf_dir_idx2user_data_uint_relative_path(inf_dir_idx, dir_size=dir_size)
    #.as_posix()
    inf_dir_user_data_relative_path = PurePosixPath(*map(repr, inf_dir_user_data_uint_relative_path))
    return inf_dir_user_data_relative_path


def inf_dir_idx2user_data_uint_relative_path(inf_dir_idx, /,*, dir_size):
    r'''
    dir_size{>=2} -> inf_dir_idx{>=0} -> inf_dir_user_data_uint_relative_path::[uint%dir_size]{len=2*n+1}

    dir_size - radix; repr actual fsys dir limit
    inf_dir_idx - stack[inf_dir_idx]
    inf_dir_user_data_uint_relative_path - to mk actual inf_dir_user_data_relative_path to cd into
        inf_dir_user_data_path == inf_dir_path / inf_dir_user_data_relative_path

    n:
        dir_size^n <= inf_dir_idx+1 < dir_size^(n+1)
        n = floor_log(dir_size, inf_dir_idx+1)
        ==>> inside n-level inf_dir
            inf_dir_user_data_uint_relative_path = [dir_size-1]*n ++ ...

    idx@n:
        idx@n = inf_dir_idx - (dir_size^n-1)
        0 <= idx@n < dir_size^(n+1) - dir_size^n
        tail_of_finite_dir_user_data_uint_relative_path = uint2reprdigits_BE(idx@n, radix=dir_size)
            0 <= len(tail_of_finite_dir_user_data_uint_relative_path) <= n+1
            not tail_of_finite_dir_user_data_uint_relative_path or 0 < tail_of_finite_dir_user_data_uint_relative_path[0] < dir_size #not dir_size-1 !
                # ==>> 1 < dir_size
                # ==>> dir_size >= 2
            len(tail_of_finite_dir_user_data_uint_relative_path) != n+1 or 0 < tail_of_finite_dir_user_data_uint_relative_path[0] < dir_size-1
                # ==>> len(tail) <= n or 1 < dir_size-1
                # ==>> dir_size >= 3 or len(tail) <= n
                # ==>> [dir_size == 2] --> [len(tail) <= n]

    finite_dir_user_data_uint_relative_path = [0]*(n+1-len(tail_of_finite_dir_user_data_uint_relative_path)) ++ tail_of_finite_dir_user_data_uint_relative_path
        len(finite_dir_user_data_uint_relative_path) == n+1
        new algo:
            _p1_finite_dir_user_data_uint_relative_path = uint2reprdigits_BE(inf_dir_idx+1, radix=dir_size)
            len(_p1_finite_dir_user_data_uint_relative_path) == n+1
        finite_dir_user_data_uint_relative_path = [_p1_finite_dir_user_data_uint_relative_path[0]-1, *_p1_finite_dir_user_data_uint_relative_path[1:]]

    inf_dir_user_data_uint_relative_path = [dir_size-1]*n ++ finite_dir_user_data_uint_relative_path
    len(inf_dir_user_data_uint_relative_path) == 2*n+1


    #'''
    if type(dir_size) is not int: raise TypeError
    if not dir_size >= 2: raise ValueError

    if type(inf_dir_idx) is not int: raise TypeError
    if not inf_dir_idx >= 0: raise ValueError

    _p1_finite_dir_user_data_uint_relative_path = uint2reprdigits_BE(inf_dir_idx+1, radix=dir_size)
    assert _p1_finite_dir_user_data_uint_relative_path
    assert _p1_finite_dir_user_data_uint_relative_path[0]

    n = len(_p1_finite_dir_user_data_uint_relative_path)-1
    assert n >= 0

    inf_dir_user_data_uint_relative_path = (*[dir_size-1]*n, _p1_finite_dir_user_data_uint_relative_path[0]-1, *_p1_finite_dir_user_data_uint_relative_path[1:])
    assert len(inf_dir_user_data_uint_relative_path) == 2*n+1
    assert all(0 <= u < dir_size for u in inf_dir_user_data_uint_relative_path)

    assert inf_dir_idx == inf_dir_user_data_uint_relative_path2idx(inf_dir_user_data_uint_relative_path, dir_size=dir_size)
    return inf_dir_user_data_uint_relative_path









def inf_dir_user_data_uint_relative_path2idx(inf_dir_user_data_uint_relative_path, /,*, dir_size):
    if type(dir_size) is not int: raise TypeError
    if not dir_size >= 2: raise ValueError

    if type(inf_dir_user_data_uint_relative_path) is not tuple: raise TypeError
    if not is_odd(len(inf_dir_user_data_uint_relative_path)): raise ValueError
    if not all(type(u) is int for u in inf_dir_user_data_uint_relative_path): raise TypeError
    if not all(0 <= u < dir_size for u in inf_dir_user_data_uint_relative_path): raise ValueError


    n = len(inf_dir_user_data_uint_relative_path)//2
    assert len(inf_dir_user_data_uint_relative_path) == 2*n+1

    if not inf_dir_user_data_uint_relative_path[:n] == (dir_size-1,)*n: raise ValueError
    if not 0 <= inf_dir_user_data_uint_relative_path[n] <= dir_size-2: raise ValueError

    _p1_finite_dir_user_data_uint_relative_path = (inf_dir_user_data_uint_relative_path[n]+1, *inf_dir_user_data_uint_relative_path[n+1:])
    assert len(_p1_finite_dir_user_data_uint_relative_path) == n+1

    inf_dir_idx = -1+iter_reprdigits_BE2uint(_p1_finite_dir_user_data_uint_relative_path, radix=dir_size)

    assert inf_dir_idx >= 0
    return inf_dir_idx


def _t():
    dir_size = 3
    paths = \
[(0,)
,(1,)
,(2, 0, 0)
,(2, 0, 1)
,(2, 0, 2)
,(2, 1, 0)
,(2, 1, 1)
,(2, 1, 2)
,(2, 2, 0, 0, 0)
,(2, 2, 0, 0, 1)
,(2, 2, 0, 0, 2)
,(2, 2, 0, 1, 0)
,(2, 2, 0, 1, 1)
,(2, 2, 0, 1, 2)
,(2, 2, 0, 2, 0)
,(2, 2, 0, 2, 1)
,(2, 2, 0, 2, 2)
,(2, 2, 1, 0, 0)
,(2, 2, 1, 0, 1)
,(2, 2, 1, 0, 2)
,(2, 2, 1, 1, 0)
,(2, 2, 1, 1, 1)
,(2, 2, 1, 1, 2)
,(2, 2, 1, 2, 0)
,(2, 2, 1, 2, 1)
,(2, 2, 1, 2, 2)
,(2, 2, 2, 0, 0, 0, 0)
,(2, 2, 2, 0, 0, 0, 1)
,(2, 2, 2, 0, 0, 0, 2)
,(2, 2, 2, 0, 0, 1, 0)
]
    for inf_dir_idx in range(30):
        inf_dir_user_data_uint_relative_path = inf_dir_idx2user_data_uint_relative_path(inf_dir_idx, dir_size=dir_size)
        assert inf_dir_idx == inf_dir_user_data_uint_relative_path2idx(inf_dir_user_data_uint_relative_path, dir_size=dir_size)
        #print(f',{inf_dir_user_data_uint_relative_path}')
        assert inf_dir_user_data_uint_relative_path == paths[inf_dir_idx]

if __name__ == "__main__":
    _t()
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#HHHHH
if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())






