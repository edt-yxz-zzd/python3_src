
__all__ = '''
    EmptyMapping
    empty_mapping
    empty_set
    empty_tuple
    empty_iterator
    '''.split()

from collections.abc import Mapping

class EmptyMapping(Mapping):
    def __getitem__(self, key):
        raise KeyError
    def __iter__(self):
        return empty_iterator
    def __len__(self):
        return 0
empty_mapping = EmptyMapping()
empty_set = frozenset()
empty_tuple = ()
empty_iterator = iter('')

