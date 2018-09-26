
goto start

:start


:setclang
rem ==========================clang set============================


set clanghome=D:\software\programming\LLVM\clang6\bin
set clang_libcxx_include=D:\software\programming\LLVM\clang-6.0.0\libcxx-6.0.0.src
set path=%clanghome%;%path%
echo clang++ -std=c++14 -I%clang_libcxx_include%

