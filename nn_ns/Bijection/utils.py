

__all__ = '''
    all_TypeVerifiers all_Bijections are_strs
    dict_value_map dict_value_map_with_key
    print_IO_of_BJs print_IO_of_BJ
    '''.split()
from .Bijection import Bijection
from .TypeVerifier import TypeVerifier


def print_IO_of_BJs(*bijections):
    for bj in bijections: print_IO_of_BJ(bj)
def print_IO_of_BJ(bijection):
    print(bijection.get_InputType().get_TypeName())
    print(bijection.get_OutputType().get_TypeName())


def all_of_Type(objs, Type):
    return all(isinstance(obj, Type) for obj in objs)
def all_TypeVerifiers(objs):
    return all_of_Type(objs, TypeVerifier)
def all_Bijections(objs):
    return all_of_Type(objs, Bijection)
def are_strs(objs):
    return all(type(x) == str for x in objs)

def dict_value_map(v2v, dict, items2dict=None):
    if items2dict is None:
        items2dict = type(dict)
    return items2dict((key, v2v(val)) for key, val in dict.items())
def dict_value_map_with_key(kv2v, dict, items2dict=None):
    if items2dict is None:
        items2dict = type(dict)
    return items2dict((key, kv2v(key, val)) for key, val in dict.items())

