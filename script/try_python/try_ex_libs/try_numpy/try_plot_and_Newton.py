
import numpy as np
import matplotlib.pyplot as plt


'''
Newton iteration

f''(r) = 0 = f(r), f'(r) > 0
f''(r-) > 0, f''(r+)<0


f'' = -2x + 2r
f' = -x**2 + 2rx + B ==>> B > -r**2
f = -x**3/3 + rx**2 + Bx + A
let B = 0
f' = -xx+2rx
f = -xxx/3+rxx+A
f(r) = 2rrr/3+A == 0
A = -2rrr/3
f = -xxx/3 + rxx - 2rrr/3 =
3f = -xxx + 3rxx - 2rrr = (x-r)(-xx) + 2rxx - 2rrr
= (x-r)(-xx) + 2r(xx - rr) = (x-r)[(-xx) + 2r(x+r)]
= (x-r)[xx - 2rx-2rr]
'''


r = 4
#help(np.safe_eval)
f = lambda x, r=r: -(x-r)*(x**2-2*r*x-2*r**2)
df = lambda x, r=r: -(x**2-2*r*x-2*r**2) - (x-r)*(x*2-2*r)
x = np.linspace(0-r*2, 2*r+r*2, 100)
y = list(map(f,x))
dy = list(map(df,x))

plt.plot(x,y)
plt.plot(x,dy)
plt.show()

for x0 in np.linspace(1, 2*r-1, 19):
    y0 = f(x0)
    dy0 = df(x0)
    assert dy0 > 0
    x1 = x0-y0/dy0
    # in different side
    if not (x1 < r < x0 or x0 < r < x1):
        print('not (x1 < r < x0 or x0 < r < x1): r, x0, x1', r,x0,x1)
    assert (x0-r)*(r-x1) >= 0
    if abs(r-x1) > abs(x0-r):
        print('abs(r-x1) > abs(x0-r): r, x0, x1', r,x0,x)

    









# dir(np)
['ALLOW_THREADS', 'BUFSIZE', 'CLIP', 'ComplexWarning',
'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_DEFAULT2', 'ERR_IGNORE',
'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN',
'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID',
'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity',
'MAXDIMS', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF',
'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE',
'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID',
'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'True_',
'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'WRAP',
'__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__',
'__config__', '__doc__', '__file__', '__git_revision__',
'__initializing__', '__loader__', '__name__', '__package__',
'__path__', '__version__', '_import_tools', '_mat', 'abs', 'absolute',
'absolute_import', 'add', 'add_docstring', 'add_newdoc',
'add_newdoc_ufunc', 'add_newdocs', 'alen', 'all', 'allclose',
'alltrue', 'alterdot', 'amax', 'amin', 'angle', 'any', 'append',
'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh',
'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax',
'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array',
'array2string', 'array_equal', 'array_equiv', 'array_repr',
'array_split', 'array_str', 'asanyarray', 'asarray',
'asarray_chkfinite', 'ascontiguousarray', 'asfarray',
'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d',
'atleast_3d', 'average', 'bartlett', 'base_repr', 'bench',
'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or',
'bitwise_xor', 'blackman', 'bmat', 'bool', 'bool8', 'bool_',
'broadcast', 'broadcast_arrays', 'busday_count', 'busday_offset',
'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_',
'can_cast', 'cast', 'cdouble', 'ceil', 'cfloat', 'char', 'character',
'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat',
'column_stack', 'common_type', 'compare_chararrays', 'compat',
'complex', 'complex128', 'complex64', 'complex_', 'complexfloating',
'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy',
'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh',
'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod',
'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string',
'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate',
'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from',
'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide',
'division', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e',
'ediff1d', 'einsum', 'emath', 'empty', 'empty_like', 'equal',
'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1',
'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft',
'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter',
'flatnonzero', 'flexible', 'fliplr', 'flipud', 'float', 'float16',
'float32', 'float64', 'float_', 'floating', 'floor', 'floor_divide',
'fmax', 'fmin', 'fmod', 'format_parser', 'frexp', 'frombuffer',
'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex',
'fromstring', 'full', 'full_like', 'fv', 'generic', 'genfromtxt',
'get_array_wrap', 'get_include', 'get_numarray_include',
'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj',
'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning',
'histogram', 'histogram2d', 'histogramdd', 'hsplit', 'hstack',
'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp',
'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert',
'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_',
'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp',
'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex',
'iscomplexobj', 'isfinite', 'isfortran', 'isinf', 'isnan', 'isneginf',
'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype',
'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_',
'kaiser', 'kron', 'ldexp', 'left_shift', 'less', 'less_equal',
'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load',
'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp',
'logaddexp2', 'logical_and', 'logical_not', 'logical_or',
'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble',
'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices',
'mat', 'math', 'matrix', 'matrixlib', 'max', 'maximum',
'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap',
'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum',
'mintypecode', 'mirr', 'mod', 'modf', 'msort', 'multiply', 'nan',
'nan_to_num', 'nanargmax', 'nanargmin', 'nanmax', 'nanmean', 'nanmin',
'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate',
'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters',
'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv',
'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid',
'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition',
'percentile', 'pi', 'piecewise', 'pkgload', 'place', 'pmt', 'poly',
'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint',
'polymul', 'polynomial', 'polysub', 'polyval', 'power', 'ppmt',
'print_function', 'prod', 'product', 'promote_types', 'ptp', 'put',
'putmask', 'pv', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate',
'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec',
'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record',
'remainder', 'repeat', 'require', 'reshape', 'resize', 'restoredot',
'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots',
'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save',
'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict',
'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops',
'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d',
'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'short',
'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc',
'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort',
'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square',
'squeeze', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum',
'swapaxes', 'sys', 'take', 'tan', 'tanh', 'tensordot', 'test',
'testing', 'tile', 'timedelta64', 'trace', 'transpose', 'trapz',
'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros',
'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc',
'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc',
'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc',
'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique',
'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort',
'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0',
'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']



