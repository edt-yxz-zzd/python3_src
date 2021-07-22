
//floor_sqrt__main.cpp


#include <iostream>
#include "floor_sqrt.hpp"
#include "main4string.hpp"


/*

cd ../../python3_src/script/cpp/try_metaprogramming/
clang ./main.cpp -c
clang ./floor_sqrt__main.cpp -c
clang ./main.o ./floor_sqrt__main.o -lstdc++ -o ~/1tmp/exec/floor_sqrt.exe
~/1tmp/exec/floor_sqrt.exe
~/1tmp/exec/floor_sqrt.exe 0 1 2 3 4 5 6 7 8 9 10
/data/data/com.termux/files/home/1tmp/exec/floor_sqrt.exe
    | 0
    | 1
    | 2
    | 3
    | 4
    | 5
    | 6
    | 7
    | 8
    | 9
    | 10
    | 0 -> floor_sqrt(0) ==0
    | 1 -> floor_sqrt(1) ==1
    | 2 -> floor_sqrt(2) ==1
    | 3 -> floor_sqrt(3) ==1
    | 4 -> floor_sqrt(4) ==2
    | 5 -> floor_sqrt(5) ==2
    | 6 -> floor_sqrt(6) ==2
    | 7 -> floor_sqrt(7) ==2
    | 8 -> floor_sqrt(8) ==2
    | 9 -> floor_sqrt(9) ==3
    | 10 -> floor_sqrt(10) ==3


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



//constexpr auto err = floor_sqrt(-1);
//      assertE fire at compile-time!!
//
int main4string(const std::string& program_name, const std::vector<std::string>& args){
  using nn_ns::metaprogramming::floor_sqrt;
  using nn_ns::metaprogramming::AssertError;
  using namespace std;
  cout << program_name << endl;
  for (auto& arg: args){
    cout << "    | " << arg << endl;
  }
  /////



  //int a[floor_sqrt(-1)];
  //      why not assertE fire at compile-time??
  //

  bool err {};
  try{
    floor_sqrt(-1);
    //    fire at runtime
  }catch (AssertError const&){
    err = true;
  }if (err){}
  else{
    throw "logic-err";
  }

  size_t sz {};
  constexpr size_t radix = 10;
  for (auto& arg: args){
    auto u = stoull(arg, &sz, 10);
    cout
      << "    | " << arg
      << " -> floor_sqrt(" << u << ")"
      << " ==" << floor_sqrt(u)
      << endl;
  }
  return 0;
}
