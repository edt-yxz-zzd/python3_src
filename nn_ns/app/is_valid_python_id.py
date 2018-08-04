

__all__ = ('is_valid_python_id', 'is_valid_python_qual_id',
           'is_special_attrname', 'is_valid_special_attrname')

from keyword import iskeyword



def is_valid_python_id(name):
    return name.isidentifier() and not iskeyword(name)


def is_valid_python_qual_id(qual_name):
    return qual_name and all(map(is_valid_python_id, qual_name.split('.')))


def is_special_attrname(name):
    '''may not a vaild id;
NOTE: "__" is a special name

usage:
    when try to call a special name method
    use getattr(type(obj), name)(obj, ...) instead of getattr(obj, name)(...)
'''
    return '__' == name[:2] == name[-2:]

def is_valid_special_attrname(name):
    return is_special_attrname(name) and is_valid_python_id(name)



# test whether "__" is a special name
class xx:
    def __():pass
    def ___():pass
    def ____():pass
    def ___x_():pass
    def __x__():pass

	
assert set(['__', '___', '____', '__x__', '_xx___x_']) < set(dir(xx))
del xx







