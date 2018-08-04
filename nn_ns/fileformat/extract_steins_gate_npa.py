import struct
import io
import os
import re



def xor_cipher(key, message):
    # version 2: use int for bitwise operator
    if 0 == len(message): return b''
    assert len(key) > 0
    keys = key * (len(message) // len(key) + 1)
    keys = keys[:len(message)]
    ikey = int.from_bytes(keys, 'little')
    imsg = int.from_bytes(message, 'little')
    iret = ikey ^ imsg
    return iret.to_bytes(len(message), 'little')

'''
def xor_cipher(buffer, key, message): 
    # version 1
    n = len(key)
    assert n > 0
    j = 0
    for i in range(len(message)):
        buffer.append(message[i]^key[j])
        j += 1
        if j == n: j = 0

    return buffer
'''

xor_key_of_steins_gate = b'\xBD\xAA\xBC\xB4\xAB\xB6\xBC\xB4'
encoding_of_steins_gate = 'shift_jis'

uint32_fmt = struct.Struct('<L')
len_of_toc_fmt = uint32_fmt
num_of_entries_fmt = uint32_fmt
len_of_string_fmt = uint32_fmt
entry_fmt = struct.Struct('<3L')

def unpack_from_file(fmt, file):
    return fmt.unpack(file.read(fmt.size))

def get_string(file, encoding):
    len_of_string, = unpack_from_file(len_of_string_fmt, file)
    fmt = struct.Struct(str(len_of_string) + 's')
    return unpack_from_file(fmt, file)[0].decode(encoding)


def open_steinsgate_npa_file(file_name):
    file_size = os.path.getsize(file_name)
    subfiles = {}
    with open(file_name, 'rb') as npa_file:
        len_of_toc, = unpack_from_file(len_of_toc_fmt, npa_file)
        table_of_contents = npa_file.read(len_of_toc)
        buffer = xor_cipher(xor_key_of_steins_gate, table_of_contents)
        with io.BytesIO(buffer) as table_of_contents:
            num_of_entries, = unpack_from_file(num_of_entries_fmt, table_of_contents)
            for i in range(num_of_entries):
                subfile_name = get_string(table_of_contents, encoding_of_steins_gate)
                assert subfile_name not in subfiles
                info = {}
                info['size'], info['offset'], info['unknown'] = unpack_from_file(entry_fmt, table_of_contents)
                assert info['unknown'] == 0 # it seems correct!
                subfiles[subfile_name] = info

    total_size = 0
    for info in subfiles.values():
        total_size += info['size']

    total_size += len_of_toc + len_of_toc_fmt.size
    assert total_size == file_size
    return subfiles




                
def extract_steinsgate_npa_file(to_path, file_name, subfiles):
    with open(file_name, 'rb') as npa_file:
        for subfile_name, info in subfiles.items():
            path = os.path.join(to_path, subfile_name)
            npa_file.seek(info['offset'])
            subfile = npa_file.read(info['size'])
            buffer = xor_cipher(xor_key_of_steins_gate, subfile)
            where = os.path.dirname(os.path.abspath(path))
            os.makedirs(where,exist_ok=True)
            # what if 'path' be removed here? f*ck!
            try:
                with open(path, 'xb') as subfile:
                    subfile.write(buffer)
            except FileExistsError as fee:
                subfile_size = os.path.getsize(path)
                if subfile_size != len(buffer): raise
                with open(path, 'rb') as subfile:
                    if subfile.read(subfile_size) != buffer: raise


                
            
steins_gate_home = r'C:\game\命运石之门STEINSGATE（汉化硬盘）\STEINSGATE/'


def ex_sound():
    sg_sound_npa = steins_gate_home + r'sound.npa'
    sg_sound_npa_filter = re.compile(r'sound/bgm/.*\.ogg')
    sg_sound = steins_gate_home + r'ex_sound/'
    extract_steinsgate_npa_file(\
        sg_sound, sg_sound_npa, \
        {name:info for name, info in open_steinsgate_npa_file(sg_sound_npa).items() \
         if sg_sound_npa_filter.match(name)})


def ex_nss():
    sg_nss_npa = steins_gate_home + r'nss.npa'
    return open_steinsgate_npa_file(sg_nss_npa)




