
//Integer.hpp

/*

e ../../python3_src/script/cpp/try_metaprogramming/Integer.hpp
cd ../../python3_src/script/cpp/try_metaprogramming/
clang ./Integer.hpp

*/
#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__Integer_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__Integer_hpp
#include "Integer.hpp"




#include "Sign.hpp"
  //Sign
#include "ValueList.hpp"
  //ValueList<V>::List<V...>
  //Mk_ValueList<V, args...>
  //Concatenation_vs_vs_
  //Concatenation_vs_vs
  //Concatenation_v_vs
  //From_ValueList_
  //From_ValueList
  //To_ValueList_
  //To_ValueList



#include "nn_ns__type_traits.hpp"
  //Get_the_type_member
  //get_the_value_member
  //If_Then_Else
  //Echo_ Echo
  //

namespace nn_ns{namespace metaprogramming{ namespace Integer{
  //using nn_ns::metaprogramming::Sign;
  //using namespace nn_ns::metaprogramming::ValueList::PackedValueList;
  //using namespace PackedValueList = namespace nn_ns::metaprogramming::ValueList::PackedValueList;
  //using PackedValueList = nn_ns::metaprogramming::ValueList::namespace PackedValueList;
  namespace PackedValueList = nn_ns::metaprogramming::ValueList::PackedValueList;


  template <typename OutputIntegerSpec, typename InputIntegerValue>
    struct IntegerConvertor;
      //::type = OutputIntegerValue
      //builtin Integer save at: Just<int, 9>
  template <typename Integer, typename NonZeroInteger>
    struct Fraction; //Fraction, Rational, Ratio
      //non-std: sign, zero, gcd
  template <typename Integer, typename... Integer__ge1>
    struct FiniteContinuedFraction__big_endian__implicitly_LSB;
      //std!
      //implicitly append 1
      //        <==> n+(0,1]
      //        <==> my[n;] -> out[n;1]===n+1 #may change sign!!
      //        <==> my[n;...,x] -> out[n;...,x,1]===out[n;...,x+1] #x+1>=2
  template <typename RealNumber>
    struct Get_sign;
      //value :: Sign
  template <typename RealNumber>
    struct Get_abs;
      //value :: Sign


  /*
    */

  /////////////////////////////////////
  /////////////////////////////////////
  /////////////////////////////////////
  /////////////////////////////////////

  /////////////////////////////////////
  /////////////////////////////////////
  /////////////////////////////////////
  /////////////////////////////////////



  template<bool... little_endian_bools__implicitly_MSB>
    struct Integer__ge1__little_endian_bools__implicitly_MSB;

  template<bool... may_signed__little_endian_bools__implicitly_MSB>
    struct Integer__may_signed__little_endian_bools__implicitly_MSB;

  template<>
    struct Integer__may_signed__little_endian_bools__implicitly_MSB<>{
      // this class repr 0
      //    no sign, no payload bits
      static constexpr Sign sign = Sign::EQ;
    };
  template<bool is_neg, bool... little_endian_bools__implicitly_MSB>
    struct Integer__may_signed__little_endian_bools__implicitly_MSB<is_neg, little_endian_bools__implicitly_MSB...>{
      static constexpr Sign sign = is_neg? Sign::LT : Sign::GT;
    };

  template<bool lsb, typename high_bits>
    using Concatenation_v_vs_4_Integer__ge1__little_endian_bools__implicitly_MSB
      = PackedValueList::From_ValueList<bool
        , Integer__ge1__little_endian_bools__implicitly_MSB
        , PackedValueList::Concatenation_v_vs<bool
          , lsb
          , high_bits
          >
        >;


  /////////////////////////////////////
  /////////////////////////////////////
  /////////////////////////////////////
  /////////////////////////////////////
  //


  template<typename lhs>
    struct Integer__inc_;
  template<typename lhs>
    using Inc_Integer = Get_the_type_member<Integer__inc_<lhs> >;


  template<typename Acc, Acc acc, typename lhs, typename rhs>
    struct Integer__full_add_;
  template<typename Acc, Acc acc, typename lhs, typename rhs>
    using Full_Add_Integer = Get_the_type_member<Integer__full_add_<Acc, acc, lhs, rhs> >;


  template<typename lhs, typename rhs>
    struct Integer__add_;
  template<typename lhs, typename rhs>
    using Add_Integer = Get_the_type_member<Integer__add_<lhs, rhs> >;


  template<typename lhs, typename rhs>
    struct Integer__cmp_;
  template<typename lhs, typename rhs>
    inline constexpr Sign cmp_Integer(){
      return get_the_value_member<Integer__cmp_<lhs, rhs> >();
    }

  template<typename lhs, typename rhs>
    struct Integer__subtract_;
  template<typename lhs, typename rhs>
    using Subtract_Integer = Get_the_type_member<Integer__subtract_<lhs, rhs> >;






  /////
  template<bool... lhs_bits>
    struct Integer__inc_<
      Integer__ge1__little_endian_bools__implicitly_MSB<lhs_bits...>
      >;


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

#include "Integer__impl/Integer__impl.cpp"
#endif // HEADER_GUARD_4_nn_ns__metaprogramming__Integer_hpp



