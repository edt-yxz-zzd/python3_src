


package seed.abc;

@FunctionalInterface
public interface IConsumerExc<T>{
    void accept(T t) throws Exception;
    default IConsumerExc<T> andThen(IConsumerExc<? super T> after)
    throws Exception
    {
        return new IConsumerExc<T>(){
            public void accept(T t)
            throws Exception
            {
                this.accept(t);
                after.accept(t);
            }
        };
    }
}


