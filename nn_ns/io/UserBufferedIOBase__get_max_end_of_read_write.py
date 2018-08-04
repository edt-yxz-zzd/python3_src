

__all__ = '''
    UserBufferedIOBase__get_max_end_of_read_write
    '''.split()



from .IUserBufferedIOBase import UserBufferedIOBase, IUserBufferedIOBase__aspect

class UserBufferedIOBase__get_max_end_of_read_write(
        UserBufferedIOBase
        , IUserBufferedIOBase__aspect):
    def __init__(self, io):
        super().__init__(io)
        self.__max_end = self.tell()

    @property
    def max_end(self):
        return self.__max_end
    def update_max_end(self):
        pos = self.tell()
        if pos > self.max_end:
            self.__max_end = pos



    def before_io(self):
        return
    def after_io(self):
        self.update_max_end()
        return

