
.. = <path/to/windows_bat>
. = ../set_path

edit
    # set_path.bat.tpl instead of set_path.bat
    <name>.bat if not exists <name>.bat.tpl else <name>.bat.tpl

execute
    generate_set_path.py
    update_cmd_reg_setting.py

    or if ../.. is the py_src_root:
        __setup__.py
            it will call the above two py script




