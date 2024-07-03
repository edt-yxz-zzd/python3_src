
#e ../../python3_src/seed/data_funcs/finger_tree__errors.py

class 错误牜展翅树相关(Exception):pass
class 错误牜欤已知非超前进(错误牜展翅树相关):pass
class 错误牜空树(错误牜展翅树相关):pass

class Error4FingerTree(Exception):pass
class Error__empty_tree(Error4FingerTree):pass
class Error__known_non_overflow(Error4FingerTree):pass
            # ===错误牜欤已知非超前进


from seed.data_funcs.finger_tree__errors import 错误牜展翅树相关,错误牜欤已知非超前进,错误牜空树
from seed.data_funcs.finger_tree__errors import Error4FingerTree, Error__empty_tree, Error__known_non_overflow
