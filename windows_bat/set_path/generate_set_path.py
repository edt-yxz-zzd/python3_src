
'''
genearate_set_path_bat
    genearate set_path.bat and other <name>.bat if <name>.bat.tpl exists
update_windows_registry
    * register_right_click_menu__open_cmd_and_set_path
        right-click on file or directory will show a new menuitem named "MS-DOS" or "MS-DOS into"
    * register_right_click_menu__copy_path
        right-click on file or directory will show a new menuitem named "copy_path"



run_as_main = '__run_as_main__'
if __name__ in ('__main__', run_as_main) or __name__.endswith('.' + run_as_main):
    main()
'''

from pathlib import Path
import winreg
import sys, os
from seed.windows.winreg_helper import reg_update_from_value_table
import nn_ns.app
'''
import os.path
from seed.io.incompatible_universal_read_write_txt import \
    incompatible_universal_read_txt
'''



class Global:
    #"tpl_var_bats_path_double_backslash should not contains spaces"
    encoding = 'gb18030'
    set_path_bat_dirname = 'set_path'
    set_path_bat_basename = 'set_path.bat'
    set_path_bat_tpl_basename = f'{set_path_bat_basename}.tpl'
    save_input_path_to_clipboard_bat_basename = 'save_input_path_to_clipboard.bat'

    into_folder_command_tpl = fr"c:\\windows\\System32\\cmd.exe /k @cd %1 & @{{tpl_var_bats_path_double_backslash}}\\{set_path_bat_dirname}\\{set_path_bat_basename}"
    same_folder_command_tpl = fr"c:\\windows\\System32\\cmd.exe /k @{{tpl_var_bats_path_double_backslash}}\\{set_path_bat_dirname}\\{set_path_bat_basename}"
    copy_path_command_tpl = fr'c:\\windows\\System32\\cmd.exe /c @{{tpl_var_bats_path_double_backslash}}\\{save_input_path_to_clipboard_bat_basename} "%1"'

    reg_path_command_tpl_pairs = [
        (r'HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into\command'
            , into_folder_command_tpl)
        #,(r'HKEY_CLASSES_ROOT\Folder\shell\MS-DOS\command'
        #    , same_folder_command_tpl)
        #   fail for driver
        ,(r'HKEY_CLASSES_ROOT\*\shell\MS-DOS\command'
            , same_folder_command_tpl)

        ,(r'HKEY_CLASSES_ROOT\Folder\shell\copy_path\command'
            , copy_path_command_tpl)
        ,(r'HKEY_CLASSES_ROOT\*\shell\copy_path\command'
            , copy_path_command_tpl)
        ]

    # use value_table instead
    #   reg_update_from_value_table
    old_reg_file = r'''
Windows Registry Editor Version 5.00

; update_windows_registry

; ====================================================
; register_right_click_menu__open_cmd_and_set_path

[HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into]

[HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into\command]
@="c:\\windows\\System32\\cmd.exe /k @cd %1 & @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"


[HKEY_CLASSES_ROOT\*\shell\MS-DOS]

[HKEY_CLASSES_ROOT\*\shell\MS-DOS\command]
@="c:\\windows\\System32\\cmd.exe /k @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"





; ====================================================
; register_right_click_menu__copy_path

[HKEY_CLASSES_ROOT\Folder\shell\copy_path]

[HKEY_CLASSES_ROOT\Folder\shell\copy_path\command]
; bug: @="c:\\windows\\System32\\cmd.exe /c @E:\\my_data\\program_source\\windows_bat\\save_input_path_to_clipboard.bat %1"
; bug: @="c:\\windows\\System32\\cmd.exe /c @E:\\my_data\\program_source\\windows_bat\\save_input_path_to_clipboard.bat %*"
; bug: @="c:\\windows\\System32\\cmd.exe /c @E:\\my_data\\program_source\\windows_bat\\save_input_path_to_clipboard.bat \"%*\""
@="c:\\windows\\System32\\cmd.exe /c @E:\\my_data\\program_source\\windows_bat\\save_input_path_to_clipboard.bat \"%1\""
    ; but OK:
    ;   [HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into\command]
    ;   @="c:\\windows\\System32\\cmd.exe /k @cd %1 & @{tpl_var_bats_path_double_backslash}\\set_path\\set_path.bat"


[HKEY_CLASSES_ROOT\*\shell\copy_path]
[HKEY_CLASSES_ROOT\*\shell\copy_path\command]
@="c:\\windows\\System32\\cmd.exe /c @E:\\my_data\\program_source\\windows_bat\\save_input_path_to_clipboard.bat \"%1\""
'''

def mk_windows_bat_folder()->Path:
    this_fname = Path(__file__).resolve()
    this_folder = this_fname.parent
    if this_folder.name != Global.set_path_bat_dirname:
        raise Exception(f'this folder name != {Global.set_path_bat_dirname}')
    windows_bat_folder = this_folder.parent
    return windows_bat_folder
def mk_nn_ns_folder()->Path:
    nn_ns_init_file = Path(nn_ns.__file__).resolve()
    assert nn_ns_init_file.is_file()
    assert nn_ns_init_file.name == '__init__.py'
    nn_ns_folder = nn_ns_init_file.parent
    return nn_ns_folder

def mk_tpl_vars_ex(windows_bat_folder:Path):
    nn_ns_folder = mk_nn_ns_folder()
    nn_ns_app_scripts_path = nn_ns_folder/'app'/'scripts'
    tpl_var_nn_ns_app_scripts_path = str(nn_ns_app_scripts_path)
    tpl_vars = mk_tpl_vars(windows_bat_folder)
    tpl_vars_ex = dict(tpl_var_nn_ns_app_scripts_path
                            =tpl_var_nn_ns_app_scripts_path
                        , **tpl_vars
                        )
    return tpl_vars_ex

def mk_tpl_vars(windows_bat_folder:Path):
    tpl_var_sys = sys
    tpl_var_NOTE = 'donot edit this generated file'

    tpl_var_bats_path = windows_bat_folder.resolve()
    tpl_var_bats_path = str(tpl_var_bats_path).replace('/', '\\')

    tpl_var_bats_path_double_backslash = \
        tpl_var_bats_path.replace('\\', '\\'*2)

    del windows_bat_folder
    #return dict(locals())
    return dict(
        tpl_var_sys=tpl_var_sys
        , tpl_var_NOTE=tpl_var_NOTE
        , tpl_var_bats_path=tpl_var_bats_path
        , tpl_var_bats_path_double_backslash
            =tpl_var_bats_path_double_backslash
        )


def update_windows_registry(windows_bat_folder):
    tpl_vars = mk_tpl_vars(windows_bat_folder)
    tpl_var_bats_path_double_backslash = tpl_vars[
        'tpl_var_bats_path_double_backslash']
    if ' ' in tpl_var_bats_path_double_backslash: raise NotImplementedError

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
    tpl_vars_ex = mk_tpl_vars_ex(windows_bat_folder)

    set_path_bat_folder = Path(windows_bat_folder, Global.set_path_bat_dirname)

    tpl_basenames = {Global.set_path_bat_tpl_basename}
    for basename in os.listdir(set_path_bat_folder):
        if basename.endswith('.bat.tpl'):
            tpl_basenames.add(basename)
    for tpl_basename in tpl_basenames:
        tpl_fname = Path(set_path_bat_folder, tpl_basename)
        bat_tpl_content = tpl_fname.read_text(encoding=Global.encoding)
        bat_content = bat_tpl_content.format(**tpl_vars_ex)

        #bug: bat_fname = Path(set_path_bat_folder, tpl_basename)
        #   == tpl_fname
        bat_fname = tpl_fname.with_suffix('')
        assert bat_fname.suffix == '.bat'
        bat_fname.write_text(bat_content, encoding=Global.encoding)

def main():
    windows_bat_folder = mk_windows_bat_folder()

    update_windows_registry(windows_bat_folder)
    genearate_set_path_bat(windows_bat_folder)


run_as_main = '__run_as_main__'
if __name__ in ('__main__', run_as_main) or __name__.endswith('.' + run_as_main):
    main()



