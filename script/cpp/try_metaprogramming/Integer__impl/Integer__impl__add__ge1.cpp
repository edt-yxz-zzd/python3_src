
//Integer__impl__add__ge1.cpp
#include "Integer.hpp"

namespace nn_ns{namespace metaprogramming{ namespace Integer{

  /////

  template<bool acc, bool... lhs_bits, bool... rhs_bits>
    struct Integer__full_add_<bool
      , acc
      ,Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >;


  template<bool... lhs_bits, bool... rhs_bits>
    struct Integer__add_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >;



  /////

  template<bool... rhs_bits>
    struct Integer__add_<
      Integer__ge1__little_endian_bools__implicitly_MSB<>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >
    {
      using type = Inc_Integer<
          Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
          >;
    };


  template<bool llsb, bool... lhs_bits>
    struct Integer__add_<
      Integer__ge1__little_endian_bools__implicitly_MSB<llsb, lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<>
      >
    {
      using type = Inc_Integer<
            Integer__ge1__little_endian_bools__implicitly_MSB<llsb, lhs_bits...>
            >;
    };

  template<bool llsb, bool rlsb, bool... lhs_bits, bool... rhs_bits>
    struct Integer__add_<
      Integer__ge1__little_endian_bools__implicitly_MSB<llsb, lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rlsb, rhs_bits...>
      >
    {
      //lazy branch ==>> Get_the_type_member+Integer__add_ but not Add_Integer
      using type = Concatenation_v_vs_4_Integer__ge1__little_endian_bools__implicitly_MSB<
          llsb^rlsb
          ,Full_Add_Integer<bool
            //bug:,(llsb==true==rlsb)
            ,(llsb && rlsb)
            ,Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
            ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
            >
          >;
    };





  template<bool acc, bool... lhs_bits, bool... rhs_bits>
    struct Integer__full_add_<bool
      , acc
      ,Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      ,Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
      >
    {
      using type = Add_Integer<
          Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
          ,Get_the_type_member<If_Then_Else<acc
            ,Integer__inc_<
                Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
                >
            ,Echo_<
                Integer__ge1__little_endian_bools__implicitly_MSB<rhs_bits...>
                >
            > >
          >;
    };







}}}






