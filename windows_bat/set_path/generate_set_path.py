
'''
run_as_main = '__run_as_main__'
if __name__ in ('__main__', run_as_main) or __name__.endswith('.' + run_as_main):
    main()
'''

from pathlib import Path
import winreg
from seed.windows.winreg_helper import reg_update_from_value_table
'''
import os.path
from seed.io.incompatible_universal_read_write_txt import \
    incompatible_universal_read_txt
'''



class Global:
    encoding = 'gb18030'
    set_path_bat_dirname = 'set_path'
    set_path_bat_basename = 'set_path.bat'
    set_path_bat_tpl_basename = f'{set_path_bat_basename}.tpl'

    into_folder_command_tpl = r"c:\\windows\\System32\\cmd.exe /k @cd %1 & @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"
    same_folder_command_tpl = r"c:\\windows\\System32\\cmd.exe /k @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"
    reg_path_command_tpl_pairs = [
        (r'HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into\command'
            , into_folder_command_tpl)
        ,(r'HKEY_CLASSES_ROOT\*\shell\MS-DOS\command'
            , same_folder_command_tpl)
        ]

    # use value_table instead
    #   reg_update_from_value_table
    old_reg_file = r'''
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into]

[HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into\command]
@="c:\\windows\\System32\\cmd.exe /k @cd %1 & @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"


[HKEY_CLASSES_ROOT\*\shell\MS-DOS]

[HKEY_CLASSES_ROOT\*\shell\MS-DOS\command]
@="c:\\windows\\System32\\cmd.exe /k @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"
'''

def mk_windows_bat_folder():
    this_fname = Path(__file__).resolve()
    this_folder = this_fname.parent
    if this_folder.name != Global.set_path_bat_dirname:
        raise Exception(f'this folder name != {Global.set_path_bat_dirname}')
    windows_bat_folder = this_folder.parent
    return windows_bat_folder

def mk_tpl_vars(windows_bat_folder):
    tpl_var_bats_path = windows_bat_folder.resolve()
    tpl_var_bats_path = str(tpl_var_bats_path).replace('/', '\\')

    tpl_var_bats_path_double_backslash = \
        tpl_var_bats_path.replace('\\', '\\'*2)
    return tpl_var_bats_path, tpl_var_bats_path_double_backslash


def update_windows_registry(windows_bat_folder):
    (tpl_var_bats_path, tpl_var_bats_path_double_backslash
    ) = mk_tpl_vars(windows_bat_folder)
    del tpl_var_bats_path

    def mk_command(command_tpl):
        command = command_tpl.format(
            tpl_var_bats_path_double_backslash
                =tpl_var_bats_path_double_backslash
            )
        command = command.replace('\\'*2, '\\')
        return command

    for path, command_tpl in Global.reg_path_command_tpl_pairs:
        command = mk_command(command_tpl)
        value_table = {'': (winreg.REG_SZ, command)}
        reg_update_from_value_table(path, value_table)

def genearate_set_path_bat(windows_bat_folder):

    set_path_bat_folder = Path(windows_bat_folder, Global.set_path_bat_dirname)
    tpl_fname = Path(set_path_bat_folder, Global.set_path_bat_tpl_basename)
    set_path_bat_tpl = tpl_fname.read_text(encoding=Global.encoding)

    (tpl_var_bats_path, tpl_var_bats_path_double_backslash
    ) = mk_tpl_vars(windows_bat_folder)

    set_path_bat_content = set_path_bat_tpl.format(
        tpl_var_NOTE = 'donot edit this generated file'
        ,tpl_var_bats_path=tpl_var_bats_path
        ,tpl_var_bats_path_double_backslash=tpl_var_bats_path_double_backslash
        )

    set_path_bat_fname = Path(set_path_bat_folder, Global.set_path_bat_basename)
    set_path_bat_fname.write_text(set_path_bat_content, encoding=Global.encoding)

def main():
    windows_bat_folder = mk_windows_bat_folder()

    update_windows_registry(windows_bat_folder)
    genearate_set_path_bat(windows_bat_folder)


run_as_main = '__run_as_main__'
if __name__ in ('__main__', run_as_main) or __name__.endswith('.' + run_as_main):
    main()



