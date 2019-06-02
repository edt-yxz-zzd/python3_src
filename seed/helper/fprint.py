

class fprint:
    def __init__(self, file, **kwargs):
        self.file = file
        self.kwargs = kwargs
    def print(self, *args, **kwargs):
        print(*args, file=self.file, **self.kwargs, **kwargs)
    def __call__(self, *args, **kwargs):
        self.print(*args, **kwargs)

