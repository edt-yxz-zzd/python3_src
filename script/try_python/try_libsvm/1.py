
'''
from C:\Python36\Lib\site-packages\libsvm-3.23\python\README
'''


def show_len(names):
    names = list(names)
    print(names)
    d = globals()
    for name in names:
        value = d[name]
        print(f'\tlen({name})={len(value)}')

def show(names):
    names = list(names)
    print(names)
    d = globals()
    for name in names:
        value = d[name]
        print(f'\t{name}={value!r}')
import svmutil
import os.path
the_libsvm_python_folder = os.path.dirname(svmutil.__file__)
the_libsvm_folder = os.path.dirname(the_libsvm_python_folder)


from svmutil import *
# Read data in LIBSVM format
y, x = svm_read_problem(os.path.join(the_libsvm_folder, 'heart_scale'))
m = svm_train(y[:200], x[:200], '-c 4')
p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)

show('m p_label p_acc p_val'.split())
print(); print()
show_len('y x p_label p_acc p_val'.split())
print(); print(); print(); print()


# Construct problem in python format
# Dense data
y, x = [1,-1], [[1,0,1], [-1,0,-1]]
# Sparse data
y, x = [1,-1], [{1:1, 3:1}, {1:-1,3:-1}]
prob  = svm_problem(y, x)
param = svm_parameter('-t 0 -c 4 -b 1')
m = svm_train(prob, param)

show('prob param m'.split())
print(); print(); print(); print()





# Precomputed kernel data (-t 4)
# Dense data
y, x = [1,-1], [[1, 2, -2], [2, -2, 2]]
# Sparse data
y, x = [1,-1], [{0:1, 1:2, 2:-2}, {0:2, 1:-2, 2:2}]
# isKernel=True must be set for precomputed kernel
prob  = svm_problem(y, x, isKernel=True)
param = svm_parameter('-t 4 -c 4 -b 1')
m = svm_train(prob, param)
# For the format of precomputed kernel, please read LIBSVM README.
show('prob param m'.split())
print(); print(); print(); print()


# Other utility functions
svm_save_model('heart_scale.model', m)
m = svm_load_model('heart_scale.model')
p_label, p_acc, p_val = svm_predict(y, x, m, '-b 1')
ACC, MSE, SCC = evaluations(y, p_label)

# Getting online help
help(svm_train)


from svm import *
prob = svm_problem([1,-1], [{1:1, 3:1}, {1:-1,3:-1}])
param = svm_parameter('-c 4')
m = libsvm.svm_train(prob, param) # m is a ctype pointer to an svm_model
# Convert a Python-format instance to svm_nodearray, a ctypes structure
x0, max_idx = gen_svm_nodearray({1:1, 3:1})
label = libsvm.svm_predict(m, x0)


