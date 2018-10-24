rem send to desktop shortcut
goto start


rem cmd /k @.\set_path\set_path.bat
call .\set_path\set_path.bat
dir . /B
cmd
:start
cmd /k "call .\set_path\set_path.bat&dir . /B"
