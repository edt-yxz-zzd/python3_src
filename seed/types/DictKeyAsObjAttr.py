

class DictKeyAsObjAttr:
    def __init__(self, globals):
        self.globals = globals
    def __getattribute__(self, name):
        d = object.__getattribute__(self, 'globals')
        try:
            return d[name]
        except KeyError:
            raise AttributeError(name)
    def __dir__(self):
        d = object.__getattribute__(self, 'globals')
        return [k for k in d if k.isidentifier()]
