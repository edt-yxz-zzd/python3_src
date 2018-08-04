
class Make_IsIn:
    def __init__(self, obj_set):
        self.obj_set = obj_set
    def __call__(self, obj):
        return obj in self.obj_set

class ConcatPreds:
    def __init__(self, *preds):
        self.preds = preds
    def __call__(self, x):
        return all(pred(x) for pred in self.preds)
    
