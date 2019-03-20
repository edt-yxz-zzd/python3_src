
import sys

if False:
    from pathlib import Path
    this_folder = Path(__file__).parent
    path4libsvm = this_folder / 'libsvm-3.23' / 'python'
    path4pcv = this_folder / 'PCV-master[20140719]' / 'PCV-master'

    paths = [path4libsvm, path4pcv]
    sys.path[0:0] = map(str, (path.resolve() for path in paths))
    # MUST use 'str' instead of Path
import os.path
this_folder = os.path.dirname(__file__)
path4libsvm = os.path.join(this_folder, 'libsvm-3.23', 'python')
path4pcv = os.path.join(this_folder, 'PCV-master[20140719]', 'PCV-master')
paths = [path4libsvm, path4pcv]
sys.path[0:0] = paths


print(sys.path)
import svmutil

if False:
    # PCV is py2!!!!
    import examples
    import examples.ch8_svm_points



