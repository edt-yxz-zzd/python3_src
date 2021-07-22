
//Integer__main.cpp


#include "Integer.hpp"
#include "main4string.hpp"
#include <iostream>
#include <type_traits>


/*

cd ../../python3_src/script/cpp/try_metaprogramming/
clang ./main.cpp -c
clang ./Integer__main.cpp -c
clang ./main.o ./Integer__main.o -lstdc++ -o ~/1tmp/exec/Integer.exe
~/1tmp/exec/Integer.exe

*/

template<bool... bits>
  using PInt = nn_ns::metaprogramming::Integer::Integer__ge1__little_endian_bools__implicitly_MSB<bits...>;

int main4string(const std::string& program_name, const std::vector<std::string>& args){
  using namespace nn_ns::metaprogramming::Integer;
  using namespace std;
  cout << program_name << endl;
  for (auto& arg: args){
    cout << "    | " << arg << endl;
  }
  /////


  static_assert(std::is_same<PInt<>, PInt<> >(), "");
  static_assert(std::is_same<PInt<0>, Inc_Integer<PInt<> > >(), "");
  static_assert(std::is_same<PInt<1>, Inc_Integer<PInt<0> > >(), "");
  static_assert(std::is_same<PInt<0,0>, Inc_Integer<PInt<1> > >(), "");
  static_assert(std::is_same<PInt<1,0>, Inc_Integer<PInt<0,0> > >(), "");
  static_assert(std::is_same<PInt<0,1>, Inc_Integer<PInt<1,0> > >(), "");
  static_assert(std::is_same<PInt<1,1>, Inc_Integer<PInt<0,1> > >(), "");
  static_assert(std::is_same<PInt<0,0,0>, Inc_Integer<PInt<1,1> > >(), "");


  static_assert(std::is_same<PInt<0>, Add_Integer<PInt<>, PInt<> > >(), "");

  static_assert(std::is_same<PInt<1>, Add_Integer<PInt<0>, PInt<> > >(), "");
  static_assert(std::is_same<PInt<1>, Add_Integer<PInt<>, PInt<0> > >(), "");
  static_assert(std::is_same<PInt<0,0>, Add_Integer<PInt<1>, PInt<> > >(), "");
  static_assert(std::is_same<PInt<0,0>, Add_Integer<PInt<>, PInt<1> > >(), "");

  static_assert(std::is_same<PInt<0,0>, Add_Integer<PInt<0>, PInt<0> > >(), "");
  static_assert(std::is_same<PInt<1,0>, Add_Integer<PInt<1>, PInt<0> > >(), "");
  static_assert(std::is_same<PInt<1,0>, Add_Integer<PInt<0>, PInt<1> > >(), "");
  static_assert(std::is_same<PInt<0,1>, Add_Integer<PInt<1>, PInt<1> > >(), "");


  static_assert(std::is_same<PInt<1,1>, Add_Integer<PInt<1>, PInt<0,0> > >(), "");
  static_assert(std::is_same<PInt<1,0,1, 1,0,1, 0,0,0,0,0,0>, Add_Integer<PInt<1,0,1, 0,1,1, 1,0,1,0>, PInt<0,0,0, 1,1,1, 0,1,0,1,0> > >(), "");

  return 0;
}



