
//Integer__impl__inc__ge1.cpp
#include "Integer.hpp"



namespace nn_ns{namespace metaprogramming{ namespace Integer{

  /////
  template<bool... lhs_bits>
    struct Integer__inc_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      >;



  template<>
    struct Integer__inc_<
      Integer__ge1__little_endian_bools__implicitly_MSB<>
      >
    {
      //[] ~~ 0b1
      //[0] ~~ 0b10
      using type = Integer__ge1__little_endian_bools__implicitly_MSB<0>;
    };




  template<bool... high_bits>
    struct Integer__inc_<
      Integer__ge1__little_endian_bools__implicitly_MSB<0, high_bits...>
      >
    {
      //0:high_bits ~~ 0b...0
      //1:high_bits ~~ 0b...1
      using type = Integer__ge1__little_endian_bools__implicitly_MSB<1, high_bits...>;
    };


  template<bool... high_bits>
    struct Integer__inc_<
      Integer__ge1__little_endian_bools__implicitly_MSB<1, high_bits...>
      >
    {
      //1:high_bits ~~ 0b...1
      //0:inc high_bits ~~ (inc 0b...)0
      using type = Concatenation_v_vs_4_Integer__ge1__little_endian_bools__implicitly_MSB<
          0
          ,Inc_Integer<
              Integer__ge1__little_endian_bools__implicitly_MSB<high_bits...>
              >
          >;
    };






}}}







