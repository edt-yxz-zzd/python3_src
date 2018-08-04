
import struct
import io
import os
import re
import zlib
import codecs


char_bit = 8
encoding_of_Crimson_Imprint = 'utf_16_le'
uint64_fmt = struct.Struct('<Q')
uint32_fmt = struct.Struct('<L')
magic_number_of_xp3 = b'XP3\x0D\x0A\x20\x0A\x1A\x8B\x67' # '\x01'
xp3_header_fmt = struct.Struct('<' + str(len(magic_number_of_xp3)) + 'sc')
xp3_encoding = {'1': 'utf_16_le'}
xp3_version_this_module_impl = 0
offset_fmt = uint64_fmt
ptr_fmt = uint64_fmt
size_fmt = uint64_fmt
xp3_version0_compressed_method = {-1: ('unknown', None), 0: ('raw', lambda x:x), 1: ('zlib', zlib.decompress)}
toc_flag_fmt = struct.Struct('<B')
toc_not_end_mask = 0x08
toc_compressed_method_mask = 0x07
toc_compressed_method = xp3_version0_compressed_method

subfile_entry_protected_mask = 1 << 31
segment_compressed_method_mask = 0x07
segment_compressed_method = xp3_version0_compressed_method

hat_fmt = struct.Struct('<4sQ')
entry_hat_fmt = hat_fmt
info_hat_fmt = hat_fmt                      # 12
info_header_fmt = struct.Struct('<LQQH')    # 22
segment_array_hat_fmt = hat_fmt             # 12
segment_fmt = struct.Struct('<L3Q')         # 28
adler_hat_fmt = hat_fmt                     # 12
ucs_2_fmt = struct.Struct('2s')
hat_tag = {'entry': b'File', 'info': b'info', 'segment_array': b'segm', 'adler': b'adlr'}


class subbytes:
    def __init__(self, bytes_data, bytes_offset, range_begin, range_end):
        self.data = bytes_data
        self.offset = bytes_offset
        self.begin = range_begin
        self.end = range_end
        assert self.is_valid()

    def range_size(self):
        return self.end - self.begin

    def remain_size(self):
        return self.end - self.offset
    
    def copy(self):
        return subbytes(self.data, self.offset, self.begin, self.end)

    def subrange(self, size):
        assert self.offset + size <= self.end
        return subbytes(self.data, self.offset, self.offset, self.offset+size)
    
    def skip(self, step_length):
        self.offset += step_length
        assert self.is_valid()
        
    def is_valid(self):
        return 0 <= self.begin <= self.offset <= self.end <= len(self.data)

    def read(self, size):
        assert self.offset + size <= self.end
        ret = self.data[self.offset : self.offset + size]
        self.skip(size)
        return ret
        
    def unpack(self, fmt):
        assert self.offset + fmt.size <= self.end
        ret = fmt.unpack_from(self.data, self.offset)
        self.skip(fmt.size)
        return ret

def eof(subbytes_data):
    return subbytes_data.offset == subbytes_data.end

def unpack_from_file(fmt, file):
    return fmt.unpack(file.read(fmt.size))



def get_text(subbytes_data, len_of_text, len_of_bytes, encoding):
    data = subbytes_data.read(len_of_bytes)
    text = codecs.decode(data, encoding)
    assert len_of_text == len(text)
    return text
        
def get_adler(subbytes_data, len_of_adler):
    adler = subbytes_data.read(len_of_adler)
    return int.from_bytes(adler, 'little')



'''
entry_hat
entry
{
    info_hat
    info
    {
        info_header
        ucs2[] subfile_name
    }
    segment_array_hat
    segment[] segment_array
    adler_hat
    adler # should be adler32
}
'''

def find_hats(toc_data, hat_tag, limit = 0):
    where = []
    while not eof(toc_data):
        tag, size = toc_data.unpack(entry_hat_fmt)
        if tag == hat_tag:
            where.append(toc_data.subrange(size))
            if len(where) == limit: break
        toc_data.skip(size)
    return where
        
        
def get_entry(entry_data, encoding):
    ############################################
    ##################info######################
    ############################################
    info = find_hats(entry_data, hat_tag['info'], 1)
    assert len(info) == 1
    info = info[0]
    info_size = info.range_size()
    
    entry = {}
    entry_flag_in_file, entry['original_size'], entry['compressed_size'], \
            len_of_subfile_name_in_text_form \
            = entry_data.unpack(info_header_fmt)
    entry['file_protected'] = entry_flag_in_file & subfile_entry_protected_mask
    # len_of_subfile_name *= ucs_2_fmt.size  # because only 'utf_16_le' used
    len_of_subfile_name_in_byte_form = info_size - info_header_fmt.size
    entry['file_name'] = get_text(entry_data, len_of_subfile_name_in_text_form, \
                                  len_of_subfile_name_in_byte_form, encoding)

    ############################################
    ##################segm######################
    ############################################
    segment_array = find_hats(entry_data, hat_tag['segment_array'], 1)
    assert len(segment_array) == 1
    segment_array = segment_array[0]
    segment_array_size = segment_array.range_size()
    num_of_segments = segment_array_size // segment_fmt.size
    assert segment_array_size % segment_fmt.size == 0
    
    segment_array = []
    for i in range(num_of_segments):
        segment = {}
        segment_flag_in_file, segment['offset'], \
                               segment['original_size'], segment['compressed_size'] \
                               = entry_data.unpack(segment_fmt)
        segment_compressed_method_in_file = segment_compressed_method_mask & segment_flag_in_file
        if segment_compressed_method_in_file not in segment_compressed_method:
            segment_compressed_method_in_file = -1
        segment_compressed_method_in_file = segment_compressed_method[segment_compressed_method_in_file]
        if segment_compressed_method_in_file[0] == 'raw':
            assert segment['original_size'] == segment['compressed_size']
        segment['compressed_method'] = segment_compressed_method_in_file
        segment_array.append(segment)

    total_compressed_size = 0
    total_original_size = 0
    for sgm in segment_array:
        total_compressed_size += sgm['compressed_size']
        total_original_size += sgm['original_size']
    assert total_compressed_size == entry['compressed_size']
    assert total_original_size == entry['original_size']
    entry['segment_array'] = segment_array

    ############################################
    ##################adlr######################
    ############################################
    adler = find_hats(entry_data, hat_tag['adler'], 1)
    assert len(adler) == 1
    adler = adler[0]
    adler_size = adler.range_size()
    # assert adler_size == 4
    '''# there may be other chunks...
    assert entry_size == info_hat_fmt.size + info_header_fmt.size + \
           len_of_subfile_name + \
           segment_array_hat_fmt.size + segment_array_size + \
           adler_hat_fmt.size + adler_size
    #'''
    entry['adler_checksum'] = get_adler(entry_data, adler_size)
    entry['adler_method'] = 'adler' + str(adler_size*char_bit)

    return entry


def read_toc(xp3_file):
    # a chunk of toc
    ptr_of_toc, = unpack_from_file(ptr_fmt, xp3_file)
    xp3_file.seek(ptr_of_toc)
    toc_flag_in_file, = unpack_from_file(toc_flag_fmt, xp3_file)
    toc_not_end = toc_not_end_mask & toc_flag_in_file
    toc_compressed_method_in_file = toc_compressed_method_mask & toc_flag_in_file
    assert toc_compressed_method_in_file in toc_compressed_method
    toc_compressed_method_in_file = toc_compressed_method[toc_compressed_method_in_file]
    if toc_compressed_method_in_file[0] == 'raw':
        compressed_size_of_toc, = unpack_from_file(size_fmt, xp3_file)
        original_size_of_toc = compressed_size_of_toc
    else:# if file_toc_compressed_method[0] == 'zlib':
        compressed_size_of_toc, = unpack_from_file(size_fmt, xp3_file)
        original_size_of_toc, = unpack_from_file(size_fmt, xp3_file)

    table_of_contents = xp3_file.read(compressed_size_of_toc)
    table_of_contents = toc_compressed_method_in_file[1](table_of_contents)
    assert len(table_of_contents) == original_size_of_toc

    return (toc_not_end, table_of_contents)


def open_kirikiri_xp3_file(file_name, encoding = None):
    file_size = os.path.getsize(file_name)
    subfiles = {}
    with open(file_name, 'rb') as xp3_file:
        assert xp3_header_fmt.size <= file_size
        file_magic_number, version_and_encoding = unpack_from_file(xp3_header_fmt, xp3_file)
        assert magic_number_of_xp3 == file_magic_number

        # assert version_and_encoding == b'\x01'
        file_version, file_encoding_number = divmod(version_and_encoding[0], 1 << 4)
        assert file_version <= xp3_version_this_module_impl # that is version 0
        if encoding == None:
            encoding = xp3_encoding[file_encoding_number] # only '1' be known when kirikiri2_232r2
        #reader = codecs.getreader(encoding)
        
        ### xp3 of version 0 below
        assert xp3_header_fmt.size + ptr_fmt.size <= file_size

        toc_not_end = True
        while toc_not_end:
            toc_not_end, table_of_contents = read_toc(xp3_file)
            # with io.BytesIO(table_of_contents) as table_of_contents:
            toc_data = subbytes(table_of_contents, 0, 0, len(table_of_contents))
            where = find_hats(toc_data, hat_tag['entry'])
            for location in where:
                entry = get_entry(location, encoding)
                subfile_name = entry['file_name']
                assert subfile_name not in subfiles
                subfiles[subfile_name] = entry
            

    '''
    total_subfiles_size = 0
    for subfile_name, entry in subfiles.items():
        total_subfiles_size += entry['compressed_size']

    #print(ptr_of_toc, xp3_header_fmt.size, total_subfiles_size)
    # it seems not right...
    assert file_size == xp3_header_fmt.size + ptr_fmt.size + total_subfiles_size + \
           toc_header_fmt.size + compressed_size_of_toc
    #'''
    return subfiles

def extract_subfile(to_file, xp3_file, entry):
    adler_method = getattr(zlib, entry['adler_method'])
    adler_checksum = adler_method(b'')
    for segment in entry['segment_array']:
        xp3_file.seek(segment['offset'])
        segment_data = xp3_file.read(segment['compressed_size'])
        compressed_method = segment['compressed_method'][1]
        segment_data = compressed_method(segment_data)
        assert len(segment_data) == segment['original_size']
        adler_checksum = adler_method(segment_data, adler_checksum)
        to_file.write(segment_data)

    adler_checksum &= 0x00FFffFFff
    assert adler_checksum == entry['adler_checksum']
    return entry['file_protected'] # may need to decrypt
        


def extract_kirikiri_xp3_file(to_path, file_name, subfiles):
    with open(file_name, 'rb') as xp3_file:
        for subfile_name, entry in subfiles.items():
            path = os.path.join(to_path, subfile_name)
            where = os.path.dirname(os.path.abspath(path))
            os.makedirs(where,exist_ok=True)
            # what if 'path' be removed here? f*ck!
            try:
                with open(path, 'xb') as subfile:
                    if extract_subfile(subfile, xp3_file, entry):
                        print('Warning: \'', subfile_name, '\' is protected!')
            except FileExistsError as fee:
                subfile_size = os.path.getsize(path)
                if subfile_size != entry['original_size']: raise
                with open(path, 'rb') as existed_file, io.BytesIO() as new_file:
                    extract_subfile(new_file, xp3_file, entry)
                    if existed_file.read(subfile_size) != new_file.getvalue(): raise


def t():
    file = r'C:\game\赤印/bgm.xp3'
    subfiles = open_kirikiri_xp3_file(file, 'utf_16_le')
    print(subfiles.keys())

def t1():
    file = r'C:\game\赤印/patch_old.xp3'
    subfiles = open_kirikiri_xp3_file(file, 'utf_16_le')
    print(subfiles.keys())
    to_path = r'C:\game\赤印/tmp_patch'
    extract_kirikiri_xp3_file(to_path, file, subfiles)

def t2():
    file = r'C:\game\赤印/patch.xp3'
    subfiles = open_kirikiri_xp3_file(file, 'utf_16_le')
    print(subfiles.keys())
    to_path = r'C:\game\赤印/tmp_patch_new'
    extract_kirikiri_xp3_file(to_path, file, subfiles)



# XP3Archive_h XP3Archive_cpp
cpp_source_from = 'kirikiri2_2.32rev2'
XP3Archive_h = '''
//---------------------------------------------------------------------------
/*
	TVP2 ( T Visual Presenter 2 )  A script authoring tool
	Copyright (C) 2000 W.Dee <dee@kikyou.info> and contributors

	See details of license at "license.txt"
*/
//---------------------------------------------------------------------------
// XP3 virtual file system support
//---------------------------------------------------------------------------

#ifndef XP3ArchiveH
#define XP3ArchiveH


#include "StorageIntf.h"



/*[*/
//---------------------------------------------------------------------------
// Extraction filter related
//---------------------------------------------------------------------------
#pragma pack(push, 4)
struct tTVPXP3ExtractionFilterInfo
{
	const tjs_uint SizeOfSelf; // structure size of tTVPXP3ExtractionFilterInfo itself
	const tjs_uint64 Offset; // offset of the buffer data in uncompressed stream position
	void * Buffer; // target data buffer
	const tjs_uint BufferSize; // buffer size in bytes pointed by "Buffer"
	const tjs_uint32 FileHash; // hash value of the file (since inteface v2)

	tTVPXP3ExtractionFilterInfo(tjs_uint64 offset, void *buffer,
		tjs_uint buffersize, tjs_uint32 filehash) :
			Offset(offset), Buffer(buffer), BufferSize(buffersize),
			FileHash(filehash),
			SizeOfSelf(sizeof(tTVPXP3ExtractionFilterInfo)) {;}
};
#pragma pack(pop)

#ifndef TVP_tTVPXP3ArchiveExtractionFilter_CONVENTION
	#ifdef _WIN32
		#define	TVP_tTVPXP3ArchiveExtractionFilter_CONVENTION _stdcall
	#else
		#define TVP_tTVPXP3ArchiveExtractionFilter_CONVENTION
	#endif
#endif
	// TVP_tTVPXP3ArchiveExtractionFilter_CONV is _stdcall on win32 platforms,
	// for backward application compatibility.

typedef void (TVP_tTVPXP3ArchiveExtractionFilter_CONVENTION *
	tTVPXP3ArchiveExtractionFilter)(tTVPXP3ExtractionFilterInfo *info);


/*]*/
//---------------------------------------------------------------------------
TJS_EXP_FUNC_DEF(void, TVPSetXP3ArchiveExtractionFilter, (tTVPXP3ArchiveExtractionFilter filter));
//---------------------------------------------------------------------------





//---------------------------------------------------------------------------
// tTVPXP3Archive  : XP3 ( TVP's native archive format ) Implmentation
//---------------------------------------------------------------------------
#define TVP_XP3_INDEX_ENCODE_METHOD_MASK 0x07
#define TVP_XP3_INDEX_ENCODE_RAW      0
#define TVP_XP3_INDEX_ENCODE_ZLIB     1

#define TVP_XP3_INDEX_CONTINUE   0x80

#define TVP_XP3_FILE_PROTECTED (1<<31)

#define TVP_XP3_SEGM_ENCODE_METHOD_MASK  0x07
#define TVP_XP3_SEGM_ENCODE_RAW       0
#define TVP_XP3_SEGM_ENCODE_ZLIB      1

//---------------------------------------------------------------------------
extern bool TVPIsXP3Archive(const ttstr &name); // check XP3 archive
extern void TVPClearXP3SegmentCache(); // clear XP3 segment cache
//---------------------------------------------------------------------------
struct tTVPXP3ArchiveSegment
{
	tjs_uint64 Start;  // start position in archive storage
	tjs_uint64 Offset; // offset in in-archive storage (in uncompressed offset)
	tjs_uint64 OrgSize; // original segment (uncompressed) size
	tjs_uint64 ArcSize; // in-archive segment (compressed) size
	bool IsCompressed; // is compressed ?
};
//---------------------------------------------------------------------------
class tTVPXP3Archive : public tTVPArchive
{
	ttstr Name;

	struct tArchiveItem
	{
		ttstr Name;
		tjs_uint32 FileHash;
		tjs_uint64 OrgSize; // original ( uncompressed ) size
		tjs_uint64 ArcSize; // in-archive size
		std::vector<tTVPXP3ArchiveSegment> Segments;
		bool operator < (const tArchiveItem &rhs) const
		{
			return this->Name < rhs.Name;
		}
	};

	tjs_int Count;

	std::vector<tArchiveItem> ItemVector;
public:
	tTVPXP3Archive(const ttstr & name);
	~tTVPXP3Archive();

	tjs_uint GetCount() { return Count; }
	const ttstr & GetName(tjs_uint idx) const { return ItemVector[idx].Name; }
	tjs_uint32 GetFileHash(tjs_uint idx) const { return ItemVector[idx].FileHash; }
	ttstr GetName(tjs_uint idx) { return ItemVector[idx].Name; }

	const ttstr & GetName() const { return Name; }

	tTJSBinaryStream * CreateStreamByIndex(tjs_uint idx);

private:
	static bool FindChunk(const tjs_uint8 *data, const tjs_uint8 * name,
		tjs_uint &start, tjs_uint &size);
	static tjs_int16 ReadI16FromMem(const tjs_uint8 *mem);
	static tjs_int32 ReadI32FromMem(const tjs_uint8 *mem);
	static tjs_int64 ReadI64FromMem(const tjs_uint8 *mem);
};
//---------------------------------------------------------------------------





//---------------------------------------------------------------------------
// tTVPXP3ArchiveStream  : XP3 In-Archive Stream Implmentation
//---------------------------------------------------------------------------
class tTVPSegmentData;
class tTVPXP3ArchiveStream : public tTJSBinaryStream
{
	tTVPXP3Archive * Owner;

	tjs_int StorageIndex; // index in archive

	std::vector<tTVPXP3ArchiveSegment> * Segments;
	tTJSBinaryStream * Stream;
	tjs_uint64 OrgSize; // original storage size

	tjs_int CurSegmentNum;
	tTVPXP3ArchiveSegment *CurSegment;
		// currently opened segment ( NULL for not opened )

	tjs_int LastOpenedSegmentNum;

	tjs_uint64 CurPos; // current position in absolute file position

	tjs_uint64 SegmentRemain; // remain bytes in current segment
	tjs_uint64 SegmentPos; // offset from current segment's start

	tTVPSegmentData *SegmentData; // uncompressed segment data

	bool SegmentOpened;

public:
	tTVPXP3ArchiveStream(tTVPXP3Archive *owner, tjs_int storageindex,
		std::vector<tTVPXP3ArchiveSegment> *segments, tTJSBinaryStream *stream,
			tjs_uint64 orgsize);
	~tTVPXP3ArchiveStream();

private:
	void EnsureSegment(); // ensure accessing to current segment
	void SeekToPosition(tjs_uint64 pos); // open segment at 'pos' and seek
	bool OpenNextSegment();


public:
	tjs_uint64 TJS_INTF_METHOD Seek(tjs_int64 offset, tjs_int whence);
	tjs_uint TJS_INTF_METHOD Read(void *buffer, tjs_uint read_size);
	tjs_uint TJS_INTF_METHOD Write(const void *buffer, tjs_uint write_size);
	tjs_uint64 TJS_INTF_METHOD GetSize();

};
//---------------------------------------------------------------------------





#endif

'''


XP3Archive_cpp = '''
//---------------------------------------------------------------------------
/*
	TVP2 ( T Visual Presenter 2 )  A script authoring tool
	Copyright (C) 2000 W.Dee <dee@kikyou.info> and contributors

	See details of license at "license.txt"
*/
//---------------------------------------------------------------------------
// XP3 virtual file system support
//---------------------------------------------------------------------------

#include "tjsCommHead.h"

#include "XP3Archive.h"
#include "MsgIntf.h"
#include "DebugIntf.h"
#include "EventIntf.h"
#include "UtilStreams.h"
#include "SysInitIntf.h"

#include <zlib/zlib.h>
#include <algorithm>

bool TVPAllowExtractProtectedStorage = true;


//---------------------------------------------------------------------------
// archive filter related
//---------------------------------------------------------------------------
tTVPXP3ArchiveExtractionFilter TVPXP3ArchiveExtractionFilter  = NULL;
void TVPSetXP3ArchiveExtractionFilter(tTVPXP3ArchiveExtractionFilter filter)
{
	TVPXP3ArchiveExtractionFilter = filter;
}
//---------------------------------------------------------------------------



//---------------------------------------------------------------------------
// tTVPXP3ArchiveHandleCache
//---------------------------------------------------------------------------
#define TVP_MAX_ARCHIVE_HANDLE_CACHE 8
static tjs_uint TVPArchiveHandleCacheAge = 0;
struct tTVPArchiveHandleCacheItem
{
	void * Pointer;
	tTJSBinaryStream * Stream;
	tjs_uint Age;
};
//---------------------------------------------------------------------------
static tTVPArchiveHandleCacheItem * TVPArchiveHandleCachePool = NULL;
static bool TVPArchiveHandleCacheInit = false;
static bool TVPArchiveHandleCacheShutdown = false;
static tTJSCriticalSection TVPArchiveHandleCacheCS;
//---------------------------------------------------------------------------
static tTJSBinaryStream * TVPGetCachedArchiveHandle(void * pointer, const ttstr & name)
{
	// get cached archive file handle from the pool
	if(TVPArchiveHandleCacheShutdown)
	{
		// the pool has shutdown
		return TVPCreateStream(name);
	}

	tTJSCriticalSectionHolder cs_holder(TVPArchiveHandleCacheCS);

	if(!TVPArchiveHandleCacheInit)
	{
		// initialize the pool
		TVPArchiveHandleCachePool =
			new tTVPArchiveHandleCacheItem[TVP_MAX_ARCHIVE_HANDLE_CACHE];
		for(tjs_int i =0; i < TVP_MAX_ARCHIVE_HANDLE_CACHE; i++)
		{
			TVPArchiveHandleCachePool[i].Pointer = NULL;
			TVPArchiveHandleCachePool[i].Stream = NULL;
			TVPArchiveHandleCachePool[i].Age = 0;
		}
		TVPArchiveHandleCacheInit = true;
	}

	// linear search wiil be enough here because the 
	// TVP_MAX_ARCHIVE_HANDLE_CACHE is relatively small
	for(tjs_int i =0; i < TVP_MAX_ARCHIVE_HANDLE_CACHE; i++)
	{
		tTVPArchiveHandleCacheItem *item =
			TVPArchiveHandleCachePool + i;
		if(item->Stream && item->Pointer == pointer)
		{
			// found in the pool
			tTJSBinaryStream * stream = item->Stream;
			item->Stream = NULL;
			return stream;
		}
	}

	// not found in the pool
	// simply create a stream and return it
	return TVPCreateStream(name);
}
//---------------------------------------------------------------------------
static void TVPReleaseCachedArchiveHandle(void * pointer,
						tTJSBinaryStream * stream)
{
	// release archive file handle
	if(TVPArchiveHandleCacheShutdown) return;
	if(!TVPArchiveHandleCacheInit) return;

	tTJSCriticalSectionHolder cs_holder(TVPArchiveHandleCacheCS);

	// search empty cell in the pool
	tjs_uint oldest_age = 0;
	tjs_int oldest = 0;
	for(tjs_int i = 0; i < TVP_MAX_ARCHIVE_HANDLE_CACHE; i++)
	{
		tTVPArchiveHandleCacheItem *item =
			TVPArchiveHandleCachePool + i;
		if(item->Stream == NULL)
		{
			// found the empty cell; fill it
			item->Pointer = pointer;
			item->Stream = stream;
			item->Age = ++TVPArchiveHandleCacheAge;
				// counter overflow in TVPArchiveHandleCacheAge
				// is not so a big problem.
				// counter overflow can worsen the cache performance,
				// but it occurs only when the counter is overflowed
				// (it's too far less than usual)
			return;
		}

		if(i == 0 || oldest_age > item->Age)
		{
			oldest_age = item->Age;
			oldest = i;
		}
	}

	// empty cell not found
	// free oldest cell and fill it
	tTVPArchiveHandleCacheItem *oldest_item =
		TVPArchiveHandleCachePool + oldest;
	delete oldest_item->Stream, oldest_item->Stream = NULL;
	oldest_item->Pointer = pointer;
	oldest_item->Stream = stream;
	oldest_item->Age = ++TVPArchiveHandleCacheAge;
}
//---------------------------------------------------------------------------
static void TVPFreeArchiveHandlePoolByPointer(void * pointer)
{
	// free all streams which have specified pointer
	if(TVPArchiveHandleCacheShutdown) return;
	if(!TVPArchiveHandleCacheInit) return;

	tTJSCriticalSectionHolder cs_holder(TVPArchiveHandleCacheCS);

	for(tjs_int i = 0; i < TVP_MAX_ARCHIVE_HANDLE_CACHE; i++)
	{
		tTVPArchiveHandleCacheItem *item =
			TVPArchiveHandleCachePool + i;
		if(item->Stream && item->Pointer == pointer)
		{
			delete item->Stream, item->Stream = NULL;
			item->Pointer = NULL;
			item->Age = 0;
		}
	}
}
//---------------------------------------------------------------------------
static void TVPFreeArchiveHandlePool()
{
	// free all streams
	if(TVPArchiveHandleCacheShutdown) return;
	if(!TVPArchiveHandleCacheInit) return;

	tTJSCriticalSectionHolder cs_holder(TVPArchiveHandleCacheCS);

	for(tjs_int i = 0; i < TVP_MAX_ARCHIVE_HANDLE_CACHE; i++)
	{
		tTVPArchiveHandleCacheItem *item =
			TVPArchiveHandleCachePool + i;
		if(item->Stream)
		{
			delete item->Stream, item->Stream = NULL;
			item->Pointer = NULL;
			item->Age = 0;
		}
	}
}
//---------------------------------------------------------------------------
static void TVPShutdownArchiveHandleCache()
{
	// free all stream and shutdown the pool
	tTJSCriticalSectionHolder cs_holder(TVPArchiveHandleCacheCS);

	TVPArchiveHandleCacheShutdown = true;
	if(!TVPArchiveHandleCacheInit) return;

	for(tjs_int i =0; i < TVP_MAX_ARCHIVE_HANDLE_CACHE; i++)
	{
		if(TVPArchiveHandleCachePool[i].Stream)
			delete TVPArchiveHandleCachePool[i].Stream;
	}
	delete [] TVPArchiveHandleCachePool;
}
//---------------------------------------------------------------------------
static tTVPAtExit TVPShutdownArchiveCacheAtExit
	(TVP_ATEXIT_PRI_CLEANUP, TVPShutdownArchiveHandleCache);
//---------------------------------------------------------------------------





//---------------------------------------------------------------------------
// tTVPXP3Archive
//---------------------------------------------------------------------------
/*
	TVP XPK3 virtual file system support. (in short : XP3)
	TVP supports no longer archive type of "XPK1/XPK2"
	( XPK1/XPK2 is used by TVP ver under 0.9x ).

	here word "in-archive" is used for the storages which are contained in
	archive.
*/
//---------------------------------------------------------------------------
static bool TVPGetXP3ArchiveOffset(tTJSBinaryStream *st, const ttstr name,
	tjs_uint64 & offset, bool raise)
{
	st->SetPosition(0);
	tjs_uint8 mark[11+1];
	static tjs_uint8 XP3Mark1[] =
		{ 0x58/*'X'*/, 0x50/*'P'*/, 0x33/*'3'*/, 0x0d/*'\r'*/,
		  0x0a/*'\n'*/, 0x20/*' '*/, 0x0a/*'\n'*/, 0x1a/*EOF*/,
		  0xff /* sentinel */ };
	static tjs_uint8 XP3Mark2[] =
		{ 0x8b, 0x67, 0x01, 0xff/* sentinel */ };

	// XP3 header mark contains:
	// 1. line feed and carriage return to detect corruption by unnecessary
	//    line-feeds convertion
	// 2. 1A EOF mark which indicates file's text readable header ending.
	// 3. 8B67 KANJI-CODE to detect curruption by unnecessary code convertion
	// 4. 01 file structure version and character coding
	//    higher 4 bits are file structure version, currently 0.
	//    lower 4 bits are character coding, currently 1, is BMP 16bit Unicode.

	static tjs_uint8 XP3Mark[11+1];
		// +1: I was warned by CodeGuard that the code will do
		// access overrun... because a number of 11 is not aligned by DWORD, 
		// and the processor may read the value of DWORD at last of this array
		// from offset 8. Then the last 1 byte would cause a fail.
	static bool DoInit = true;
	if(DoInit)
	{
		// the XP3 header above is splitted into two part; to avoid
		// mis-finding of the header in the program's initialized data area.
		DoInit = false;
		memcpy(XP3Mark, XP3Mark1, 8);
		memcpy(XP3Mark + 8, XP3Mark2, 3);
		// here joins it.
	}

	mark[0] = 0; // sentinel
	st->ReadBuffer(mark, 11);
	if(mark[0] == 0x4d/*'M'*/ && mark[1] == 0x5a/*'Z'*/)
	{
		// "MZ" is a mark of Win32/DOS executables,
		// TVP searches the first mark of XP3 archive
		// in the executeble file.
		bool found = false;

		offset = 16;
		st->SetPosition(16);

		// XP3 mark must be aligned by a paragraph ( 16 bytes )
		const tjs_uint one_read_size = 256*1024;
		tjs_uint read;
		tjs_uint8 buffer[one_read_size]; // read 256kbytes at once

		while(0!=(read = st->Read(buffer, one_read_size)))
		{
			tjs_uint p = 0;
			while(p<read)
			{
				if(!memcmp(XP3Mark, buffer + p, 11))
				{
					// found the mark
					offset += p;
					found = true;
					break;
				}
				p+=16;
			}
			if(found) break;
			offset += one_read_size;
		}

		if(!found)
		{
			if(raise)
				TVPThrowExceptionMessage(TVPCannotUnbindXP3EXE, name);
			else
				return false;
		}
	}
	else if(!memcmp(XP3Mark, mark, 11))
	{
		// XP3 mark found
		offset = 0;
	}
	else
	{
		if(raise)
			TVPThrowExceptionMessage(TVPCannotFindXP3Mark, name);
		return false;
	}

	return true;
}
//---------------------------------------------------------------------------
bool TVPIsXP3Archive(const ttstr &name)
{
	tTVPStreamHolder holder(name);
	try
	{
		tjs_uint64 offset;
		return TVPGetXP3ArchiveOffset(holder.Get(), name, offset, false);
	}
	catch(...)
	{
		return false;
	}
}
//---------------------------------------------------------------------------
tTVPXP3Archive::tTVPXP3Archive(const ttstr & name) : tTVPArchive(name)
{
	Name = name;
	Count = 0;

	tjs_uint64 offset;

	tTJSBinaryStream *st = TVPCreateStream(name);

	tjs_uint8 *indexdata = NULL;

	static tjs_uint8 cn_File[] =
		{ 0x46/*'F'*/, 0x69/*'i'*/, 0x6c/*'l'*/, 0x65/*'e'*/ };
	static tjs_uint8 cn_info[] =
		{ 0x69/*'i'*/, 0x6e/*'n'*/, 0x66/*'f'*/, 0x6f/*'o'*/ };
	static tjs_uint8 cn_segm[] =
		{ 0x73/*'s'*/, 0x65/*'e'*/, 0x67/*'g'*/, 0x6d/*'m'*/ };
	static tjs_uint8 cn_adlr[] =
		{ 0x61/*'a'*/, 0x64/*'d'*/, 0x6c/*'l'*/, 0x72/*'r'*/ };

	TVPAddLog(TJS_W("(info) Trying to read XP3 virtual file system "
		"information from : ") +
		name);

	int segmentcount = 0;
	try
	{
		// retrieve archive offset
		TVPGetXP3ArchiveOffset(st, name, offset, true);

		// read index position and seek
		st->SetPosition(11 + offset);

		// read all XP3 indices
		while(true)
		{
			tjs_uint64 index_ofs = st->ReadI64LE();
			st->SetPosition(index_ofs + offset);

			// read index to memory
			tjs_uint8 index_flag;
			st->ReadBuffer(&index_flag, 1);
			tjs_uint index_size;

			if((index_flag & TVP_XP3_INDEX_ENCODE_METHOD_MASK) ==
				TVP_XP3_INDEX_ENCODE_ZLIB)
			{
				// compressed index
				tjs_uint64 compressed_size = st->ReadI64LE();
				tjs_uint64 r_index_size = st->ReadI64LE();

				if((tjs_uint)compressed_size != compressed_size ||
					(tjs_uint)r_index_size != r_index_size)
						TVPThrowExceptionMessage(TVPReadError);
						// too large to handle, or corrupted
				index_size = (tjs_int)r_index_size;
				indexdata = new tjs_uint8[index_size];
				tjs_uint8 *compressed = new tjs_uint8[(tjs_uint)compressed_size];
				try
				{
					st->ReadBuffer(compressed, (tjs_uint)compressed_size);

					unsigned long destlen = (unsigned long)index_size;

					int result = uncompress(  /* uncompress from zlib */
						(unsigned char *)indexdata,
						&destlen, (unsigned char*)compressed,
							(unsigned long)compressed_size);
					if(result != Z_OK ||
						destlen != (unsigned long)index_size)
							TVPThrowExceptionMessage(TVPUncompressionFailed);
				}
				catch(...)
				{
					delete [] compressed;
					throw;
				}
				delete [] compressed;
			}
			else if((index_flag & TVP_XP3_INDEX_ENCODE_METHOD_MASK) ==
				TVP_XP3_INDEX_ENCODE_RAW)
			{
				// uncompressed index
				tjs_uint64 r_index_size = st->ReadI64LE();
				if((tjs_uint)r_index_size != r_index_size)
					TVPThrowExceptionMessage(TVPReadError);
						// too large to handle or corrupted
				index_size = (tjs_uint)r_index_size;
				indexdata = new tjs_uint8[index_size];
				st->ReadBuffer(indexdata, index_size);
			}
			else
			{
				// unknown encode method
				TVPThrowExceptionMessage(TVPReadError);
			}


			// read index information from memory
			tjs_uint ch_file_start = 0;
			tjs_uint ch_file_size = index_size;
			//Count = 0;
			for(;;)
			{
				// find 'File' chunk
				if(!FindChunk(indexdata, cn_File, ch_file_start, ch_file_size))
					break; // not found

				// find 'info' sub-chunk
				tjs_uint ch_info_start = ch_file_start;
				tjs_uint ch_info_size = ch_file_size;
				if(!FindChunk(indexdata, cn_info, ch_info_start, ch_info_size))
					TVPThrowExceptionMessage(TVPReadError);

				// read info sub-chunk
				tArchiveItem item;
				tjs_uint32 flags = ReadI32FromMem(indexdata + ch_info_start + 0);
				if(!TVPAllowExtractProtectedStorage && (flags & TVP_XP3_FILE_PROTECTED))
					TVPThrowExceptionMessage(TJS_W("Specified storage had been protected!"));
				item.OrgSize = ReadI64FromMem(indexdata + ch_info_start + 4);
				item.ArcSize = ReadI64FromMem(indexdata + ch_info_start + 12);

				tjs_int len = ReadI16FromMem(indexdata + ch_info_start + 20);
				ttstr name = TVPStringFromBMPUnicode(
						(const tjs_uint16 *)(indexdata + ch_info_start + 22), len);
				item.Name = name;
				NormalizeInArchiveStorageName(item.Name);

				// find 'segm' sub-chunk
				// Each of in-archive storages can be splitted into some segments.
				// Each segment can be compressed or uncompressed independently.
				// segments can share partial area of archive storage. ( this is used for
				// OggVorbis' VQ code book sharing )
				tjs_uint ch_segm_start = ch_file_start;
				tjs_uint ch_segm_size = ch_file_size;
				if(!FindChunk(indexdata, cn_segm, ch_segm_start, ch_segm_size))
					TVPThrowExceptionMessage(TVPReadError);

				// read segm sub-chunk
				tjs_int segment_count = ch_segm_size / 28;
				tjs_uint64 offset_in_archive = 0;
				for(tjs_int i = 0; i<segment_count; i++)
				{
					tjs_uint pos_base = i * 28 + ch_segm_start;
					tTVPXP3ArchiveSegment seg;
					tjs_uint32 flags = ReadI32FromMem(indexdata + pos_base);

					if((flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) ==
							TVP_XP3_SEGM_ENCODE_RAW)
						seg.IsCompressed = false;
					else if((flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) ==
							TVP_XP3_SEGM_ENCODE_ZLIB)
						seg.IsCompressed = true;
					else
						TVPThrowExceptionMessage(TVPReadError); // unknown encode method
						
					seg.Start = ReadI64FromMem(indexdata + pos_base + 4) + offset;
						// data offset in archive
					seg.Offset = offset_in_archive; // offset in in-archive storage
					seg.OrgSize = ReadI64FromMem(indexdata + pos_base + 12); // original size
					seg.ArcSize = ReadI64FromMem(indexdata + pos_base + 20); // archived size
					item.Segments.push_back(seg);
					offset_in_archive += seg.OrgSize;
					segmentcount ++;
				}

				// find 'aldr' sub-chunk
				tjs_uint ch_adlr_start = ch_file_start;
				tjs_uint ch_adlr_size = ch_file_size;
				if(!FindChunk(indexdata, cn_adlr, ch_adlr_start, ch_adlr_size))
					TVPThrowExceptionMessage(TVPReadError);

				// read 'aldr' sub-chunk
				item.FileHash = ReadI32FromMem(indexdata + ch_adlr_start);

				// push information
				ItemVector.push_back(item);

				// to next file
				ch_file_start += ch_file_size;
				ch_file_size = index_size - ch_file_start;
				Count++;
			}

			if(!(index_flag & TVP_XP3_INDEX_CONTINUE))
				break; // continue reading index when the bit sets
		}

		// sort item vector by its name (required for tTVPArchive specification)
		std::stable_sort(ItemVector.begin(), ItemVector.end());
	}
	catch(...)
	{
		if(indexdata) delete [] indexdata;
		delete st;
		TVPAddLog(TJS_W("(info) Failed."));
		throw;
	}
	if(indexdata) delete [] indexdata;
	delete st;

	TVPAddLog(TJS_W("(info) Done. (contains ") + ttstr(Count) +
		TJS_W(" file(s), ") + ttstr(segmentcount) + TJS_W(" segment(s))"));
}
//---------------------------------------------------------------------------
tTVPXP3Archive::~tTVPXP3Archive()
{
	TVPFreeArchiveHandlePoolByPointer(this);
}
//---------------------------------------------------------------------------
tTJSBinaryStream * tTVPXP3Archive::CreateStreamByIndex(tjs_uint idx)
{
	if(idx >= ItemVector.size()) TVPThrowExceptionMessage(TVPReadError);

	tArchiveItem &item = ItemVector[idx];

	tTJSBinaryStream *stream = TVPGetCachedArchiveHandle(this, Name);

	tTJSBinaryStream *out;
	try
	{
		out = new tTVPXP3ArchiveStream(this, idx, &(item.Segments), stream,
			item.OrgSize);
	}
	catch(...)
	{
		TVPReleaseCachedArchiveHandle(this, stream);
		throw;
	}

	return out;
}
//---------------------------------------------------------------------------
bool tTVPXP3Archive::FindChunk(const tjs_uint8 *data, const tjs_uint8 * name,
		tjs_uint &start, tjs_uint &size)
{
	tjs_uint start_save = start;
	tjs_uint size_save = size;

	tjs_uint pos = 0;
	while(pos < size)
	{
		bool found = !memcmp(data + start, name, 4);
		start += 4;
		tjs_uint64 r_size = ReadI64FromMem(data + start);
		start += 8;
		tjs_uint size_chunk = (tjs_uint)r_size;
		if(size_chunk != r_size)
			TVPThrowExceptionMessage(TVPReadError);
		if(found)
		{
			// found
			size = size_chunk;
			return true;
		}
		start += size_chunk;
		pos += size_chunk + 4 + 8;
	}

	start = start_save;
	size = size_save;
	return false;
}
//---------------------------------------------------------------------------
tjs_int16 tTVPXP3Archive::ReadI16FromMem(const tjs_uint8 *mem)
{
	return (tjs_int16)mem[0] + ((tjs_int16)mem[1] << 8);
}
//---------------------------------------------------------------------------
tjs_int32 tTVPXP3Archive::ReadI32FromMem(const tjs_uint8 *mem)
{
	return (tjs_int32)mem[0] + ((tjs_int32)mem[1] << 8) +
		((tjs_int32)mem[2] << 16) + ((tjs_int32)mem[3] << 24);
}
//---------------------------------------------------------------------------
tjs_int64 tTVPXP3Archive::ReadI64FromMem(const tjs_uint8 *mem)
{
	tjs_int32 low = ReadI32FromMem(mem);
	tjs_int32 high = ReadI32FromMem(mem + 4);
	return ((tjs_int64)high << 32) | ((tjs_int64)low);
}
//---------------------------------------------------------------------------




//---------------------------------------------------------------------------
// Compressed segment cache related
//---------------------------------------------------------------------------
#define TVP_SEGCACHE_ONE_LIMIT (1024*1024)     // max size limit for each segment
#define TVP_SEGCACHE_TOTAL_LIMIT (1024*1024)   // total segment cache size
tjs_uint TVPSegmentCacheLimit = TVP_SEGCACHE_TOTAL_LIMIT;
//---------------------------------------------------------------------------
struct tTVPSegmentCacheSearchData
{
	ttstr Name; // archive name
	tjs_int StorageIndex; // storage index in archive
	tjs_int SegmentIndex; // segment index in storage

	bool operator == (const tTVPSegmentCacheSearchData &rhs) const
	{
		return Name == rhs.Name && StorageIndex == rhs.StorageIndex &&
			SegmentIndex == rhs.SegmentIndex;
	}
};
//---------------------------------------------------------------------------
class tTVPSegmentCacheSearchHashFunc
{
public:
	static tjs_uint32 Make(const tTVPSegmentCacheSearchData &val)
	{
		tjs_uint32 v = tTJSHashFunc<ttstr>::Make(val.Name);

		v ^= val.StorageIndex;
		v ^= (val.SegmentIndex<<2);
		return v;
	}
};
//---------------------------------------------------------------------------
class tTVPSegmentData
{
	tjs_int RefCount;
	tjs_uint Size;
	tjs_uint8 *Data;

public:
	tTVPSegmentData() { RefCount = 1; Size = 0; Data = NULL; }
	~tTVPSegmentData() { if(Data) delete [] Data; }

	void SetData(unsigned long outsize, tTJSBinaryStream *instream,
		unsigned long insize)
	{
		// uncompress data
		tjs_uint8 * indata = new tjs_uint8 [insize];
		try
		{
			instream->Read(indata, insize);

			Data = new tjs_uint8 [outsize];
			unsigned long destlen = outsize;
			int result = uncompress( (unsigned char*)Data, &outsize,
				(unsigned char*)indata, insize);
			if(result != Z_OK || destlen != outsize)
				TVPThrowExceptionMessage(TVPUncompressionFailed);
			Size = outsize;
		}
		catch(...)
		{
			delete [] indata;
			throw;
		}
		delete [] indata;
	}

	const tjs_uint8 * GetData() const { return Data; }
	tjs_uint GetSize() const { return Size; }

	void AddRef() { RefCount ++; }
	void Release()
	{
		if(RefCount == 1)
		{
			delete this;
		}
		else
		{
			RefCount--;
		}
	}
};
//---------------------------------------------------------------------------
typedef tTJSRefHolder<tTVPSegmentData> tTVPSegmentDataHolder;

typedef
tTJSHashTable<tTVPSegmentCacheSearchData, tTVPSegmentDataHolder, tTVPSegmentCacheSearchHashFunc>
	tTVPSegmentCache;
static tTVPSegmentCache TVPSegmentCache;
static tjs_uint TVPSegmentCacheTotalBytes = 0;

static tTJSCriticalSection TVPSegmentCacheCS;
//---------------------------------------------------------------------------
static void TVPCheckSegmentCacheLimit()
{
	tTJSCriticalSectionHolder cs_holder(TVPSegmentCacheCS);

	while(TVPSegmentCacheTotalBytes > TVPSegmentCacheLimit)
	{
		// chop last segment
		tTVPSegmentCache::tIterator i;
		i = TVPSegmentCache.GetLast();
		if(!i.IsNull())
		{
			tjs_uint size = i.GetValue().GetObjectNoAddRef()->GetSize();
			TVPSegmentCacheTotalBytes -= size;
			TVPSegmentCache.ChopLast(1);
		}
		else
		{
			break;
		}
	}
}
//---------------------------------------------------------------------------
void TVPClearXP3SegmentCache()
{
	tTJSCriticalSectionHolder cs_holder(TVPSegmentCacheCS);

	TVPSegmentCache.Clear();
	TVPSegmentCacheTotalBytes = 0;
}
//---------------------------------------------------------------------------
struct tTVPClearSegmentCacheCallback : public tTVPCompactEventCallbackIntf
{
	virtual void TJS_INTF_METHOD OnCompact(tjs_int level)
	{
		if(level >= TVP_COMPACT_LEVEL_DEACTIVATE)
		{
			// clear the segment cache on application deactivate
			TVPClearXP3SegmentCache();
			// also free archive handle pool
			TVPFreeArchiveHandlePool();
		}
	}
} static TVPClearSegmentCacheCallback;
static bool TVPClearSegmentCacheCallbackInit = false;
//---------------------------------------------------------------------------
static tTVPSegmentData * TVPSearchFromSegmentCache(
	const tTVPSegmentCacheSearchData &sdata, tjs_uint32 hash)
{
	tTJSCriticalSectionHolder cs_holder(TVPSegmentCacheCS);

	tTVPSegmentDataHolder * ptr =
		TVPSegmentCache.FindAndTouchWithHash(sdata, hash);
	if(ptr)
	{
		// found in cache
		return ptr->GetObject(); // add-refed
	}

	return NULL; // not found in cache
}
//---------------------------------------------------------------------------
static void TVPPushToSegmentCache(const tTVPSegmentCacheSearchData &sdata, tjs_uint32 hash,
	tTVPSegmentData *data)
{
	if(!TVPClearSegmentCacheCallbackInit)
	{
		TVPAddCompactEventHook(&TVPClearSegmentCacheCallback);
		TVPClearSegmentCacheCallbackInit = true;
	}

	tTJSCriticalSectionHolder cs_holder(TVPSegmentCacheCS);

	tTVPSegmentDataHolder holder(data);
	TVPSegmentCache.AddWithHash(sdata, hash, holder);
	TVPSegmentCacheTotalBytes += data->GetSize();

	TVPCheckSegmentCacheLimit();
}
//---------------------------------------------------------------------------






//---------------------------------------------------------------------------
// tTVPXP3ArchiveStream : stream class for in-archive storage
//---------------------------------------------------------------------------
tTVPXP3ArchiveStream::tTVPXP3ArchiveStream(tTVPXP3Archive *owner,
	tjs_int storageindex,
	std::vector<tTVPXP3ArchiveSegment> *segments, tTJSBinaryStream * stream,
		tjs_uint64 orgsize)
{
	StorageIndex = storageindex;
	Segments = segments;
	SegmentData = NULL;
	CurSegmentNum = 0;
	CurSegment = &(Segments->operator [](0));
	SegmentPos = 0;
	SegmentRemain = CurSegment->OrgSize;
	SegmentOpened = false;
	CurPos = 0;

	LastOpenedSegmentNum = -1;

	Owner = owner;
	Owner->AddRef(); // hook
	Stream = stream;
	OrgSize = orgsize;
}
//---------------------------------------------------------------------------
tTVPXP3ArchiveStream::~tTVPXP3ArchiveStream()
{
	TVPReleaseCachedArchiveHandle(Owner, Stream);
	Owner->Release(); // unhook
	if(SegmentData) SegmentData->Release();
}
//---------------------------------------------------------------------------
void tTVPXP3ArchiveStream::EnsureSegment()
{
	// ensure accessing to current segment
	if(SegmentOpened) return;

	if(LastOpenedSegmentNum == CurSegmentNum)
	{
		if(!CurSegment->IsCompressed)
			Stream->SetPosition(CurSegment->Start + SegmentPos);
		return;
	}

	// erase buffer
	if(SegmentData) SegmentData->Release(), SegmentData = NULL;

	// is compressed segment ?
	if(CurSegment->IsCompressed)
	{
		// a compressed segment

		if(CurSegment->OrgSize >= TVP_SEGCACHE_ONE_LIMIT)
		{
			// too large to cache
			Stream->SetPosition(CurSegment->Start);
			SegmentData = new tTVPSegmentData;
			SegmentData->SetData((tjs_uint)CurSegment->OrgSize,
				Stream, (tjs_uint)CurSegment->ArcSize);
		}
		else
		{
			// search thru segment cache
			tTVPSegmentCacheSearchData sdata;
			sdata.Name = Owner->GetName();
			sdata.StorageIndex = StorageIndex;
			sdata.SegmentIndex = CurSegmentNum;

			tjs_uint32 hash;
			hash = tTVPSegmentCacheSearchHashFunc::Make(sdata);

			SegmentData = TVPSearchFromSegmentCache(sdata, hash);
			if(!SegmentData)
			{
				// not found in cache
				Stream->SetPosition(CurSegment->Start);
				SegmentData = new tTVPSegmentData;
				SegmentData->SetData((tjs_uint)CurSegment->OrgSize,
					Stream, (tjs_uint)CurSegment->ArcSize);

				// add to cache
				TVPPushToSegmentCache(sdata, hash, SegmentData);
			}
		}
	}
	else
	{
		// not a compressed segment

		Stream->SetPosition(CurSegment->Start + SegmentPos);
	}

	SegmentOpened = true;
	LastOpenedSegmentNum = CurSegmentNum;
}
//---------------------------------------------------------------------------
void tTVPXP3ArchiveStream::SeekToPosition(tjs_uint64 pos)
{
	// open segment at 'pos' and seek
	// pos must between zero thru OrgSize
	if(CurPos == pos) return;

	// do binary search to determine current segment number
	tjs_int st = 0;
	tjs_int et = Segments->size();
	tjs_int seg_num;

	while(true)
	{
		if(et-st <= 1) { seg_num = st; break; }
		tjs_int m = st + (et-st)/2;
		if(Segments->operator[](m).Offset > pos)
			et = m;
		else
			st = m;
	}

	CurSegmentNum = seg_num;
	CurSegment = &(Segments->operator [](CurSegmentNum));
	SegmentOpened = false;

	SegmentPos = pos - CurSegment->Offset;
	SegmentRemain = CurSegment->OrgSize - SegmentPos;
	CurPos = pos;
}
//---------------------------------------------------------------------------
bool tTVPXP3ArchiveStream::OpenNextSegment()
{
	// open next segment
	if(CurSegmentNum == (tjs_int)(Segments->size() -1))
		return false; // no more segments
	CurSegmentNum ++;
	CurSegment = &(Segments->operator [](CurSegmentNum));
	SegmentOpened = false;
	SegmentPos = 0;
	SegmentRemain = CurSegment->OrgSize;
	CurPos = CurSegment->Offset;
	EnsureSegment();
	return true;
}
//---------------------------------------------------------------------------
tjs_uint64 TJS_INTF_METHOD tTVPXP3ArchiveStream::Seek(tjs_int64 offset, tjs_int whence)
{
	tjs_int64 newpos;
	switch(whence)
	{
	case TJS_BS_SEEK_SET:
		newpos = offset;
		if(offset >= 0 && offset <= OrgSize)
		{
			SeekToPosition(newpos);
		}
		return CurPos;

	case TJS_BS_SEEK_CUR:
		newpos = offset + CurPos;
		if(offset >= 0 && offset <= OrgSize)
		{
			SeekToPosition(newpos);
		}
		return CurPos;

	case TJS_BS_SEEK_END:
		newpos = offset + OrgSize;
		if(offset >= 0 && offset <= OrgSize)
		{
			SeekToPosition(newpos);
		}
		return CurPos;
	}
	return CurPos;
}
//---------------------------------------------------------------------------
tjs_uint TJS_INTF_METHOD tTVPXP3ArchiveStream::Read(void *buffer, tjs_uint read_size)
{
	EnsureSegment();

	tjs_uint write_size = 0;
	while(read_size)
	{
		while(SegmentRemain == 0)
		{
			// must go next segment
			if(!OpenNextSegment()) // open next segment
				return write_size; // could not read more
		}

		tjs_uint one_size =
			read_size > SegmentRemain ? (tjs_uint)SegmentRemain : read_size;

		if(CurSegment->IsCompressed)
		{
			// compressed segment; read from uncompressed data in memory
			memcpy((tjs_uint8*)buffer + write_size,
				SegmentData->GetData() + (tjs_uint)SegmentPos, one_size);
		}
		else
		{
			// read directly from stream
			Stream->ReadBuffer((tjs_uint8*)buffer + write_size, one_size);
		}

		// execute filter (for encryption method)
		if(TVPXP3ArchiveExtractionFilter)
		{
			tTVPXP3ExtractionFilterInfo info(CurPos, (tjs_uint8*)buffer + write_size,
				one_size, Owner->GetFileHash(StorageIndex));
			TVPXP3ArchiveExtractionFilter
				( (tTVPXP3ExtractionFilterInfo*) &info );
		}

		// adjust members
		SegmentPos += one_size;
		CurPos += one_size;
		SegmentRemain -= one_size;
		read_size -= one_size;
		write_size += one_size;
	}

	return write_size;
}
//---------------------------------------------------------------------------
tjs_uint TJS_INTF_METHOD tTVPXP3ArchiveStream::Write(const void *buffer, tjs_uint write_size)
{
	return 0;
}
//---------------------------------------------------------------------------
tjs_uint64 TJS_INTF_METHOD tTVPXP3ArchiveStream::GetSize()
{
	return OrgSize;
}
//---------------------------------------------------------------------------





//---------------------------------------------------------------------------
// Archive extraction utility
//---------------------------------------------------------------------------
#define TVP_LOCAL_TEMP_COPY_BLOCK_SIZE 65536*2
#if 0
// this routine is obsoleted because the Releaser includes over 256-characters
// file name if the user specifies "protect over the archive" option.
// Windows cannot handle such too long filename.
void TVPExtractArchive(const ttstr & name, const ttstr & _destdir, bool allowextractprotected)
{
	// extract file to
	bool TVPAllowExtractProtectedStorage_save =
		TVPAllowExtractProtectedStorage;
	TVPAllowExtractProtectedStorage = allowextractprotected;
	try
	{

		ttstr destdir(_destdir);
		tjs_char last = _destdir.GetLastChar();
		if(_destdir.GetLen() >= 1 && (last != TJS_W('/') && last != TJS_W('\\')))
			destdir += TJS_W('/');

		tTVPArchive *arc = TVPOpenArchive(name);
		try
		{
			tjs_int count = arc->GetCount();
			for(tjs_int i = 0; i < count; i++)
			{
				ttstr name = arc->GetName(i);

				tTJSBinaryStream *src = arc->CreateStreamByIndex(i);
				try
				{
					tTVPStreamHolder dest(destdir + name, TJS_BS_WRITE);
					tjs_uint8 * buffer = new tjs_uint8[TVP_LOCAL_TEMP_COPY_BLOCK_SIZE];
					try
					{
						tjs_uint read;
						while(true)
						{
							read = src->Read(buffer, TVP_LOCAL_TEMP_COPY_BLOCK_SIZE);
							if(read == 0) break;
							dest->WriteBuffer(buffer, read);
						}
					}
					catch(...)
					{
						delete [] buffer;
						throw;
					}
					delete [] buffer;
				}
				catch(...)
				{
//					delete src;
//					throw;
				}
				delete src;
			}

		}
		catch(...)
		{
			arc->Release();
			throw;
		}

		arc->Release();
	}
	catch(...)
	{
		TVPAllowExtractProtectedStorage =
			TVPAllowExtractProtectedStorage_save;
		throw;
	}
	TVPAllowExtractProtectedStorage =
		TVPAllowExtractProtectedStorage_save;
}
#endif
//---------------------------------------------------------------------------


'''



