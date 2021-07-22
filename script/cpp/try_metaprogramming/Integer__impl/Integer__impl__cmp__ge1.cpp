
//Integer__impl__cmp__ge1.cpp
#include "Integer.hpp"



namespace nn_ns{namespace metaprogramming{ namespace Integer{

  /////
  template<bool... lhs_bits, bool... rhs_bits>
    struct Integer__cmp_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >;





}}}







