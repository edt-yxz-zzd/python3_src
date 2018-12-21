
__all__ = '''
    Enum__NoShowValue
    '''.split()

import enum
class Enum__NoShowValue(enum.Enum):
    def __repr__(self):
        C = type(self).__name__
        N = self.name
        return f'<{C}.{N}>'
