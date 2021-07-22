
//Sign.hpp

#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__Sign_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__Sign_hpp
#include "Sign.hpp"
  //Sign
  //eq_0 gt_0 lt_0
  //


namespace nn_ns{namespace metaprogramming{


  enum class Sign { LT=-1, EQ=0, GT=+1};

  template<typename T>
  inline constexpr bool eq_0(){
    return T::sign == Sign::EQ;
  }
  template<typename T>
  inline constexpr bool lt_0(){
    return T::sign == Sign::LT;
  }
  template<typename T>
  inline constexpr bool gt_0(){
    return T::sign == Sign::GT;
  }




}}

#endif // HEADER_GUARD_4_nn_ns__metaprogramming__Sign_hpp

