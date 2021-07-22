
//nn_ns__type_traits.hpp

#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__nn_ns__type_traits_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__nn_ns__type_traits_hpp
#include "nn_ns__type_traits.hpp"
  //Get_the_type_member
  //get_the_value_member
  //If_Then_Else
  //Echo_ Echo
  //Enable_if
  //


/*

  lazy version:
    F_<...>::type
  strict version:
    F<...>

  // below T_, F_ using lazy version to avoid failure
  Get_the_type_member<
    If_Then_Else<b
      ,T_<...>
      ,F_<...>
      >
    >

*/



#include <type_traits>
  //conditional<b,T,F>::type
  //enable_if<b, T>::type
  //is_integral<X>()
  //is_unsigned<X>() #::value
  //is_nothrow_constructible<X,args>
  //is_same<X,Y> Is X the same type as Y?
  //is_base_of<X,Y> Is X a base of Y?
  //is_convertible<X,Y> Can an X be implicitly converted to a Y?
  //
  //common_type<X,Y>::type ??==>>?? decltype(b?X:Y)
  //



namespace nn_ns{namespace metaprogramming{


  template<typename T>
    using Get_the_type_member = typename T::type;
  template<typename T>
    inline constexpr auto get_the_value_member() -> decltype(T::value) {
      return T::value;
    }

  template<bool b, typename T, typename F>
    using If_Then_Else = Get_the_type_member<std::conditional<b, T,F> >;


  template<typename T>
    struct Echo_{
      using type = T;
    };
  template<typename T>
    using Echo = Get_the_type_member<Echo_<T> >;


  template<bool b, typename T>
    using Enable_if = Get_the_type_member<std::enable_if<b,T> >;

  template<typename V, V val>
    struct ValueAsType{
      // TypeList vs ValueList
      // now, we can lift ValueList to TypeList by using ValueAsType
      using type = V;
      static inline constexpr V get_value(){
        return val;
      }
    };



}}

#endif // HEADER_GUARD_4_nn_ns__metaprogramming__nn_ns__type_traits_hpp

