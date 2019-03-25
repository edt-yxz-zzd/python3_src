
'''
numpy.ndarray
    image
        color_image
            RGB
            RGBA
        grey_image
            binary_image


usage:
    > py to_binary_image.py -T 0 1 0 -G -F -i 6.jpg
'''


__all__ = '''
    the_numpy_dtype_bool
    is_numpy_ndarray
    is_image
    is_color_image
    is_grey_image
    is_binary_image

    ndarray2grey_image
    grey_image2binary_image

    binary_image2text_grey_image
    grey_image2iter_rows
    grey_image2iter_byte_rows
    grey_image2iter_text_rows

    '''.split()
    #main

import numpy # bool_

the_numpy_dtype_bool = numpy.dtype('bool')

def is_numpy_ndarray(obj):
    'ndim may not be 1'
    return isinstance(obj, numpy.ndarray)
def is_image(obj):
    'grey_image | color_image RGB | color_image RGBA'
    return (is_numpy_ndarray(obj)
        and (obj.ndim == 2
            or (obj.ndim == 3 and obj.shape[-1] in (3,4))
            )
        )
def is_color_image(obj):
    'color_image RGB | color_image RGBA'
    return is_numpy_ndarray(obj) and obj.ndim == 3 and obj.shape[-1] in (3,4)
def is_grey_image(obj):
    return is_numpy_ndarray(obj) and obj.ndim == 2
def is_binary_image(obj):
    'binary_image == bitmap'
    return is_grey_image(obj) and obj.dtype is the_numpy_dtype_bool

def ndarray2grey_image(ndarray, height, width):
    assert isinstance(ndarray, numpy.ndarray)
    assert ndarray.size == height*width
    shape = height, width
    grey_image = ndarray.reshape(shape)
    return grey_image

def grey_image2binary_image(grey_image, threshold, *, negative=False):
    if negative:
        binary_image = grey_image < threshold
    else:
        binary_image = grey_image >= threshold
    return binary_image






def binary_image2text_grey_image(binary_image):
    grey_image = binary_image.astype('uint8')
    grey_image += 0x30 # (0,1) -> '01'
    text_grey_image = grey_image
    return text_grey_image
def grey_image2iter_rows(grey_image):
    height, width = grey_image.shape
    for i in range(height):
        yield grey_image[i]
def grey_image2iter_byte_rows(grey_image):
    for row in grey_image2iter_rows(grey_image):
        yield row.tobytes()
def grey_image2iter_text_rows(grey_image):
    for row in grey_image2iter_rows(grey_image):
        yield row.tostring()






def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    #import skimage.io as image_io
    import imageio as image_io
    read_image = image_io.imread
    del image_io

    parser = argparse.ArgumentParser(
        description='convert grey_image to binary_image'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str
                        , required=True
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-F', '--flip', action='store_true'
                        , default = False
                        , help='flip final binary_image')
    parser.add_argument('-G', '--as_grey', action='store_true'
                        , default = False
                        , help='convert color_image to grey_image first')
    parser.add_argument('-T', '--threshold_coeff', type=float
                        , required=True
                        , nargs = 3
                        , help='threshold_coeff A B C; threshold = A*min+B*mean+C+max')
    '''
    parser.add_argument('-out_txt', '--output_as_text', action='store_true'
                        , default = False
                        , help='output binary_image as text')
    '''

    args = parser.parse_args(args)
    encoding = None
    omode = 'wb' if args.force else 'xb'

    ifname = args.input
    image = read_image(ifname, as_gray=args.as_grey)
    if not is_grey_image(image): raise Exception('not grey_image')
    grey_image = image

    A,B,C = args.threshold_coeff
    threshold = A*grey_image.min() + B*grey_image.mean() + C*grey_image.max()
    binary_image = grey_image2binary_image(grey_image, threshold, negative=args.flip)
    text_grey_image = binary_image2text_grey_image(binary_image)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        for byte_row in grey_image2iter_byte_rows(text_grey_image):
            fout.write(byte_row)
            fout.write(b'\n')

'''
if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())
'''


if __name__ == "__main__":
    main()



