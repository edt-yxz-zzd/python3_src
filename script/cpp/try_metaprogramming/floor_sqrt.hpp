
//floor_sqrt.hpp

/*

e ../../python3_src/script/cpp/try_metaprogramming/floor_sqrt.hpp
clang ../../python3_src/script/cpp/try_metaprogramming/floor_sqrt.hpp

*/
#ifndef HEADER_GUARD_4_nn_ns__metaprogramming__floor_sqrt_hpp
#define HEADER_GUARD_4_nn_ns__metaprogramming__floor_sqrt_hpp
#include "floor_sqrt.hpp"
  //floor_sqrt
  //cached_floor_sqrt








#include <limits>
  //numeric_limits<double>::epsilon()/max()/min()/lowest()
  //    lowest() < 0 #smallest value # vs -max()
  //    min() > 0 # the smallest positive normalized number # vs 1/max()
  //    epsilon() > 0 is the smallest positive floating-point number such that 1+epsilon−1 is larger than 0.
  //
  //numeric_limits<int>::max()/min()
  //numer ic_limits<T>::is_specialized; //is infor mation available for numer ic_limits<T>?
  //static const bool is_specialized = true;//yes, we have infor mation 
  //static const int digits = 7;//number of bits (‘‘binar y digits’’) excluding sign 
  //static const bool is_signed = true;//this implementation has char signed 
  //static const bool is_integer = true;//char is an integral type
#include <type_traits>
  //enable_if<b, T>::type
  //is_integral<X>()
  //is_unsigned<X>() #::value
  //is_nothrow_constructible<X,args>
  //is_same<X,Y> Is X the same type as Y?
  //is_base_of<X,Y> Is X a base of Y?
  //is_convertible<X,Y> Can an X be implicitly converted to a Y?

#include "nn_ns__exceptions.hpp"
  //AssertError
  //ValueError
  //assertE
  //
namespace nn_ns{ namespace metaprogramming{
  template <typename U>
    struct Constants{
      public:
      static_assert(std::is_nothrow_constructible<U>(), "U requires U{}");
      static_assert(std::is_nothrow_constructible<U, bool>(), "U requires U{true}");

      private:
      static inline constexpr U inc__impl(U u){
        //return ++u;//success??
        return u+get_1();
      }
      static inline constexpr U get_1__impl(){
        return {true};
        //recur:return inc(get_0());
        //return {1};
        //fail:return ++get_0();
      }
      public:
      static inline constexpr U check_gt(U u, U v){
        return assertE(u > v, u);
      }
      static inline constexpr U inc(U u){
        return check_gt(inc__impl(u), u);
      }
      static inline constexpr U get_0(){
        return {};
      }
      static inline constexpr auto get_1()->typename std::enable_if<(get_0()<get_1__impl()), U>::type{
        return get_1__impl();
      }
      //static inline constexpr U get_2(){}
      static inline constexpr auto get_2()->typename std::enable_if<(get_0()<get_1__impl() && get_1__impl()<inc__impl(get_1__impl())), U>::type{
        return inc(get_1());
        //return {2};
        //fail:return ++get_1();
      }
    };
  template <typename U>
    struct FloorSqrt{
      //static_assert(std::is_integral<U>() && std::is_unsigned<U>(), "U is not unsigned integral");
      static_assert(std::is_integral<U>(), "U is not integral");
      //static_assert(std::is_unsigned<U>(), "U is not unsigned");
      static inline constexpr U floor_sqrt(U u){
        //return assertE(u>=(Constants<U>::get_0()), u);
        return (u<(Constants<U>::get_0()))?throw AssertError() : check_floor_sqrt(floor_sqrt__impl(u), u);
      }
      template <U u>
        struct CachedFloorSqrt{
          static constexpr U value = floor_sqrt(u);
        };
      static inline constexpr U check_floor_sqrt(U result, U u){
        return ((result < (Constants<U>::get_0()))
                // [result>=0]
              || (u < result)
                // [0<=result<=u]
              || (result!=(Constants<U>::get_0()) && u/result < result)
                // [0<=result<=u][result**2<=u]
              || (result < u && (result+ (Constants<U>::get_1())) <= u/(result+ (Constants<U>::get_1())))
                // [0<=result<=u][result**2<=u<(result+1)**2]
              )? throw AssertError() : result;
            //cmp_uint_with_sum
      }
      private:
      static inline constexpr U floor_sqrt__impl(U u){
        /*
           * Newton_iter::
            f(x)=x^2-u
            f'(x) = 2*x
            x' := x-f(x)/f'(x) = x-(x^2-u)/(2*x) = x/2+u/2/x = (x+u/x)/2;
            dx = x' - x = u/2/x - x/2
           * bisearch::
        */
        return (u<(Constants<U>::get_0()))? throw ValueError():(u <= (Constants<U>::get_1()))? u : floor_sqrt__impl__bisearch(u, {}, u);
      }
      static inline constexpr U floor_sqrt__impl__bisearch(U u, U begin, U end){
        return (
                (! (begin < end
                    && Constants<U>::get_1() < end
                      // protect get_2 below
                    )
                 )?
                    throw AssertError()
                    :floor_sqrt__impl__bisearch__mid(u, begin, begin+((end-begin)/((Constants<U>::get_2()))), end)
              );
      }
      static inline constexpr U floor_sqrt__impl__bisearch__mid(U u, U begin, U mid, U end){
        return ((begin==mid)?
                  ((end-begin!=(Constants<U>::get_1()))?
                    throw AssertError()
                    :begin
                  )
                  :((u/mid < mid)?
                    floor_sqrt__impl__bisearch(u, begin, mid)
                    :floor_sqrt__impl__bisearch(u, mid, end)
                   )
                );

      }
    };

  template <typename U, U u>
    inline constexpr U cached_floor_sqrt(){
      return FloorSqrt<U>::template CachedFloorSqrt<u>::value;
    }
  template <typename U>
    inline constexpr U floor_sqrt(U u){
      return FloorSqrt<U>::floor_sqrt(u);
    }


}}

#endif // HEADER_GUARD_4_nn_ns__metaprogramming__floor_sqrt_hpp


