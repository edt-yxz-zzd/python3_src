


class FailAtPos(ValueError):
    def __init__(self, *args, pos, **kwargs):
        super().__init__(pos, kwargs, *args)
        self.pos = pos
        self.kwargs = kwargs
    pass
