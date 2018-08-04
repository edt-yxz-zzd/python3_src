
'''
0th  424D
2th  file size 4B little-endian
6th  00000000
10th 3E000000 // offset of bits, this file is 62th
//   end: bitmap-file header 
14th 28000000
18th width 4B little-endian
22th height 4B little-endian
26th 0100010000000000
34th 1C000000 // guess data_size 4B little-endian
38th 0000000000000000000000000000000000000000FFFFFF00
62th start of bits
one row 4 byte at least
white is 1
black or none is 0



screen:
left top == 0, 0 -----> x
    |
    |
    V
    y



bmp:
    y
    ^
    |
    |
left bottom == 0, 0 ------> x


mx is list of bytes
mx[i] is one column
mx[i][j] --> i
    |
    |
    V
    j
'''


__all__ = '''
    single_color_bmp_read
    single_color_bmp_write
'''.split()


white = 1
black = 0
none = 0

def hex2bytes(hex_str):
    return bytes.fromhex(hex_str)
    assert len(hex_str)%2 == 0
    u = int(hex_str, base=16)
    return u.to_bytes(len(hex_str)//2, 'big')
magic = '424D'
len_file_size = 4 # +4B file_size 
head1 = '000000003E00000028000000'
len_width = 4 # +4B width
len_height = 4 # +4B height
head2 = '0100010000000000'
len_data_size = 4 # guess? +4B data_size
head3 = '0000000000000000000000000000000000000000FFFFFF00'
magic = hex2bytes(magic)
head1 = hex2bytes(head1)
head2 = hex2bytes(head2)
head3 = hex2bytes(head3)

bits_offset = len_head = 62

loc_magic = 0
loc_file_size = loc_magic + len(magic)
loc_head1 = loc_file_size + len_file_size
loc_width = loc_head1 + len(head1)
loc_height = loc_width + len_width
loc_head2 = loc_height + len_height
loc_data_size = loc_head2 + len(head2)
loc_head3 = loc_data_size + len_data_size

assert len_head == loc_head3 + len(head3)




def little_endian_4B_to_uint32(byte4):
    assert len(byte4) == 4
    return int.from_bytes(byte4, 'little')

def uint32_to_little_endian_4B(u):
    return u.to_bytes(4, 'little')
    assert u >= 0
    bs = bytearray()
    for i in range(4):
        bs.append(u & 0x0FF)
        u >>= 8

    assert u == 0
    return bs


def bin2bytes(bin_str):
    assert len(bin_str)%8 == 0
    u = int(bin_str, base=2)
    return u.to_bytes(len(bin_str)//8, 'big')

def bytes2bin(bs):
    u = int.from_bytes(bs, 'big')
    s = bin(u)[2:]
    s = '0' * (len(bs)*8 - len(s)) + s
    return s
    
    
'mx[width][height]'
def xy2color(mx, x, y):
    return mx[x][y]


def calc_num_row_bits(width):
    return (width+31) & ~(32-1)

def single_color_bmp_write(mx, width, height, xy2color = xy2color):
    bytes_width = uint32_to_little_endian_4B(width)
    bytes_height = uint32_to_little_endian_4B(height)

    ls = []
    n_row_bits = calc_num_row_bits(width)    
    for h in range(height):
        # row = '10100...' + padding'0's
        row = ['1' if xy2color(mx, w, h) else '0' for w in range(width)]
        row.append('0' * (n_row_bits-len(row)))
        row = ''.join(row)
        assert n_row_bits == len(row)

        ls.append(bin2bytes(row))
    ls.reverse()
    bits = b''.join(ls)

    data_size = len(bits)
    assert data_size == n_row_bits//8 * height
    file_size = len_head + data_size
    bytes_data_size = uint32_to_little_endian_4B(data_size)
    bytes_file_size = uint32_to_little_endian_4B(file_size)
    head = b''.join([magic, bytes_file_size, head1,
                     bytes_width, bytes_height, head2,
                     bytes_data_size, head3])
    assert len_head == len(head)

    bmp = head + bits
    assert file_size == len(bmp)
    return bmp

def single_color_bmp_read(bmp):
    assert len(bmp) >= len_head
    head = bmp[:len_head]

    assert head[loc_magic : loc_magic + len(magic)] == magic
    assert head[loc_head1 : loc_head1 + len(head1)] == head1
    assert head[loc_head2 : loc_head2 + len(head2)] == head2
    assert head[loc_head3 : loc_head3 + len(head3)] == head3

    bytes_file_size = head[loc_file_size : loc_file_size + len_file_size]
    bytes_width = head[loc_width : loc_width + len_width]
    bytes_height = head[loc_height : loc_height + len_height]
    bytes_data_size= head[loc_data_size: loc_data_size + len_data_size]

    file_size = little_endian_4B_to_uint32(bytes_file_size)
    width = little_endian_4B_to_uint32(bytes_width)
    height = little_endian_4B_to_uint32(bytes_height)
    data_size = little_endian_4B_to_uint32(bytes_data_size)

    ls = []
    n_row_bits = calc_num_row_bits(width)
    n_row_bytes = n_row_bits >> 3

    assert len(bmp) == len(head) + n_row_bytes * height
    if file_size != len(bmp):
        print('warning: file_size error')
    if data_size != n_row_bytes * height:
        print('warning: data_size error')

    p = bmp[len_head:]
    ls = []
    for i in range(0, len(p), n_row_bytes):
        row_bytes = p[i : i+n_row_bytes]
        row = bytes2bin(row_bytes)
        assert row[width:] == '0' * (len(row) - width)

        row = row[:width]
        row = bytes(0 if c == '0' else 1 for c in row)
        ls.append(row)

    ls.reverse()

    # mx = ls'  transpose
    # since mx is column list and ls is row list
    mx = [bytes(ls[j][i] for j in range(height)) for i in range(width)]
    return mx








output_folder = 'E:/temp_output/'
_mx = [b'\1'*7,]*3
_mx[1] = b'\0'*7
def test_single_color_bmp_write(mx=_mx):
    with open(output_folder+'sc3x7wbw.bmp', 'wb') as fout:
        bmp = single_color_bmp_write(mx, 3, 7)
        fout.write(bmp)
def test_single_color_bmp_read(mx=_mx):
    bmp = single_color_bmp_write(mx, 3, 7)
    mx2 = single_color_bmp_read(bmp)
    if not mx2 == mx:
        print(mx2)
        print(mx)
        
    assert mx2 == mx



if __name__ == '__main__':
    #test_single_color_bmp_write()
    test_single_color_bmp_read()


