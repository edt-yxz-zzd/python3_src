:setmsvc
set boost_build_inc_lnk=
set msvchome="C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin"
set path=%msvchome%;%path%
set _vc=%msvchome%\SetEnv.cmd /x64 /release
call %_vc%
rem echo %%_vc%% ###### for set msvc env

