:setboost
goto start
tpl_variables:
    tpl_var_sys
:start

rem setboost should not be before setpython since using py_XXX in "cl_py" definition

set "boost=D:\software\programming\library\boost\boost_1_55_0"
::: "boost_build_stagedir=%boost%\binary_lib\x86_64_py33"
set "boost_build_stagedir=%boost%\binary_lib\x86_64_py36"
set "boost_lib=%boost_build_stagedir%\lib"
set "path=%boost%\tools\build\v2;%path%"


set "boost_build_options=--build-dir=D:\temp_output\build_dir --stagedir=%boost_build_stagedir% address-model=64  architecture=x86 target-os=windows --build-type=complete --layout=versioned threading=multi variant=release runtime-link=shared"
set "bjj=b2 toolset=msvc %boost_build_options% %boost_build_inc_lnk%"

rem b2 --with-random toolset=msvc %boost_build_options% %boost_build_inc_lnk%
echo b2 --with-random toolset=msvc %%boost_build_options%% %%boost_build_inc_lnk%%
echo %%bjj%% --with-random

echo gcc main.cpp -I%%boost%% -L%%boost_lib%% -lboost_random-xxxxx-mt-1_55-x86_64

set "cl_py=/Fo /LD /MD /EHsc /I%py_include% /I%boost% /link /LIBPATH:%boost_lib% /LIBPATH:%py_lib%"
rem cl /Fo /LD /MD /EHsc hello.cpp /I%py_include% /I%boost% /link /LIBPATH:%boost_lib% /LIBPATH:%py_lib%
echo cl /Fo /LD /MD /EHsc hello.cpp /I%%py_include%% /I%%boost%% /link /LIBPATH:%%boost_lib%% /LIBPATH:%%py_lib%%
echo cl hello.cpp %%cl_py%%

