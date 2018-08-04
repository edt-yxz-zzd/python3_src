
r'''
[RFC 3533] The Ogg Encapsulation Format Version 0


codec.encode(data) ==>> packets (one logical bitstream)
packet ==>> chunks(ogg_segments) ==>> put into ogg_non_bos_pages
    chunk_sizes(Lacing values) per packet = 0xFF*[0x00-0xFE]
    # NOTE: [0x00] and [0xFF, 0x00]

    Lacing values per page = [0x00-0xFF]+
        # may start with previous packet tail
        # may contain several packets
        # may next with incomplete packet


ogg_file = chained_ogg_file                  # physical bitstream
chained_ogg_file = grouped_ogg_files         # physical bitstream = chained physical bitstreams
grouped_ogg_files = grouped_ogg_files[??]
grouped_ogg_file = bos_pages + non_bos_pages # concurrently multiplexed logical bitstreams
                                             # bos ::= begin of stream
bos_pages = bos_page[num_logical_bitstream]  # without ogg_segments
page = page_header + ogg_segments
    ==>> ogg_file = pages






###############################################################

6. The Ogg page format

   A physical Ogg bitstream consists of a sequence of concatenated
   pages.  Pages are of variable size, usually 4-8 kB, maximum 65307
   bytes.  A page header contains all the information needed to
   demultiplex the logical bitstreams out of the physical bitstream and
   to perform basic error recovery and landmarks for seeking.  Each page
   is a self-contained entity such that the page decode mechanism can
   recognize, verify, and handle single pages at a time without
   requiring the overall bitstream.

   The Ogg page header has the following format:

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1| Byte
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| capture_pattern: Magic number for page start "OggS"           | 0-3
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| version       | header_type   | granule_position              | 4-7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               | 8-11
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               | bitstream_serial_number       | 12-15
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               | page_sequence_number          | 16-19
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               | CRC_checksum                  | 20-23
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               |page_segments  | segment_table | 24-27
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| ...                                                           | 28-
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   The LSb (least significant bit) comes first in the Bytes.  Fields
   with more than one byte length are encoded LSB (least significant
   byte) first.



   The fields in the page header have the following meaning:

   1. capture_pattern: a 4 Byte field that signifies the beginning of a
      page.  It contains the magic numbers:

            0x4f 'O'

            0x67 'g'

            0x67 'g'

            0x53 'S'

      It helps a decoder to find the page boundaries and regain
      synchronisation after parsing a corrupted stream.  Once the
      capture pattern is found, the decoder verifies page sync and
      integrity by computing and comparing the checksum.

   2. stream_structure_version: 1 Byte signifying the version number of
      the Ogg file format used in this stream (this document specifies
      version 0).

   3. header_type_flag: the bits in this 1 Byte field identify the
      specific type of this page.

      *  bit 0x01

         set: page contains data of a packet continued from the previous
            page

         unset: page contains a fresh packet

      *  bit 0x02

         set: this is the first page of a logical bitstream (bos)

         unset: this page is not a first page

      *  bit 0x04

         set: this is the last page of a logical bitstream (eos)

         unset: this page is not a last page

   4. granule_position: an 8 Byte field containing position information.
      For example, for an audio stream, it MAY contain the total number
      of PCM samples encoded after including all frames finished on this
      page.  For a video stream it MAY contain the total number of video
      frames encoded after this page.  This is a hint for the decoder
      and gives it some timing and position information.  Its meaning is
      dependent on the codec for that logical bitstream and specified in
      a specific media mapping.  A special value of -1 (in two's
      complement) indicates that no packets finish on this page.

   5. bitstream_serial_number: a 4 Byte field containing the unique
      serial number by which the logical bitstream is identified.

   6. page_sequence_number: a 4 Byte field containing the sequence
      number of the page so the decoder can identify page loss.  This
      sequence number is increasing on each logical bitstream
      separately.

   7. CRC_checksum: a 4 Byte field containing a 32 bit CRC checksum of
      the page (including header with zero CRC field and page content).
      The generator polynomial is 0x04c11db7.

   8. number_page_segments: 1 Byte giving the number of segment entries
      encoded in the segment table.

   9. segment_table: number_page_segments Bytes containing the lacing
      values of all segments in this page.  Each Byte contains one
      lacing value.

   The total header size in bytes is given by:
   header_size = number_page_segments + 27 [Byte]

   The total page size in Bytes is given by:
   page_size = header_size + sum(lacing_values: 1..number_page_segments)
   [Byte]




'''


r'''
Numerical_Recipes(3rd_2007).pdf
22.4 Cyclic Redundancy and Other Checksums
'''


__all__ = '''
    OggPage
    
    ogg_file2iter_pages
    read_one_grouped_ogg
    iter_grouped_ogg_infos_from_path
    read_grouped_ogg_infos_from_path
    iter_split_segment_table
    pages_of_logic_bitstream2iter_packets
'''.split()


import os.path, zlib
from sand import CheckError, CheckTypeError, CheckValueError, DecodeUtils_32le
from sand.small.check_utils import *
from sand.big.CRC import CRC_Info, reverse_uint, find_CRC_argss, \
     reverse_bitorder_per_byte, ogg_CRC32, ogg_crc32


    
def int2byte(i):
    return bytes([i])
def uint32_to_4bytesle(u):
    return u.to_bytes(4, 'little')




class OggPage:
    CRC_size = 4
    CRC_generator_polynomial = 0x04c11db7
    CRC_generator = CRC_generator_polynomial | (1<< (CRC_size*8))

    def crc32(self, data, crc=None):
        return ogg_crc32(data, crc)
    def is_begin_of_packet(self):
        return not (self.header_type_flag & 0x01)
    is_bop = is_begin_of_packet
    def is_end_of_packet(self):
        return self.segment_table[-1] < 0xFF
    is_eop = is_end_of_packet
    def is_start_of_logic_bitstream(self):
        return bool(self.header_type_flag & 0x02)
    is_bos = is_start_of_logic_bitstream
    def is_last_of_logic_bitstream(self):
        return bool(self.header_type_flag & 0x04)
    is_eos = is_last_of_logic_bitstream

    def verify(self, verify_CRC=True):
        check_type_value(self.capture_pattern, b'OggS',
                         "capture_pattern", "b'OggS'")
        check_type_value(self.stream_structure_version, 0,
                         'stream_structure_version', '0')
        check_type(self.header_type_flag, int, 'header_type_flag')
        if not self.header_type_flag < 0x08:
            raise ValueError('not header_type_flag < 0x08')
        check_type(self.granule_position, bytes, 'granule_position')
        if not len(self.granule_position) == 8:
            raise ValueError('not len(granule_position) == 8')


        check_uint32(self.bitstream_serial_number, 'bitstream_serial_number')
        check_uint32(self.page_sequence_number, 'page_sequence_number')
        check_uint32(self.CRC_checksum, 'CRC_checksum')

        
        check_type(self.number_page_segments, int, 'number_page_segments')
        check_type(self.segment_table, bytes, 'segment_table')
        check_type(self.payload, bytes, 'payload')
        if not self.number_page_segments > 0: # at least [0]
            raise ValueError('not number_page_segments > 0')
        check_value(self.number_page_segments, len(self.segment_table),
                         'number_page_segments != len(segment_table)')
        # error:
        # xxxxx assert b'\xFF'*(number_page_segments-1) == segment_table[:-1]
        # xxxxx assert segment_table[-1] < 0xFF
        check_value(len(self.payload), sum(self.segment_table),
                    'len(payload) != sum(segment_table)')

        if verify_CRC:
            page = self.make_page(0)
            # NOT: crc = zlib.crc32(page) & 0xffffffff
            # since zlib :: byte_MSB_first == False

            # calced_crc = ogg_CRC32.bytes2crc(page)
            calced_crc = ogg_crc32(page)
            check_value(self.CRC_checksum, calced_crc,
                        'CRC_checksum != calced_crc')
            




    def make_page(self, CRC_checksum=None):
        header = self.make_header(CRC_checksum)
        page = header + self.payload
        return page
    def make_header(self, CRC_checksum=None):
        if CRC_checksum is None:
            CRC_checksum = self.CRC_checksum
        check_uint32(CRC_checksum, 'CRC_checksum')
        
        ls = [self.capture_pattern,
              int2byte(self.stream_structure_version),
              int2byte(self.header_type_flag),
              self.granule_position,
              uint32_to_4bytesle(self.bitstream_serial_number),
              uint32_to_4bytesle(self.page_sequence_number),
              uint32_to_4bytesle(CRC_checksum), # not self.CRC_checksum
              int2byte(self.number_page_segments),
              self.segment_table,
              ]
        return b''.join(ls)
              
              
    
    def __init__(self,
                 capture_pattern,
                 stream_structure_version,
                 header_type_flag,
                 granule_position,
                 bitstream_serial_number,
                 page_sequence_number,
                 CRC_checksum,
                 number_page_segments,
                 segment_table,
                 payload,
                 *, verify_CRC=True):

##        print(segment_table,
##              number_page_segments,
##              len(segment_table))
        
        (self.capture_pattern,
             self.stream_structure_version,
             self.header_type_flag,
             self.granule_position,
             self.bitstream_serial_number,
             self.page_sequence_number,
             self.CRC_checksum,
             self.number_page_segments,
             self.segment_table,
             self.payload) = (
                             capture_pattern,
                             stream_structure_version,
                             header_type_flag,
                             granule_position,
                             bitstream_serial_number,
                             page_sequence_number,
                             CRC_checksum,
                             number_page_segments,
                             segment_table,
                             payload)

        self.verify(verify_CRC=verify_CRC)
##        if 1 or not (b'\xFF'*(number_page_segments-1) == segment_table[:-1]
##                and segment_table[-1] < 0xFF):
##            print(self)
##            print('is_bop', self.is_bop())
##            print('is_bos', self.is_bos())
##            print('is_eos', self.is_eos())
            
    @classmethod
    def from_file(cls, file, verify_CRC=True):
        begin = file.tell()
        
        du = DecodeUtils_32le(file)
        capture_pattern = b'OggS'
        du.check_bytes(capture_pattern)
        stream_structure_version, header_type_flag = du.read_bytes(2)
        granule_position = du.read_bytes(8)
        bitstream_serial_number = du.read_uint()
        page_sequence_number = du.read_uint()
        CRC_checksum = du.read_uint()
        number_page_segments, = du.read_bytes(1)
        segment_table = du.read_bytes(number_page_segments)
        payload_size = sum(segment_table)
        payload = du.read_bytes(payload_size)
        
        end = file.tell()
        this = cls  (
                         capture_pattern,
                         stream_structure_version,
                         header_type_flag,
                         granule_position,
                         bitstream_serial_number,
                         page_sequence_number,
                         CRC_checksum,
                         number_page_segments,
                         segment_table,
                         payload,
                         verify_CRC = verify_CRC)
        file.seek(begin)
        page = du.read_bytes(end-begin)
        assert this.make_page() == page
        return this

    def get_args(self):
        return (self.capture_pattern,
             self.stream_structure_version,
             self.header_type_flag,
             self.granule_position,
             self.bitstream_serial_number,
             self.page_sequence_number,
             self.CRC_checksum,
             self.number_page_segments,
             self.segment_table,
             self.payload)
    def __str__(self):
        s = '{}{}'.format(type(self).__name__, self.get_args()[:-1])
        s = s[:-1] + ', ...)'
        return s
    def __repr__(self):
        return '<' + str(self) + '>'
    
            

def ogg_file2iter_pages(file, end, verify_CRC=True):
    f = OggPage.from_file
    while file.tell() < end:
        yield f(file, verify_CRC)

    if not file.tell() == end:
        if file.tell() > end:
            raise FormatError('file.tell() > end')
        raise logic-error



def read_one_grouped_ogg(file, file_size, verify_CRC=True):
    'return bitstream_serial_number2pages, (begin, end), (bos_pages, non_bos_pages)'
    begin = file.tell()
    it = ogg_file2iter_pages(file, file_size, verify_CRC)

    bos_pages = []
    non_bos_pages = []
    num_eos_pages = 0
    for page in it:
        if page.is_eos():
            num_eos_pages += 1

        #####
        if page.is_bos():
            bos_pages.append(page)
        else:
            non_bos_pages.append(page)
            break

    num_logic_bitstreams = len(bos_pages)
    while num_eos_pages < num_logic_bitstreams:
        page = next(it)
        if page.is_bos():
            raise FormatError('bos in middle of non_bos_pages')

        ####
        if page.is_eos():
            num_eos_pages += 1
        non_bos_pages.append(page)

    end = file.tell()



        
    ################
    bitstream_serial_number2pages = {
        bos.bitstream_serial_number:[bos] for bos in bos_pages}
    if len(bitstream_serial_number2pages) < num_logic_bitstreams:
        raise FormatError('bitstream_serial_numbers are duplicated')

    for page in non_bos_pages:
        bitstream_serial_number2pages[page.bitstream_serial_number].append(page)

    for pages in bitstream_serial_number2pages.values():
        page_sequence_numbers = [page.page_sequence_number for page in pages]
        if not page_sequence_numbers == list(range(len(pages))):
            raise FormatError('page_sequence_numbers != [0..len(pages)]')

    if not all(pages[-1].is_eos()
               for pages in bitstream_serial_number2pages.values()):
        raise FormatError('not all(logic_bitstream_pages[-1].is_eos())')

    if not all(page.is_bop() == (pages[i-1].segment_table[-1] < 0xFF)
               for pages in bitstream_serial_number2pages.values()
               for i, page in enumerate(pages)):
        raise FormatError('not all(page.is_bop() == (prev_page.segment_table[-1] < 0xFF))')
    return bitstream_serial_number2pages, (begin, end), (bos_pages, non_bos_pages)




def iter_grouped_ogg_infos_from_path(path, verify_CRC=True):
    with open(path, 'rb') as fin:
        size = os.path.getsize(path)
        #group_infos = []
        while fin.tell() < size:
            yield read_one_grouped_ogg(fin, size, verify_CRC)
        assert fin.tell() == size


def read_grouped_ogg_infos_from_path(path, verify_CRC=True):
    return list(iter_grouped_ogg_infos_from_path(path, verify_CRC))


def iter_split_segment_table(segment_table):
    begin = 0
    for i, u8 in enumerate(segment_table):
        if u8 < 0xFF:
            end = i+1
            yield segment_table[begin:end]
            begin = end
    if begin != len(segment_table):
        yield segment_table[begin:]




def pages_of_logic_bitstream2iter_packets(pages):
    assert pages
    
    incomplete_packet = b''
    for page in pages:
        assert bool(incomplete_packet) == (not page.is_bop())
        payload = page.payload
        it = iter_split_segment_table(page.segment_table)
        last_idx = i = None
        begin = 0
        for i, chunk_sizes in enumerate(it):
            assert chunk_sizes
            size = sum(chunk_sizes)
            end = begin + size
            packet = payload[begin:end]
            begin = end
            
            if incomplete_packet:
                assert i == 0
                assert not page.is_bop()
                packet = incomplete_packet + packet
                incomplete_packet = b''

            ############
            if chunk_sizes[-1] != 0xFF:
                yield packet
            else:
                if not end == len(payload):
                    print(end, len(payload))
                    print(i, chunk_sizes)
                    print(page.segment_table)
                assert end == len(payload)
                assert size
                assert last_idx is None
                last_idx = i
                incomplete_packet = packet

                    
        assert last_idx is None or last_idx == i
        assert i is not None

    
    assert not incomplete_packet
    assert page.is_eos()

                
                

def _find_out_ogg_CRC32_args(fname):        
    for grouped_ogg_info in iter_grouped_ogg_infos_from_path(fname, verify_CRC=True):
        bitstream_serial_number2pages, (begin, end), (bos_pages, non_bos_pages) = grouped_ogg_info
        pages = bos_pages + non_bos_pages
        
        ### to find out CRC args ### byte_MSB_first=True !!!
        data_crc_pairs = ((page.make_page(0), page.CRC_checksum) for page in pages)
        argss = find_CRC_argss(
            generater=OggPage.CRC_generator,
            byte_MSB_first=True, # not False, !!!!!!!!!!!
            data_crc_pairs=data_crc_pairs,
            verify=True)
        if not argss:
            raise fail
        for args in argss:
            info = CRC_Info(*args)
            print(info)
            assert info == CRC_Info(0x104c11db7, 32, 0x0, 0x0, True, True)
        del pages, data_crc_pairs
            

def t():
    from pprint import pprint
    for fname in [r'C:\Users\Administrator\Desktop\天上人间.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v11.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v12.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v13.ogg',
                  #r'E:\multimedia\audio\music\bgm\赤印_BGM\v14.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v19.ogg',
                  #r'E:\multimedia\audio\music\bgm\赤印_BGM\s06.ogg',
                  #r'E:\multimedia\audio\music\bgm\赤印_BGM\s07.ogg',
                  ]:
        print('----------------------------------------')
        print(fname)
        infos = read_grouped_ogg_infos_from_path(fname, verify_CRC=True)
        #pprint(infos)
        for ID2pages, *_ in infos:
            for pages in ID2pages.values():
                bos = pages[0]
                print(bos)
                print(pages[1])
                #print(bos.payload)
                for i, packet in enumerate(pages_of_logic_bitstream2iter_packets(pages)):
                    if i == 2:
                        break
                    #print(packet)
                    
        print()
        #break


if __name__ == "__main__":
    t()
    _find_out_ogg_CRC32_args(r'C:\Users\Administrator\Desktop\天上人间.ogg')
        










