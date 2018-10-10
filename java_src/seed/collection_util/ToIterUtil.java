
package seed.collection_util;


import java.util.Arrays;
import java.util.Iterator;
import java.util.stream.Stream;
import java.util.stream.BaseStream;
import java.lang.Iterable;



public interface ToIterUtil{

public class ToIterator<T> implements Iterator<T>{
    private final Iterator<? extends T> iterator;
    public ToIterator(Iterator<? extends T> iterator){
        this.iterator = iterator;
    }
    public boolean hasNext(){
        return this.iterator.hasNext();
    }
    public T next() {
        return this.iterator.next();
    }
}

public class ToIterable<T> implements Iterable<T>{
    private final Iterable<? extends T> iterable;
    public ToIterable(Iterable<? extends T> iterable){
        this.iterable = iterable;
    }
    public Iterator<T> iterator(){
        return new ToIterator<T>(this.iterable.iterator());
    }
}

////////////////////// to_iterable/to_iterator
public static <T>
Iterable<T> to_iterable(Iterable<T> iterable){ return iterable; }
public static <T>
Iterable<T> to_iterable_ex(Iterable<? extends T> iterable){
    return new ToIterable<T>(iterable);
}
@SafeVarargs
public static <T>
Iterable<T> to_iterable(T... array){
    // fixed size list ref to array
    // O(1)
    return Arrays.asList(array);
}

public static <T>
Iterator<T> to_iterator(Iterator<T> iterator){ return iterator; }
public static <T>
Iterator<T> to_iterator_ex(Iterator<? extends T> iterator){
    return new ToIterator<T>(iterator);
}
public static <T>
Iterator<T> to_iterator(Iterable<T> iterable){
    return iterable.iterator();
}
@SafeVarargs
public static <T>
Iterator<T> to_iterator(T... array){
    // fixed size list ref to array
    // O(1)
    return to_iterator(to_iterable(array));
}
public static <T,S extends BaseStream<T,S>>
Iterator<T> to_iterator(BaseStream<T,S> stream){
    return stream.iterator();
}





}//ToIterUtil
