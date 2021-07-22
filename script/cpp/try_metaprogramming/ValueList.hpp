
//ValueList.hpp

#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__ValueList_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__ValueList_hpp
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

namespace nn_ns{namespace metaprogramming{ namespace ValueList{ namespace PackedValueList{




  template <typename V>
    struct ValueList{
      template<V...> class List;
    };
  template<typename V, V... args>
    using Mk_ValueList = typename ValueList<V>::template List<args...>;
  /*
  template<typename V, template<V...> class T, typename lhs, typename rhs>
    struct Concatenation_vs_vs;
  template<typename V, template<V...> class T, template<V...> class lhs, template<V...> class rhs, V... lhs_args, V... rhs_args>
    struct Concatenation_vs_vs<V, T, lhs<lhs_args...>, rhs<rhs_args...> >{
      using type = T<lhs_args..., rhs_args...>;
    };
    */
  template<typename V, typename lhs, typename rhs>
    struct Concatenation_vs_vs_;
  template<typename V, typename lhs, typename rhs>
    using Concatenation_vs_vs = Get_the_type_member<Concatenation_vs_vs_<V, lhs, rhs> >;
  template<typename V, V lhs, typename rhs>
    using Concatenation_v_vs = Concatenation_vs_vs<V, Mk_ValueList<V, lhs>, rhs>;

  //without V ==>> lhs<> with no args ==>> donot know V
  //error: class template partial specialization contains template parameters that cannot be deduced; this partial specialization will never be used
  //
  //
  template<typename V, V... lhs_args, V... rhs_args, template<V...> class lhs, template<V...> class rhs>
    struct Concatenation_vs_vs_<
        V
        ,lhs<lhs_args...>
        ,rhs<rhs_args...> >
    {
      //using type = typename ValueList<V>::template List<lhs_args..., rhs_args...>;
      using type = Mk_ValueList<V, lhs_args..., rhs_args...>;
    };
  /*
  template<typename V, V... lhs_args, V... rhs_args>
    struct Concatenation_vs_vs_<
        V
        ,typename ValueList<V>::template List<lhs_args...>
        ,typename ValueList<V>::template List<rhs_args...> >
    {
      using type = typename ValueList<V>::template List<lhs_args..., rhs_args...>;
    };
  */

  template<typename V, template<V...> class Output, typename Input>
    struct From_ValueList_;
  template<typename V, template<V...> class Output, typename Input>
    using From_ValueList = Get_the_type_member<From_ValueList_<V, Output, Input> >;
  template<typename V, template<V...> class Output, template<V...> class Input, V... args>
    //bug:struct From_ValueList_<V, Output, typename ValueList<V>::template List<args...> >
    struct From_ValueList_<V, Output, Input<args...> >
    {
      using type = Output<args...>;
    };


  template<typename V, typename Input>
    struct To_ValueList_;
  template<typename V, typename Input>
    using To_ValueList = Get_the_type_member<To_ValueList_<V, Input> >;
  template<typename V, template<V...> class Input, V... args>
    struct To_ValueList_<V, Input<args...> >
    {
      //using type = typename ValueList<V>::template List<args...>;
      using type = Mk_ValueList<V, args...>;
    };





}}}}

//#include "ValueList__impl.cpp"
#endif // HEADER_GUARD_4_nn_ns__metaprogramming__ValueList_hpp





