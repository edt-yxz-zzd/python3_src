
'''
used in ImmutableNamespaceBase
'''

__all__ = '''
    NamedReadOnlyProperty
    '''.split()

from seed.helper.repr_input import repr_helper

class NamedReadOnlyProperty:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    # MUST define "__set__" to make self a data_descriptor
    #   otherwise, instance override self
    def __set__(self, instance, value):
        raise AttributeError(self.name)
    def __delete__(self, instance):
        raise AttributeError(self.name)
    def __repr__(self):
        return repr_helper(self, self.name)



