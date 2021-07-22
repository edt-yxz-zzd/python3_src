
//nn_ns__exceptions.hpp

#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__nn_ns__exceptions_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__nn_ns__exceptions_hpp
#include "nn_ns__exceptions.hpp"
  //AssertError
  //ValueError
  //assertE
  //assertF
  //


namespace nn_ns{namespace metaprogramming{


  struct AssertError{};
  struct ValueError{};

  template <typename T>
      inline constexpr T assertE(bool b, T x){
        return b? x:throw AssertError();
      }
  template <typename T, typename... Ts>
      inline constexpr T assertF(bool (*predicator)(T, Ts...), T x, Ts... args){
        return predicator(x, args...)? x:throw AssertError();
      }


}}

#endif // HEADER_GUARD_4_nn_ns__metaprogramming__nn_ns__exceptions_hpp

