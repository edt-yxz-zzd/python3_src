
package seed.abc;
//import java.util.function.Function;

public interface IFunctionExc<A,R>{

R apply(A a) throws Exception;

default <S> IFunctionExc<A,S>
andThen(IFunctionExc<? super R,? extends S> after)
throws Exception{
    return new IFunctionExc<A,S>(){
        public S apply(A a) throws Exception{
            return after.apply(IFunctionExc.this.apply(a));
        };
    };
}

default <I> IFunctionExc<I,R>
compose(IFunctionExc<? super I,? extends A> before)
throws Exception{
    //return before.andThen(this); error?
    return new IFunctionExc<I,R>(){
        public R apply(I i) throws Exception{
            return IFunctionExc.this.apply(before.apply(i));
        };
    };
}
static <A> IFunctionExc<A,A> identity(){


    //return IFunctionExc_Identity.id;
    return new IFunctionExc<A,A>(){
        public A apply(A a) throws Exception{ return a; };
    };
}


} // IFunctionExc


/*
    class IFunctionExc_Identity<A,A> implements IFunctionExc<A,A>
    {
        public A apply(A a) throws Exception{ return a; };
        public static final <A>
        IFunctionExc<A,A> id = new IFunctionExc_Identity<A,A>();
    }
*/
