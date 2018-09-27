@echo off


goto start
!!!!!!!!!!!donot edit this generated file!!!!!!!!!!
used to generate ./set_path.bat by generate_set_path.py

encoding=gb18030
template variables:
    tpl_var_NOTE
    tpl_var_bats_path
        tpl_var_bats_path == tpl_var_bats_path.replace('/', '\\')
    tpl_var_bats_path_double_backslash
        tpl_var_bats_path_double_backslash == tpl_var_bats_path.replace('\\', '\\'*2)




REM ##############################################################################
REM #CMD环境恢复中文:
chcp 936 # gbk
chcp 65001 # Windows only: Windows UTF-8 (CP_UTF8) ##############################################################################
chcp 54936 # gb18030
https://www.ibm.com/support/knowledgecenter/en/SSKM8N_7.0.0/com.ibm.etools.mft.doc/ac00408_.htm

REM ######################################################################
# 右键菜单
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into]

[HKEY_CLASSES_ROOT\Folder\shell\MS-DOS into\command]
@="c:\\windows\\System32\\cmd.exe /k @cd %1 & @E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat\\set_path\\set_path.bat"


[HKEY_CLASSES_ROOT\*\shell\MS-DOS]

[HKEY_CLASSES_ROOT\*\shell\MS-DOS\command]
@="c:\\windows\\System32\\cmd.exe /k @E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat\\set_path\\set_path.bat"

REM ##############################################################################


c:\python33;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Microsoft Windows Performance Toolkit\


:start

set bats_path=E:\my_data\program_source\github\edt-yxz-zzd\python3_src\windows_bat
set set_bat_path=%bats_path%\set_path
set 7z=py -m nn_ns.fileformat.zip_by_7z


rem choose set_msvc, set_gcc or set_clang
call %set_bat_path%\set_msvc
call %set_bat_path%\set_gcc
call %set_bat_path%\set_clang
rem call %set_bat_path%\set_haskell2012
=======
call %set_bat_path%\set_plain_tex
call %set_bat_path%\set_swig
call %set_bat_path%\set_python
rem set_boost should be after set_python
call %set_bat_path%\set_boost
call %set_bat_path%\set_mysql
call %set_bat_path%\set_java
call %set_bat_path%\set_svn
rem call %set_bat_path%\set_perl
call %set_bat_path%\set_mathematica
call %set_bat_path%\set_qt_qmake
call %set_bat_path%\set_git
call %set_bat_path%\set_haskell8

rem set path=%path%;D:\software\programming\gcc\tool\UnxUtils\usr\local\wbin
rem to override C:\Windows\System32\find.exe
set usrbin_path=D:\software\programming\gcc\tool\UnxUtils\usr\local\wbin
set path=%usrbin_path%;%path%;%usrbin_path%\pkg-config
set path=%path%;%set_bat_path%\cmdline_tool_link
set path=%path%;%bats_path%
set path=%path%;D:\software\programming\develop tools\cmake\cmake-3.7.2-win64-x64\bin
set path=%path%;D:\software\cmdline_tool_link

goto end

rem set path=%path%;D:\software\programming\gcc\tool\moreLinuxCmd
rem 
rem set path=%path%;D:\software\programming\gcc\tool\boost_build\bin
rem set path=%path%;C:\Program Files\gs\gs9.06\bin
rem 

REM pause


:end

@echo on

