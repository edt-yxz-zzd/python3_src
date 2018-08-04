
# 韵部检索_诗词吾爱网.py has some lines in string too long.
# so, we need this read_韵部检索_诗词吾爱网.py to read it.



# import ast
from itertools import chain
from pprint import pprint
from refine_classes import refine_classes


ifname = r'韵部检索_诗词吾爱网.py'
ofname = r'三合一韵部.py'

def read_module_file(ifname, *, module_name = '<string>', encoding='utf8'):
    with open(ifname, 'r', encoding=encoding) as fin:
        s = fin.read()
    obj = compile(s, module_name, 'exec')
    return obj
def exec_module_file(ifname, *, module_name = '<string>', encoding='utf8'):
    obj = read_module_file(ifname, module_name = module_name, encoding=encoding)
    g, local = {}, {}
    exec(obj, g, local)
    #rint(g)
    return local

def read_韵部检索_诗词吾爱网(ifname):
    module_name = '韵部检索_诗词吾爱网'
    local = exec_module_file(ifname, module_name = module_name)
    #rint(local.keys())
    #rint(local['yun_arr'].keys())
    #   ['psy', 'clzy', 'zhxy']

    yun_arr = local['yun_arr']
    psy = yun_arr['psy']
    clzy = yun_arr['clzy']
    zhxy = yun_arr['zhxy']
    #print(type(psy))


    strs = list(chain.from_iterable(map(dict.values, yun_arr.values())))
    #rint(strs)
    return yun_arr, strs

yun_arr, strs = read_韵部检索_诗词吾爱网(ifname)
############################################
############################################

# 共同字集

# chars_lsls :: [[str]]
chars_lsls = [list(cls2chars.values()) for cls2chars in yun_arr.values()]
def union_elems(elemss):
    s = set()
    return s.union(*elemss)
    return s
assert union_elems([[1], [2]]) == {1,2}
def collect_common_elems(elemss):
    it = iter(elemss)
    head = next(it, ())
    s = set(head)
    return s.intersection(*it)
    return s
def collect_common_elems_in_elemsss(elemsss):
    #rint(elemsss[0])
    #rint(union_elems(elemsss[0]))
    elemss = map(union_elems, elemsss)
    elemss = list(elemss)
    #rint(elemss)
    return collect_common_elems(elemss)

#rint(chars_lsls)
共同字集 = collect_common_elems_in_elemsss(chars_lsls)
def _remove_noncommon(chars):
    return set(chars) & 共同字集
chars_lsls2 = [[_remove_noncommon(chars) for chars in chars_ls]
                for chars_ls in chars_lsls]
from 多音字 import collect_multi
共同多音字 = union_elems(collect_multi(chars_ls) for chars_ls in chars_lsls2)
def join_to_str(s):
    return ''.join(sorted(s))
print(join_to_str(共同字集))
print(join_to_str(共同多音字))
assert join_to_str(共同多音字)[-1] == '龟'

############################################
############################################
# bug: 多音字！！！
def make_三合一韵部(strs):
    lsls = refine_classes(strs)
    result = sorted(''.join(sorted(ls)) for ls in lsls)
    result = sorted(result, key=lambda a: -len(a))
    #pprint(result)
    return result
三合一韵部 = make_三合一韵部(strs)
def write_三合一韵部(三合一韵部, ofname):
    with open(ofname, 'x', encoding='utf8') as fout:
        fout.write('三合一韵部 = \\\n')
        pprint(三合一韵部, stream = fout)
#write_三合一韵部(三合一韵部, ofname)

def read_三合一韵部(ofname):
    local = exec_module_file(ofname, module_name='三合一韵部')
    return local['三合一韵部']

assert 三合一韵部 == read_三合一韵部(ofname)

