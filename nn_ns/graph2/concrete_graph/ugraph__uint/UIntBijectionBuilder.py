
__all__ = '''
    UIntBijectionBuilder
    '''.split()

from .UIntBijection import UIntBijection

class UIntBijectionBuilder:
    def __init__(self, size):
        assert type(size) is int
        assert size >= 0
        self.size = size
        self.new2old = []
        self.old2new = [None]*size
        self.maybe_uint_bijection = None
    def is_old_uint_visited(self, old_uint):
        return self.old2new[old_uint] is not None
    def may_visit_next_old_uint(self, old_uint):
        self.visit_next_old_uint(old_uint, allow_duplicate=True)
    def visit_next_old_uint(self, old_uint, allow_duplicate=False):
        assert type(old_uint) is int
        if not 0 <= old_uint < self.size: raise ValueError

        if self.is_old_uint_visited(old_uint):
            if allow_duplicate: return
            raise ValueError('duplicate old_uint')
        if self.maybe_uint_bijection is not None: raise Exception('too many old_uint')

        new_uint = len(self.new2old)
        self.old2new[old_uint] = new_uint
        self.new2old.append(old_uint)
        if len(self.new2old) == self.size:
            self.maybe_uint_bijection = UIntBijection(forward_mapping=self.old2new, backward_mapping=self.new2old)

    def to_uint_bijection__old2new(self):
        if self.maybe_uint_bijection is None: raise Exception('too few old_uint')
        uint_bijection = self.maybe_uint_bijection
        return uint_bijection


