
NOTE:
    NOTE: %0 neednot ""
    %0
        - user input name
        - "xxx yyy.bat"
    "%~f0"
        - absname
        - "C:\d d\xxx yyy.bat"
    "%~dp0"
        - dirname
        - "C:\d d\"

    CALL %0\..\SecondBatch.cmd

NOTE:
    set "xxx_home=xxx xxx\yy yy"
        # not: set xxx_home="xxx xxx\yy yy"
    set "path=%path%;%xxx_home%\bin"
        # not: set path=%path%;%xxx_home%\bin
        why?
            to avoid special characters like "&>" in %path% or %xxx_home%

    call "%xxx_home%\bin\xxx"
        # not: call %xxx_home%\bin\xxx
    set xxx_cmd="%xxx_home%\bin\xxx"
        not: "set xxx_cmd=%xxx_home%\bin\xxx"
        why?
            set xxx_cmd="%xxx_home%\bin\xxx" -args
    call %xxx_cmd%

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




