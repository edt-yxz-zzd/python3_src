#from jidianzhengmaciku2zmls import zmls
from zmls2dicts import gen_dicts
#zm2hzs, hz2zms, hz2pre = gen_dicts(zmls)

def hz2zms2ls(hz2zms):
    hz_zms_ls = [(hz2num_gb2int(hz), sorted(zms)) for hz, zms in hz2zms.items()]
    hz_zms_ls.sort()
    hz_zms_ls = [(num2hz_int2gb(hz), zms) for hz, zms in hz_zms_ls]
    return hz_zms_ls

def gen_hz_zms_ls(hz2zms):
    zm2hzs, hz2zms, hz2pre = gen_dicts(zmls)
    return hz2zms2ls(hz2zms)

def write_hz_zms_ls(hz_zms_ls, hz_zms_fname=hz_zms_fname, encoding=encoding):
    with open(hz_zms_fname, 'x', encoding=encoding) as fout:
        for hz, zms in hz_zms_ls:
            s = '{} {}\n'.format(hz, ' '.join(zms))
            fout.write(s)


def subset_zmls(zmls, pre_filter=('', '~')):# 去除用户自定义的
    zmls = [(zm, [(hz, pre) for hz, pre in chars if pre in pre_filter]) \
            for zm, chars in zmls] 
    zmls = [(zm, chars) for zm, chars in zmls if chars]
    #assert zmls
    return zmls

def t():
    from jidianzhengmaciku2zmls import zmls
    zmls = subset_zmls(zmls, ('', '~'))# 去除用户自定义的
    write_hz_zms_ls(gen_hz_zms_ls(zmls))
    zmls = subset_zmls(zmls, ('',))# 去除生僻的
    write_hz_zms_ls(gen_hz_zms_ls(zmls), hz_zms_fname[:-4]+'_easy.txt')

