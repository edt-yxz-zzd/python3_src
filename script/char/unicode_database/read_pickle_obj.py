
import pickle
import pprint

file_names = '''
    han2ntype2number.py.obj
    han2variant2vtype2srcs.py.obj
    vary_charss.py.obj
    '''.split()

def read_pickle_obj(file):
    return pickle.load(file)
for fname in file_names:
    with open(fname, 'rb') as fin:
        obj = read_pickle_obj(fin)
    with open(f'{fname}.txt', 'xt', encoding='utf8') as fout:
        pprint.pprint(obj, stream=fout)

