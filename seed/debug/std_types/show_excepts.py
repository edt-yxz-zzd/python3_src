
__all__ = '''
    show_dict
    Obj2Vars
    ShowExcepts
'''.split()


from pprint import pprint

class DotDotDot:
    def __repr__(self):
        return '<<... Hidden ...>>'
ddd = DotDotDot()
def show_dict(d, excepts):
    d = d.copy()
    for key in excepts:
        if key in d:
            d[key] = ddd
    pprint(d)
class Obj2Vars:
    def __init__(self, pred):
        # pred :: attr_name -> bool
        self.pred= pred
    def __call__(self, obj):
        return {name: getattr(obj, name) for name in dir(obj) if self.pred(name)}

class ShowExcepts(Obj2Vars):
    def __init__(self, pred, excepts):
        super().__init__(pred)
        self.excepts = tuple(excepts)
    def __call__(self, obj):
        d = super().__call__(obj)
        show_dict(d, self.excepts)



