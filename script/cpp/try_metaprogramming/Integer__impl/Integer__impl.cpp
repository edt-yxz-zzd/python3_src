
//Integer__impl.cpp
#include "Integer.hpp"
#include "Integer__impl__inc__ge1.cpp"
#include "Integer__impl__add__ge1.cpp"
#include "Integer__impl__cmp__ge1.cpp"
#include "Integer__impl__subtract__ge1.cpp"



namespace nn_ns{namespace metaprogramming{ namespace Integer{

  /////
  template<bool... lhs_bits>
    struct Integer__inc_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      >;



  template<bool... lhs_bits, bool... rhs_bits>
    struct Integer__add_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >;



  template<bool... lhs_bits, bool... rhs_bits>
    struct Integer__cmp_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >;



  template<bool... lhs_bits, bool... rhs_bits>
    struct Integer__subtract_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >;





}}}







