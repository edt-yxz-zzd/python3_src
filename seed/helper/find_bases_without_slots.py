
__all__ = '''
    find_bases_without_slots
    print_bases_without_slots
    '''.split()

def print_bases_without_slots(*classes):
    print('bases_without_slots:')
    for cls in find_bases_without_slots(*classes):
        print(f'\t{cls}')

def find_bases_without_slots(*classes):
    s = set()
    done_classes = set()
    Nothing = []

    for cls in classes:
        if not isinstance(cls, type): raise TypeError(cls)
        if cls in done_classes: continue

        '''
        try:
            mro = cls.mro()
        except:
            print(cls) # fail for abc.ABCMeta
            raise
        '''

        mro = cls.__mro__
        for base in mro:
            if base in done_classes: continue
            done_classes.add(base)

            may_slots = base.__dict__.get('__slots__', Nothing)
            if may_slots is Nothing or not hasattr(type(may_slots), '__iter__'):
                s.add(base)
    s.discard(object)
    return s

#print(find_bases_without_slots(object))
assert not find_bases_without_slots(object)

class A:
    __slots__ = ()
class B:pass
assert not find_bases_without_slots(A)
assert find_bases_without_slots(B) == {B}
del A, B


