
//main.cpp

/*

cd ../../python3_src/script/cpp/try_metaprogramming/
clang ./main.cpp -c
clang ./floor_sqrt.cpp -c
clang ./main.o ./floor_sqrt.o -lstdc++ -o ~/1tmp/exec/floor_sqrt.exe
~/1tmp/exec/floor_sqrt.exe


====old
e ../../python3_src/script/cpp/try_metaprogramming/floor_sqrt.cpp
#bug:output ./floor_sqrt.o: clang ../../python3_src/script/cpp/try_metaprogramming/floor_sqrt.cpp -c
ls ../../python3_src/script/cpp/try_metaprogramming/
cd ../../python3_src/script/cpp/try_metaprogramming/
clang ./floor_sqrt.cpp -c
clang ./floor_sqrt.o -lstdc++
chmod +x ./a.out
chmod: changing permissions of './a.out': Operation not permitted

cp -t ~/1tmp/exec/ ./a.out
chmod +x ~/1tmp/exec/a.out
clang ./floor_sqrt.o -lstdc++ -o ~/1tmp/exec/floor_sqrt.exe
~/1tmp/exec/floor_sqrt.exe




*/



#include <cassert>
#include "main4string.hpp"
namespace {
int _main(const int argc, char const *const *const argv){
  assert(argc >= 1);
  for (int i=0; i < argc; ++i){
    assert(argv[i] != nullptr);
  }
  assert(argv[argc] == nullptr);

  if (! (argc >= 1)){
    throw "(! (argc >= 1))";
  }
  for (int i=0; i < argc; ++i){
    if (argv[i] == nullptr){
      throw "nullptr <- argv[0:argc]";
    }
  }
  if (! (argv[argc] == nullptr)){
    throw "(! (argv[argc] == nullptr))";
  }

  const std::string program_name {argv[0]};
  std::vector<std::string> args {argv+1, argv+argc};
  //for (int i=1; i < argc; ++i){ args.emplace_back(argv[i]); }
  try{
    return main4string(program_name, args);
  }catch (...){
    //
    throw;
  }

}//_main
}//namespace
int main(const int argc, char const *const *const argv){
  try{
    return _main(argc, argv);
  }catch (...){
    //clean-up all objs
    //  to avoid "terminating with uncaught exception"
    throw;
  }
}


