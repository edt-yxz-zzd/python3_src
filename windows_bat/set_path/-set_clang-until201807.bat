
goto start

     head / lib     where
c    stdio.h        ./include
     libm.a         ./lib
c++  string         ./lib/gcc/$mn/$ver/include/c++
     libstdc++.a    ./lib/gcc/$mn/$ver
3rd  iconv.h        ./include
     libiconv.a     ./lib

     head / lib
c    stdio.h        ./$mn/include
     libm.a         ./$mn/lib     and  ./$mn/lib32
c++  string         ./$mn/include/c++
     libstdc++.a    ./lib/gcc/$mn/$ver and ..../32
3rd  iconv.h        ./$mn/include
     libiconv.a     ./$mn/lib     and  ./$mn/lib32


     head / lib
c    stdio.h        ./$mn/include
     libm.a         ./$mn/lib
c++  string         ./lib/gcc/$mn/$ver/include/c++
     libstdc++.a    ./lib/gcc/$mn/$ver
3rd  iconv.h        ./$mn/include
     libiconv.a     ./$mn/lib

so, c and 3rd are the same, ./[$mn/](lib|include)

c++.lib == ./lib/gcc/$mn/$ver
c++.include == ./lib/gcc/$mn/$ver/include/c++ or ./$mn/include/c++
<bits/c++config.h> in c++.include/$mn

:start


:setclang
rem ==========================clang set============================
rem C:\mingw64\x86_64-4.9.0-release-win32-sjlj-rt_v3-rev2 x86_64-w64-mingw32 4.9.0
rem C:\mingw64\x64-4.8.1-posix-seh-rev5\mingw64           x86_64-w64-mingw32 4.8.1
rem D:\software\programming\gcc\mingw32\bin               mingw32            4.7.2
set gcc64paths=C:\mingw64\x64-4.8.1-posix-seh-rev5\mingw64\bin;C:\mingw64\x86_64-4.9.0-release-win32-sjlj-rt_v3-rev2\bin
set gcchome=C:\mingw64\x86_64-4.9.0-release-win32-sjlj-rt_v3-rev2
set middlename=x86_64-w64-mingw32
set mingwversion=4.9.0

rem          C:\mingw64\MSYS-20111123\msys
rem          D:\software\programming\gcc\mingw32\msys\1.0
set msyshome=C:\mingw64\MSYS-20111123\msys

set clanghome=C:\mingw64\x86_64-w64-mingw32-clang-3.2-release-win64_rubenvb

set path=%msyshome%;%path%
set path=%msyshome%\bin;%path%
set path=%clanghome%\bin;%gcc64paths%;%path%
rem set path=%gcchome%\bin;%path%



set mingwc1include=%gcchome%\%middlename%\include
set mingwclib=%gcchome%\%middlename%\lib
set mingwc2include=%gcchome%\include
set mingwc2lib=%gcchome%\lib
set mingwcxxlib=%gcchome%\lib\gcc\%middlename%\%mingwversion%
set mingwcxx1include=%gcchome%\lib\gcc\%middlename%\%mingwversion%\include\c++
set mingwcxx2include=%gcchome%\%middlename%\include\c++
set mingwcxx1_include=%mingwcxx1include%\%middlename%
set mingwcxx2_include=%mingwcxx2include%\%middlename%

set boost_build_inc_lnk=include=%mingwc1include% include=%mingwc2include% include=%mingwcxx1include% include=%mingwcxx2include% include=%mingwcxx1_include% include=%mingwcxx2_include% linkflags=-L%mingwc1lib% linkflags=-L%mingwc2lib% linkflags=-L%mingwcxxlib%

set clang_build_inc_lnk=-I%mingwc1include% -I%mingwc2include% -I%mingwcxx1include% -I%mingwcxx2include% -I%mingwcxx1_include% -I%mingwcxx2_include% -L%mingwc1lib% -L%mingwc2lib% -L%mingwcxxlib%
echo clang %%clang_build_inc_lnk%%

