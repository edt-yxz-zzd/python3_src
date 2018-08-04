
'''
see also:
    nn_ns.bin.concat_files
    nn_ns.app.concat_files
    nn_ns.bin.truncate_and_move_to
    nn_ns.fileformat.zip.move_last_zip_to

    nn_ns.fileformat.zip.get_last_zip_begin
    nn_ns.fileformat.jpg.calc_first_jpg_size


####################
zip
    unknown bytes
    file entity space
        # not file entity array
        # contains some deleted holes
    central directory
    end of central directory record



WTF??????!!!!
    signature: 0x06054b50 in file is b'\x50\x4b\x05\x06'
    and it is not in end of file!!!
    do I have to search it??


  comment from zipfile.py of python stdlib:
    # Either this is not a ZIP file, or it is a ZIP file with an archive
    # comment.  Search the end of the file for the "end of central directory"
    # record signature. The comment is the last item in the ZIP file and may be
    # up to 64K long.  It is assumed that the "end of central directory" magic
    # number does not appear in the comment.



Central directory file header
    Offset  Bytes   Description
    20      4       Compressed size
End of central directory record (EOCD)
    Offset  Bytes   Description
    0       4       End of central directory signature = 0x06054b50
                    0x06_05_4b_50
    16      4       Offset of start of central directory, relative to start of archive




sz = int.from_bytes(bs, 'little')
'''



__all__ = '''
    get_last_zip_begin

    get_last_zip_size
    '''.split()

import zipfile
from zipfile import _EndRecData, _ECD_OFFSET
    #, _ECD_SIZE, _ECD_COMMENT, _ECD_LOCATION
from nn_ns.filedir.get_file_size import get_file_size


def read_uint_LE(fin, sz):
    bs = fin.read(sz)
    return int.from_bytes(bs, 'little')

def get_last_zip_size(fname):
    file_size = get_file_size(fname)
    last_zip_begin = get_last_zip_begin(fname)
    last_zip_size = file_size - last_zip_begin
    return last_zip_size

def get_last_zip_begin(fname):
    with zipfile.ZipFile(fname) as zfin:
        central_directory_begin = zfin.start_dir

        last_zip_first_file_entity_begin = min(
            (info.header_offset for info in zfin.infolist()), default=None)
        # NOTE:
        #   * when infolist is empty
        #   * when there are some deleted file entry in front of last zip file

    with open(fname, 'rb') as fin:
        endrec = _EndRecData(fin)
            # [b'PK\x05\x06', 0, 0, 2, 2, 183, 32592, 0, b'', 65296]
        offset_cd = endrec[_ECD_OFFSET]         # offset of central directory

        # offset_cd is the old central_directory_begin
        # central_directory_begin is new, i.e. prefix_size + offset_cd
        concat_prefix_file_size = central_directory_begin - offset_cd

    if last_zip_first_file_entity_begin is not None:
        assert concat_prefix_file_size <= last_zip_first_file_entity_begin
    last_zip_begin = concat_prefix_file_size
    return last_zip_begin





