
'''
numpy ops:
    # image_PIL -> array
        greys = numpy.asarray(image_PIL.convert('L'))

    # array -> matrix
    # mx.reshape(num_rows, num_columns)
        greys = greys.reshape(image_PIL.height, image_PIL.width)

    # change matrix.dtype
        matrix.astype(numpy.uint8)
        matrix.astype(numpy.int_)
        matrix.astype(int)
        matrix.floor(matrix)

    # matrix -> image_PIL
        PIL.Image.fromarray(matrix.astype(numpy.uint8))

del sys.modules['binary_matrix2mountain_height']
import binary_matrix2mountain_height as B
from binary_matrix2mountain_height import *


del sys.modules['_try__binary_matrix2mount_height']
import _try__binary_matrix2mount_height as B
from _try__binary_matrix2mount_height import *
'''

def reshape(array, *, num_rows, num_columns, container=None):
    if len(array) != num_rows*num_columns: raise ValueError
    if num_rows <= 0: raise ValueError
    if num_columns <= 0: raise ValueError
    it = (array[i:i+num_columns] for i in range(0, len(array), num_columns))
    if container is None:
        return list(it)
    else:
        return container(map(container, it))

def adjust_show(matrix):
    matrix = matrix - matrix.min()
    M = matrix.max()
    if M:
        #bug: matrix *= (0xFF / M)
        #fine: matrix = matrix * (0xFF / M)
        matrix = matrix * (0xFF / M)
        matrix = numpy.floor(matrix)
    #PIL.Image.fromarray(matrix.astype(int)).show()
    #PIL.Image.fromarray(numpy.uint8(matrix)).show()
    PIL.Image.fromarray(matrix.astype(numpy.uint8)).show()
def cut_at_level(binary_level):
    I = (greys < binary_level)*0xFF
    PIL.Image.fromarray(I.astype(numpy.uint8)).show()

def reload():
    del sys.modules['_try__binary_matrix2mount_height']
    import _try__binary_matrix2mount_height as B
    return B

import sys
from . import binary_matrix2mountain_height as B2M
from . import erase_low_mountains_of_mountain_height_matrix as ERL
import PIL.Image
import numpy
#import statistics # mean

print(sys.argv)
_this_py, binary_level, min_height = sys.argv
binary_level = int(binary_level)
min_height = int(min_height)

image_path = r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\internet\webpage\captcha_images\6.jpg'
image_path = r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\internet\webpage\captcha_images\0_67uguw.jpg'
image_PIL = PIL.Image.open(image_path)
#image_PIL.show()


#greys = list(image_PIL.convert('L').transpose().getdata())
greys = numpy.asarray(image_PIL.convert('L'))
greys = greys.reshape(image_PIL.height, image_PIL.width)
#greys.mean()
#mean = statistics.mean(greys)


print(f'binary_level = {binary_level}')
print(f'greys.mean() == {greys.mean()}')
I = input_binary_matrix = greys < binary_level # greys.mean()
O = output_uint_matrix = numpy.zeros(greys.shape, dtype=numpy.uint8)
R, C = greys.shape
B2M.binary_matrix2mountain_height(input_binary_matrix=I, output_uint_matrix=O, num_rows=R, num_columns=C, case=4)

print(O)
adjust_show(O)

IO = numpy.copy(O)
ERL.erase_low_mountains_of_mountain_height_matrix(inout_matrix=IO, num_rows=R, num_columns=C, case=4, min_height=min_height)
print(IO)
adjust_show(IO)


