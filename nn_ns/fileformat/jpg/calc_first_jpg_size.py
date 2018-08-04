
'''
see also:
    nn_ns.bin.concat_files
    nn_ns.app.concat_files
    nn_ns.bin.truncate_and_move_to
    nn_ns.fileformat.zip.move_last_zip_to

    nn_ns.fileformat.zip.get_last_zip_begin
    nn_ns.fileformat.jpg.calc_first_jpg_size
'''

__all__ = '''
    calc_first_jpg_size
    '''.split()

# Pillow
from PIL import Image
from PIL import ImageFile
from nn_ns.filedir.get_file_size import get_file_size



def calc_may_first_jpg_size(fname):
    # -> (raise IOError) | UInt
    with open(fname, 'rb') as fin:
        bs = fin.read()
    i = binary_search_min_prefix_that_is_image(bs)
    return i
def binary_search_min_prefix_that_is_image(bs):
    # find the min length
    begin = 0
    end = len(bs)
    while end - begin >= 2:
        middle = (end+begin)//2
        assert begin < middle < end
        if is_image(bs, middle):
            end = middle
        else:
            begin = middle

    for i in range(begin, end):
        if is_image(bs, i):
            return i
    else:
        if is_image(bs, end):
            return end

    raise IOError
    return None

def is_image(bs, length):
    bs = bs[:length]
    p = ImageFile.Parser()
    p.feed(bs)
    try:
        im = p.close()
    except IOError:
        return False
    return True









if False:
    import os.path
    folder = r'E:\temp_output\concat files'
    a_jpg = folder + r'\a.jpg'
    a_zip = folder + r'\a.zip'
    jpg_zip = folder + r'\jpg+zip.jpg - stable.zip'




    def try_pillow():
        with Image.open(a_jpg) as im:
            print('\n'.join(dir(im)))
            help(im.load)
            help(im.load_end)

    def try__max_end():
        # fail:
        #   max_end == file_size

        from nn_ns.io.UserBufferedIOBase__get_max_end_of_read_write import \
            UserBufferedIOBase__get_max_end_of_read_write
        with open(jpg_zip, 'rb') as fin:
            fin = UserBufferedIOBase__get_max_end_of_read_write(fin)
            with Image.open(fin) as im:
                print(fin.tell())
            print(fin.max_end)

        with open(jpg_zip, 'rb') as fin:
            fin = UserBufferedIOBase__get_max_end_of_read_write(fin)
            with Image.open(fin) as im:
                bs = im.tobytes()
                print(fin.tell())
            print(fin.max_end)
            fin.max_end == get_file_size(jpg_zip)


    def try_binary_search():
        from io import BytesIO
        i = calc_first_jpg_size(jpg_zip)
        print(i)

    try_binary_search()


