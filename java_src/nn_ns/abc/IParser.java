
package nn_ns.abc;

@FunctionalInterface
public interface IParser<T> {
    // err: public final static Class<T> result_type = T.class;
    public T parse(String s) throws Exception;
} // class IParser<T>

