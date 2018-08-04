
"""
os.listdir(path='.')
os.path.lexists(path) 
os.path.isfile(path)
os.path.isdir(path) 
os.path.join(path1[, path2[, ...]]) 


re.
re.compile(pattern, flags=0)
prog = re.compile(pattern)
result = prog.match(string)
re.split(pattern, string, maxsplit=0, flags=0) 


os.rename(src, dst) 


list all file names in thd diretory $path
scanf - re.match/split - pick up names that match the regular expression $rex_filter (note: file or folder!!)
printf - str.format - generate new names
check whether the new names are available
rename them

"""


import os, re

def list_files(path): # -> [file_names]
    ls = os.listdir(path)
    return [fn for fn in ls if os.path.isfile(os.path.join(path, fn))]


def list_folders(path): # -> [folder_names]
    ls = os.listdir(path)
    return [fn for fn in ls if os.path.isdir(os.path.join(path, fn))]


def name_filter(all_names, filter_pattern): # -> [old_names]
    re_filter = re.compile(filter_pattern)
    return [name for name in all_names if re_filter.match(name)]




def generate_new_names(old_names, split_pattern, num_index, \
                        pre_str, mid_num_digits, mid_num_offset, post_str):
    '''
    old_names = ['8.???BookXXX_Volume7_chapter5_NameYYY.pdf']
    split_pattern = r'(\d+)' # => ['', '8', *, '7', *, '5', *] 
    num_index = 5 # -> '5' at location 5
                  # note: if not '8', -> [*, '7', *, '5', *]
                  # first item and last one never match $split_pattern
    pre = 'XXX_'
    mid_num_digits = 3  # => '5' to '005'
    mid_num_offset = 17 # '022'if number of chapters in pre-volumes is 12
    post_str = '.pdf'

    return ['XXX_022.pdf']
    '''
    new_names = []
    format_str = pre_str + '{num:0>' + str(mid_num_digits) + '}' + post_str
    for name in old_names:
        #print(re.split(split_pattern, name))
        num = int(re.split(split_pattern, name)[num_index]) + mid_num_offset
        new_name = format_str.format(num = num)
        new_names.append(new_name)

    return new_names

'''''
print(generate_new_names(['8.???BookXXX_Volume7_chapter5_NameYYY.pdf'],\
                           r'(\d+)', 5, 'XXX_', 3, 17, '.pdf'))

print(generate_new_names(['.???BookXXX_Volume7_chapter5_NameYYY.pdf'],\
                           r'(\d+)', 3, 'XXX_', 3, 17, '.pdf'))

#'''


def join_path_basenames(path, basenames):
    return [os.path.join(path, basename) for basename in basenames]


def get_existing_paths(paths): # -> [denied_names]
    return [path for path in paths if os.path.lexists(path)]


def rename_to(old_paths, new_paths): # -> None
    assert len(old_paths) == len(new_paths) == \
           len(set(new_paths)) == len(get_existing_paths(old_paths))
    assert len(get_existing_paths(new_paths)) == 0
    
    for src,dst in zip(old_paths,new_paths):
        os.rename(src,dst)
        
def fname_from_txt_line(txt_fname, encoding=None):
    ls = []
    with open(txt_fname, encoding = encoding) as fin:
        for line in fin:
            ls.append(line[:-1])
    return ls

def rename_by_fname_from_txt(oldname_txtfn, newname_txtfn, path='.', encoding=None):

    def to_names(name_txtfn):
        names = fname_from_txt_line(name_txtfn, encoding = encoding)
        names = join_path_basenames(path, names)
        return names
    
    olds = to_names(oldname_txtfn)
    news = to_names(newname_txtfn)
    
    old_new_ls = [(old, new) for old, new in zip(olds, news) if old != new]
    olds = [old for old, new in old_new_ls]
    news = [new for old, new in old_new_ls]

    rename_to(olds, news)
    return




def t1(i):
    if i > 0:
        path = 'E:/picture/comic/一起一起这里那里（未完）！！！/卷2/p2'
        all_files = list_files(path)
        old_files = name_filter(all_files, r'\d+.jpg')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '', 3, 28, '.jpg')
        print(old_files, new_files)

    if i > 1:
        old_path_names = join_path_names(path, old_files)
        new_path_names = join_path_names(path, new_files)
        rename_to(old_path_names, new_path_names)
    
def t2():
    path_prefix = 'E:/picture/comic/一起一起这里那里（未完）！！！/卷3/3'
    from_px = 1
    to_px = 7
    paths = []
    for i in range(from_px,to_px+1):
        paths.append(path_prefix + str(i))

    offset = 0
    offsets = []
    for path in paths:
        offsets.append(offset)
        offset += len(list_files(path))

    print(offsets)
    for j in range(from_px+1,to_px+1):
        i = j-1
        path = paths[i]
        offset = offsets[i]
        all_files = list_files(path)
        old_files = name_filter(all_files, r'\d+.jpg')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '', 3, offset, '.jpg')
        #print(old_files, new_files)
        print(new_files)

        old_path_names = join_path_names(path, old_files)
        new_path_names = join_path_names(path, new_files)
        #rename_to(old_path_names, new_path_names)




def t3(i):
    if i > 0:
        path = 'E:/multimedia/video'
        all_files = list_files(path)
        old_files = name_filter(all_files,
                                r'\[Kaicn&Kisssub\]\[To_Love_Ru\]' \
                                r'\d\d\[BIG5\]\[868×480\]（流畅）.f4v')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '出包王女01_', 2, 0, '.f4v')
        print(old_files, new_files)

    if i > 1:
        old_path_names = join_path_basenames(path, old_files)
        new_path_names = join_path_basenames(path, new_files)
        print(old_path_names, new_path_names)

    if i > 2:
        rename_to(old_path_names, new_path_names)





