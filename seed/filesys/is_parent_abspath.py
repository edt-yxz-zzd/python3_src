
__all__ = ['is_parent_abspath']
import os
def is_parent_abspath(parent_abspath, child_abspath):
    if not parent_abspath:
        raise ValueError('not a path : empty??')
    if child_abspath.startswith(parent_abspath):
        # NOTE: child_abspath may not in parent_abspath
        # unless tail starts with a seperator...
        tail = child_abspath[len(parent_abspath):]

        # assert '/sf' == os.path.join('a', '/sf')
        # assert r'a\sf' == os.path.join('a', 'sf')
        new = os.path.join(parent_abspath, tail)
        #print(new, tail, parent, child)
        if new == tail:
            # startswith a seperater
            return True
        elif len(new) > len(child_abspath):
            # introduce a new seperator
            return False
        else:
            raise logic-error
    return False
child = r'E:\my_data\program_source\windows_bat\[20160322]windows_bat.7z'
parent = r'E:\my_data\program_source\windows_bat'
assert r'\b' == os.path.join('a', r'\b')
for parent, child in [(parent, child), ('ab', r'ab\b')]:
    assert is_parent_abspath(parent, child)
    assert not is_parent_abspath(parent[:-1], child)
del parent, child



