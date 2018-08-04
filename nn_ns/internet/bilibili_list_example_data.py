


import os
from sand import save_value

write_ls = save_value.write_value
read_ls = save_value.read_value


path = r'E:/my_data/program_source/python3_src/root/internet/'
tv_drama_cn = path + 'bilibili_list_example_data_tv_drama_cn'
music_dance = path + 'bilibili_list_example_data_music_dance'

'''
def _t1(fn, ls):
    if not os.path.exists(fn):
        write_ls(ls, fn)
    ls_r = read_ls(fn)
    
    assert ls == ls_r

def _t2(fn_ls):
    for fn, ls in fn_ls:
        _t1(fn, ls)

from bilibili_list_example_data_tv_drama_cn import ls as tv_drama_cn_ls
from bilibili_list_example_data_music_dance import ls as music_dance_ls

fn_ls = [(tv_drama_cn, tv_drama_cn_ls), (music_dance, music_dance_ls)]

'''
    
tv_drama_cn_ls = read_ls(tv_drama_cn)
music_dance_ls = read_ls(music_dance)

if __name__ == "__main__":
    pass





    
