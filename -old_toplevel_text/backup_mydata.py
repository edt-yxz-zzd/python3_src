# py3
'''
7z.exe -xr!__pycache__ -xr!*.pyc a -t7z -x!<FOLDER>/xxx target.7z source
'''


import os.path
from datetime import datetime
from sand import default_WorkingPath, to_names
from sand.big.makedirs import makedirs
from subprocess import check_call
from nn_ns.fileformat.auto_backup import auto_backup

exe7z = r'C:\Program Files\7-Zip\7z.exe'
root = r'E:\my_data'
today = datetime.today()
date = '{:%Y%m%d}'.format(today)
exclude_onefile_fmt = r'-x!{}'
exe7z_args = [exe7z] + r'-xr!__pycache__ -xr!*.pyc a -t7z'.split()

names = 'program_source, program_config, backup, my_record_txt'
names = to_names(names)
program_source, program_config, backup, my_record_txt = names

joiner = default_WorkingPath.joiner__variables(root)
joiner(globals(), names)

assert program_source == os.path.join(root, 'program_source')
program_source_path = program_source
backup_root = backup
dated_backup_root = os.path.join(backup_root, '[{}]my_data'.format(date))
program_config_path = program_config
my_record_txt_path = my_record_txt









def pack_program_source(date, exe7z_args, program_source_path, dated_backup_root):
    '''
    7z.bin a -t7z "[%date%}]program_source(exclude C++ py3 renpy svn).7z" %program_source% -xr!__pycache__ -xr!*.pyc
    7z.bin a -t7z [%date%}]python3_src.7z %program_source%\python3_src -xr!__pycache__ -xr!*.pyc
    7z.bin a -t7z [%date%]c++.7z %program_source%\c++
'''
    basename = os.path.basename(program_source_path)
    backup_folder = os.path.join(dated_backup_root, basename)
    makedirs(backup_folder)
    
    basename2exclude_path = lambda name: exclude_onefile_fmt.format(#name)
        os.path.join(basename, name))
    

    if 1:
        others_outname = 'program_source(exclude C++ py3 renpy svn).7z'
        others_outname = os.path.join(backup_folder, others_outname)
        others_excludes = 'c++ python3_src renpy svn_working_copy_parent'.split()
        others_argsex = list(map(basename2exclude_path, others_excludes))

        args = exe7z_args + others_argsex + [others_outname, program_source_path]
        #print(' '.join(args))
        check_call(args)

    cpp_basename = 'c++'
    py3_basename = 'python3_src'
    for basename in [cpp_basename, py3_basename]:
        inname = os.path.join(program_source_path, basename)
        outname = os.path.join(backup_folder, basename+'.7z')
        args = exe7z_args + [outname, inname]
        check_call(args)
    return

#

def pack_program_config(date, exe7z_args, program_config_path, dated_backup_root):
    basename = os.path.basename(program_config_path)
    backup_folder = dated_backup_root
    makedirs(backup_folder)
    outname = os.path.join(backup_folder, basename+'.7z')

    # auto_backup.py to program_config_path
    auto_backup(program_config_path)

    # pack all [date]xxx file
    includes1 = r'-ir!{}/[{}]*'.format(program_config_path, date)
    includes2 = r'-ir!{}/*.txt'.format(program_config_path, date)
    args = exe7z_args + [outname, includes1, includes2]
    check_call(args)
    return

#



def pack_my_record_txt(date, exe7z_args, my_record_txt_path, dated_backup_root):
    basename = os.path.basename(my_record_txt_path)
    backup_folder = dated_backup_root
    makedirs(backup_folder)
    outname = os.path.join(backup_folder, basename+'.7z')
    inname = my_record_txt_path
    args = exe7z_args + [outname, inname]
    check_call(args)
    return

if __name__ == '__main__':
    print('backup to ->', dated_backup_root)
    for path in [program_source_path, program_config_path, my_record_txt_path]:
        print('\t<-', path)
    input()
    pack_program_source(date, exe7z_args, program_source_path, dated_backup_root)
    pack_program_config(date, exe7z_args, program_config_path, dated_backup_root)
    pack_my_record_txt(date, exe7z_args, my_record_txt_path, dated_backup_root)
#print(date)

    
