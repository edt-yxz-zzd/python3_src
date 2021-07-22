
//TypeList.hpp

#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__TypeList_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__TypeList_hpp
#include "TypeList.hpp"
  //List__Empty
  //List__Con
  //
  //Get_List_Head_
  //Get_List_Head
  //Get_List_Tail_
  //Get_List_Tail
  //
  //is_List__Empty
  //is_List__Con____shallow
  //is_List____shallow
  //is_List__Con____deep
  //is_List____deep
  //
  //is_List_with_all____deep
  //all4List
  //is_List_with_any____deep
  //any4List
  //
  //////Lookup AssociatedList
  //Is_Made_By_Constructor
  //AssociatedListItem
  //Get_Associated_KeyT_
  //Get_Associated_KeyT
  //Get_Associated_ValueT_
  //Get_Associated_ValueT
  //Is_AssociatedListItem
  //is_AssociatedListItem
  //
  //is_AssociatedList
  //Lookup_First_MayEmptySub_AssociatedList_
  //Lookup_First_MayEmptySub_AssociatedList
  //Lookup_Maybe_First_AssociatedListItem_
  //Lookup_Maybe_First_AssociatedListItem
  //is_Key_in_AssociatedList
  //












#include "nn_ns__exceptions.hpp"
  //AssertError
  //ValueError
  //assertE
  //assertF
  //


#include "nn_ns__type_traits.hpp"
  //Get_the_type_member
  //get_the_value_member
  //If_Then_Else
  //Echo_ Echo
  //Enable_if
  //

namespace nn_ns{namespace metaprogramming{ namespace TypeList{ namespace LinkedTypeList{


  struct List__Empty;
  template<typename Head, typename Tail>
    struct List__Con;


  template<typename List>
    struct Get_List_Head_;
  template<typename List>
    using Get_List_Head = Get_the_type_member<Get_List_Head_<List> >;
  template<typename Head, typename Tail>
    struct Get_List_Head_<List__Con<Head, Tail> >
    {
      using type = Head;
    };


  template<typename List>
    struct Get_List_Tail_;
  template<typename List>
    using Get_List_Tail = Get_the_type_member<Get_List_Tail_<List> >;
  template<typename Head, typename Tail>
    struct Get_List_Tail_<List__Con<Head, Tail> >
    {
      using type = Tail;
    };



  template<typename List>
    inline constexpr bool is_List__Empty(){
      return std::is_same<List, List__Empty>();
    }
  template<typename List>
    struct Is_List__Con____shallow{
      static constexpr bool value = false;
    };
  template<typename Head, typename Tail>
    struct Is_List__Con____shallow<List__Con<Head, Tail> >{
      static constexpr bool value = true;
    };
  template<typename List>
    inline constexpr bool is_List__Con____shallow(){
      return get_the_value_member<Is_List__Con____shallow<List> >();
    }
  template<typename List>
    inline constexpr bool is_List____shallow(){
      return is_List__Empty<List>() || is_List__Con____shallow<List>();
    }

  template<typename List>
    inline constexpr auto is_List__Con____deep() -> Enable_if<! is_List__Con____shallow<List>(), bool>
    {
      return false;
    }
  template<typename List>
    inline constexpr bool is_List____deep(){
      return is_List__Empty<List>() || is_List__Con____deep<List>();
    }
  template<typename List>
    inline constexpr auto is_List__Con____deep() -> Enable_if<is_List__Con____shallow<List>(), bool>
    {
      return is_List____deep<Get_List_Tail<List> >();
    }


//#if 0
  // /*
  template<template<typename Elem> class Predicator, typename List>
    inline constexpr auto is_List_with_all____deep__ver1() -> Enable_if<!is_List____shallow<List>(), bool>
    {
      return false;
    }
  template<template<typename Elem> class Predicator, typename List>
    inline constexpr auto is_List_with_all____deep__ver1() -> Enable_if<is_List__Empty<List>(), bool>
    {
      return true;
    }
  template<template<typename Elem> class Predicator, typename List>
    inline constexpr auto is_List_with_all____deep__ver1() -> Enable_if<is_List__Con____shallow<List>(), bool>
    {
      return get_the_value_member<Predicator<Get_List_Head<List> > >() && is_List_with_all____deep__ver1<Predicator, Get_List_Tail<List> >();
    }
    // */
//#else
  template<template<typename Elem> class Predicator, typename List, bool prev_pred_result=true>
    struct Is_List_with_all____deep{
      static constexpr bool value = false;
      static_assert(prev_pred_result||!value, "logic-err:not [[!prev_pred_result] -->> [!value]]");

    };

  template<template<typename Elem> class Predicator, bool prev_pred_result>
    struct Is_List_with_all____deep<Predicator, List__Empty, prev_pred_result>{
      static constexpr bool value = prev_pred_result;
      static_assert(prev_pred_result||!value, "logic-err:not [[!prev_pred_result] -->> [!value]]");
    };
  template<template<typename Elem> class Predicator, typename Head, typename Tail>
    struct Is_List_with_all____deep<Predicator, List__Con<Head, Tail>, false>{
      static constexpr bool value = false;
    };
  template<template<typename Elem> class Predicator, typename Head, typename Tail>
    struct Is_List_with_all____deep<Predicator, List__Con<Head, Tail>, true>
    :Is_List_with_all____deep<Predicator, Tail, get_the_value_member<Predicator<Head> >() >
    {
    };
  template<template<typename Elem> class Predicator, typename List>
    inline constexpr bool is_List_with_all____deep__ver2() {
      return get_the_value_member<Is_List_with_all____deep<Predicator, List> >();
    }
//#endif

  template<template<typename Elem> class Predicator, typename List>
    inline constexpr bool is_List_with_all____deep() {
      return assertE(
          ( is_List_with_all____deep__ver2<Predicator,List>()
          ==is_List_with_all____deep__ver1<Predicator,List>()
          )
          , is_List_with_all____deep__ver2<Predicator,List>()
          );
    }

  template<template<typename Elem> class Predicator, typename List>
    inline constexpr bool all4List() {
      static_assert(is_List____deep<List>(), "not LinkedTypeList");
      return is_List_with_all____deep<Predicator, List>();
    }








  template<template<typename Elem> class Predicator, typename List, bool prev_pred_result=false, bool prev_is__List=true>
    struct Is_List_with_any____deep{
      static constexpr bool value = false;
      static_assert((prev_is__List||!value) && ((!(prev_is__List&&prev_pred_result))||(value==is_List____deep<List>())), "logic-err:not [[!prev_is__List] -->> [!value]][[prev_is__List][prev_pred_result] -->> [value=is_List____deep<List>()]]");

    };

  template<template<typename Elem> class Predicator, bool prev_pred_result, bool prev_is__List>
    struct Is_List_with_any____deep<Predicator, List__Empty, prev_pred_result, prev_is__List>{
      static constexpr bool value = prev_is__List && prev_pred_result;
      static_assert((prev_is__List||!value) && ((!(prev_is__List&&prev_pred_result))||(value==is_List____deep<List__Empty>())), "logic-err:not [[!prev_is__List] -->> [!value]][[prev_is__List][prev_pred_result] -->> [value=is_List____deep<List>()]]");
    };
  template<template<typename Elem> class Predicator, typename Head, typename Tail>
    struct Is_List_with_any____deep<Predicator, List__Con<Head, Tail>, true, true>{
      static constexpr bool value = is_List____deep<Tail>();
    };
  template<template<typename Elem> class Predicator, typename Head, typename Tail>
    struct Is_List_with_any____deep<Predicator, List__Con<Head, Tail>, false, true>
    :Is_List_with_any____deep<Predicator, Tail, get_the_value_member<Predicator<Head>, true>() >
    {
    };
  template<template<typename Elem> class Predicator, typename List>
    inline constexpr bool is_List_with_any____deep() {
      return get_the_value_member<Is_List_with_any____deep<Predicator, List> >();
    }

  template<template<typename Elem> class Predicator, typename List>
    inline constexpr bool any4List() {
      static_assert(is_List____deep<List>(), "not LinkedTypeList");
      return is_List_with_any____deep<Predicator, List>();
    }




  template <template<typename...> class Constructor, typename T>
    struct Is_Made_By_Constructor{
      static constexpr bool value = false;
    };
  template <template<typename...> class Constructor, typename... args>
    struct Is_Made_By_Constructor<Constructor, Constructor<args...> >{
      static constexpr bool value = true;
    };



  template<typename fst, typename snd>
    struct AssociatedListItem;
  template <typename Item>
    struct Get_Associated_KeyT_;
  template <typename Item>
    using Get_Associated_KeyT = Get_the_type_member<Get_Associated_KeyT_<Item> >;
  template <typename Item>
    struct Get_Associated_ValueT_;
  template <typename Item>
    using Get_Associated_ValueT = Get_the_type_member<Get_Associated_ValueT_<Item> >;

  template<typename fst, typename snd>
    struct Get_Associated_KeyT_<AssociatedListItem<fst, snd> >{
      using type = fst;
    };
  template<typename fst, typename snd>
    struct Get_Associated_ValueT_<AssociatedListItem<fst, snd> >{
      using type = snd;
    };


  template <typename Item>
    struct Is_AssociatedListItem
      :Is_Made_By_Constructor<AssociatedListItem, Item>
    {};
  template<typename Item>
    inline constexpr bool is_AssociatedListItem(){
      return get_the_value_member<Is_AssociatedListItem<Item> >();
    }
  template<typename List>
    inline constexpr bool is_AssociatedList(){
      return is_List_with_all____deep<Is_AssociatedListItem, List>();
    }

  template<typename Key, typename AssociatedList>
    struct Lookup_First_MayEmptySub_AssociatedList_{
      static_assert(is_AssociatedList<AssociatedList>(), "not AssociatedList");
      //static_assert(false, "logic-err");
      //using type = List__Empty;
    };
  template<typename Key, typename AssociatedList>
    using Lookup_First_MayEmptySub_AssociatedList = Get_the_type_member<Lookup_First_MayEmptySub_AssociatedList_<Key, AssociatedList> >;


  template<typename Key>
    struct Lookup_First_MayEmptySub_AssociatedList_<Key, List__Empty>{
      using type = List__Empty;
      static_assert(is_AssociatedList<type>(), "logic-err:not AssociatedList");
    };
  template<typename Key, typename fst, typename snd, typename Tail>
    struct Lookup_First_MayEmptySub_AssociatedList_<
      Key
      , List__Con<
          AssociatedListItem<fst, snd>
          ,Tail
          >
      > : Lookup_First_MayEmptySub_AssociatedList_<Key, Tail>
    {
    };

  template<typename Key, typename snd, typename Tail>
    struct Lookup_First_MayEmptySub_AssociatedList_<
      Key
      , List__Con<
          AssociatedListItem<Key, snd>
          ,Tail
          >
      >
    {
      static_assert(is_AssociatedList<Tail>(), "not AssociatedList");
      using type = List__Con<
          AssociatedListItem<Key, snd>
          ,Tail
          >;
      static_assert(is_AssociatedList<type>(), "logic-err:not AssociatedList");
    };


  template<typename Key, typename AssociatedList>
    struct Lookup_Maybe_First_AssociatedListItem_{
      static_assert(is_AssociatedList<AssociatedList>(), "not AssociatedList");
      using MayEmptySub_AssociatedList = Lookup_First_MayEmptySub_AssociatedList<Key, AssociatedList>;
      static constexpr bool is_Nothing = std::is_same<MayEmptySub_AssociatedList, List__Empty>();
      // void | AssociatedListItem<Key, ?>
      using Maybe_Item = Get_the_type_member<
        If_Then_Else<
            is_Nothing
            ,Echo_<void>
            ,Get_List_Head_<MayEmptySub_AssociatedList>
            >
        >;
      using Maybe_Value = Get_the_type_member<
        If_Then_Else<
            is_Nothing
            ,Echo_<void>
            ,Get_Associated_ValueT_<Maybe_Item>
            >
        >;

      using type = Maybe_Item;
    };
  template<typename Key, typename AssociatedList>
    using Lookup_Maybe_First_AssociatedListItem = Get_the_type_member<Lookup_Maybe_First_AssociatedListItem_<Key, AssociatedList> >;

  template<typename Key, typename AssociatedList>
    inline constexpr bool is_Key_in_AssociatedList(){
      static_assert(is_AssociatedList<AssociatedList>(), "not AssociatedList");
      return ! Lookup_Maybe_First_AssociatedListItem_<Key, AssociatedList> :: is_Nothing;
      //return ! std::is_same<void, Lookup_Maybe_First_AssociatedListItem<Key, AssociatedList> >();
    }



}}}}

//#include "TypeList__impl.cpp"
#endif // HEADER_GUARD_4_nn_ns__metaprogramming__TypeList_hpp





