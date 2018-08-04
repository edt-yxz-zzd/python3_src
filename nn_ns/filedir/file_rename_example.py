

from file_rename import \
     list_files, \
     name_filter, \
     generate_new_names, \
     join_path_basenames, \
     rename_to


def t():
    path = r'D:\software\programming\library' + \
           r'\graph\planar\plantri45\txt\CubicPolyhedralGraph\c2sub/'
    fname = [\
        '0#0#012##4#145#245',\
        '0#0#0##1#245#34#347#125',\
        '0#0#02##4#45#16#145#237',\
        '0#0#02##4#14#146#25#358',\
        '0#0#0###5#34#347#156#256#124',\
        '0#0#0##4#4#56#267#345#12#13A',\
        '0#0#0##4#45##367#245#137#127',\
        '0#0#0##4#45#4#267#357#12#13A',\
        '0#0#0##4#45#1#37#268#345#127',\
        '0#0#0##4#45#1#27#368#345#127',\
        '0#0#02###5#56#467#14#145#239',\
        '0#0#02##4##6#567#145#367#124',\
        '0#0#02##4##56#56#148#167#234',\
        '0#0#02##4##46#567#16#145#239',\
        '0#0#02##4#5#56#16#178#24#34A',\
        '0#0#02##4#4#5#67#157#168#234',\
        '0#0#02##4#45#56#7#18#389#124',\
        '0#0#02##4#45#56#7#18#189#234',\
        '0#0#012##4#45#6#45#7#289#179',\
        ]
    old_files = [fn+'.png' for fn in fname]
    new_files = [str(i).zfill(4) + '#' + old for i, old in enumerate(old_files, 2001)]
    old_path_names = join_path_basenames(path, old_files)
    new_path_names = join_path_basenames(path, new_files)
    #return (old_path_names, new_path_names)
    rename_to(old_path_names, new_path_names)


def t6():
    path = r'D:\software\programming\library' + \
           r'\graph\planar\plantri45\txt\\CubicPolyhedralGraph/'
    fname = [\
        '0#0#0###5#14#245#346#356#127',\
        '0#0#0##4#5#36#36#248#157#124',\
        '0#0#0##4#5#14#24#368#356#127',\
        '0#0#0##4#4#5#367#257#136#124',\
        '0#0#0##4#4#5#346#257#136#127',\
        '0#0#0##4#4#4#267#357#126#135',\
        '0#0#0##4#4#35#36#157#268#124',\
        '0#0#0##4#45#4#27#378#126#135',\
        '0#0#02##4#5#56#16#17#348#249',\
        '0#0#02##4#4#5#16#178#346#257',\
        '0#0#02##4#4#56#7#168#358#124',\
        '0#0#02##4#45#6#7#358#178#124',\
        '0#0#02##4#45#6#7#158#378#124',\
        '0#0#02##4#45#6#57#18#379#124',\
        ]
    old_files = [fn+'.png' for fn in fname]
    new_files = [str(i).zfill(4) + '#' + old for i, old in enumerate(old_files, 10)]
    old_path_names = join_path_basenames(path, old_files)
    new_path_names = join_path_basenames(path, new_files)
    #return (old_path_names, new_path_names)
    rename_to(old_path_names, new_path_names)




def t5(n):
    if n > 0:
        path = 'E:/temp_output/video'
        all_files = list_files(path)
        old_files = name_filter(all_files,
                                r'叛逆的鲁鲁修第二季.*\d+.*（流畅）\.f4v')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '叛逆的鲁鲁修02_', 2, 0, '（流畅）.f4v')
        #print(old_files, new_files)
        for idx,old,new in zip(range(len(old_files)), old_files, new_files):
            print(idx, old, new)

    if n > 1:
        old_path_names = join_path_basenames(path, old_files)
        new_path_names = join_path_basenames(path, new_files)
        #print(old_path_names, new_path_names)
        for idx, old, new in zip(range(len(old_files)), \
                               old_path_names, \
                               new_path_names):
            print(idx, old, new)

    if n > 2:
        rename_to(old_path_names, new_path_names)




def t4(n):
    if n > 0:
        path = 'E:/temp_output/video'
        all_files = list_files(path)
        old_files = name_filter(all_files,
                                r'只有神知道的世界II.*\d+.*（清晰）\.f4v')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '只有神知道的世界02_', 2, 0, '（清晰）.f4v')
        #print(old_files, new_files)
        for idx,old,new in zip(range(len(old_files)), old_files, new_files):
            print(idx, old, new)

    if n > 1:
        old_path_names = join_path_basenames(path, old_files)
        new_path_names = join_path_basenames(path, new_files)
        #print(old_path_names, new_path_names)
        for idx, old, new in zip(range(len(old_files)), \
                               old_path_names, \
                               new_path_names):
            print(idx, old, new)

    if n > 2:
        rename_to(old_path_names, new_path_names)














def t1(i):
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



def t2(n):
    if n > 0:
        path = 'E:/multimedia/video'
        all_files = list_files(path)
        old_files = name_filter(all_files,
                                r'出包王女.*\d\d\（流畅）\.f4v')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '出包王女02_', 2, 0, '.f4v')
        #print(old_files, new_files)
        for idx,old,new in zip(range(len(old_files)), old_files, new_files):
            print(idx, old, new)

    if n > 1:
        old_path_names = join_path_basenames(path, old_files)
        new_path_names = join_path_basenames(path, new_files)
        #print(old_path_names, new_path_names)
        for idx, old, new in zip(range(len(old_files)), \
                               old_path_names, \
                               new_path_names):
            print(idx, old, new)

    if n > 2:
        rename_to(old_path_names, new_path_names)



def t3(n):
    if n > 0:
        path = 'E:/temp_output/video'
        all_files = list_files(path)
        old_files = name_filter(all_files,
                                r'只有神知道的世界.*\d+.*（流畅）\.f4v')
        new_files = generate_new_names(old_files, r'(\d+)', 1, \
                                        '只有神知道的世界01_', 2, 0, '（流畅）.f4v')
        #print(old_files, new_files)
        for idx,old,new in zip(range(len(old_files)), old_files, new_files):
            print(idx, old, new)

    if n > 1:
        old_path_names = join_path_basenames(path, old_files)
        new_path_names = join_path_basenames(path, new_files)
        #print(old_path_names, new_path_names)
        for idx, old, new in zip(range(len(old_files)), \
                               old_path_names, \
                               new_path_names):
            print(idx, old, new)

    if n > 2:
        rename_to(old_path_names, new_path_names)








