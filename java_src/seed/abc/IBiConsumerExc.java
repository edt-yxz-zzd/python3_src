


package seed.abc;

@FunctionalInterface
public interface IBiConsumerExc<T,U>{
    void accept(T t, U u) throws Exception;
    default IBiConsumerExc<T,U> andThen(IBiConsumerExc<? super T,? super U> after)
    throws Exception
    {
        return new IBiConsumerExc<T,U>(){
            public void accept(T t, U u)
            throws Exception
            {
                this.accept(t, u);
                after.accept(t, u);
            }
        };
    }
}


