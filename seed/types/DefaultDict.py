
from collections import MutableMapping

curryDefaultDict = lambda mapping: lambda default_factory:\
                     DefaultDict(mapping, default_factory)
class DefaultDict(MutableMapping):
    def __init__(self, mapping, default_factory):
        self.mapping = mapping
        self.default_factory = type(None) if default_factory is None \
                               else default_factory

    def __getitem__(self, key):
        try:
            return self.mapping[key]
        except KeyError:
            self[key] = self.default_factory()
            return self.mapping[key]
    def __setitem__(self, key, value):
        self.mapping[key] = value
    def __delitem__(self, key):
        del self.mapping[key]

    def __iter__(self):
        return iter(self.mapping)
    def __len__(self):
        return len(self.mapping)

del MutableMapping




