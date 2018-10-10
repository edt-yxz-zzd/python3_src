
/*
    Haskell.map
    map :: (a->b) -> [a] -> [b]
*/

package seed.collection_util;

import seed.collection_util.ToIterUtil;
//import seed.abc.IFunctionExc;
import java.util.function.Function;

import java.util.Iterator;
//import java.util.ArrayList;
//import java.util.stream.Stream;
import java.util.stream.BaseStream;
import java.lang.Iterable;

public interface FunctionalMapUtil{

public static <A,T>
Iterator<T> map(Function<? super A, ? extends T> f, Iterator<A> iterator){
    return new MapIterator<A,T>(f, iterator);
}


public static <A,T>
Iterable<T> mapx(Function<? super A, ? extends T> f, Iterable<A> iterable){
    return new MapIterable<A,T>(f, iterable);
}



////////////////////////// Haskell.map
////////////////////////// map/mapx
/*
public static <A,T>
Iterator<T> map(Function<? super A, ? extends T> f, Iterator<A> objs){
    return FunctionalMapUtil.map(f, objs);
} */
public static <A,T>
Iterator<T> map(Function<? super A, ? extends T> f, Iterable<A> objs){
    return FunctionalMapUtil.map(f, ToIterUtil.to_iterator(objs));
}
@SafeVarargs
public static <A,T>
Iterator<T> map(Function<? super A, ? extends T> f, A... objs){
    return FunctionalMapUtil.map(f, ToIterUtil.to_iterator(objs));
}
public static <A,T,S extends BaseStream<A,S>>
Iterator<T> map(Function<? super A, ? extends T> f, BaseStream<A,S> objs){
    return FunctionalMapUtil.map(f, ToIterUtil.to_iterator(objs));
}




/*
public static <A,T>
Iterable<T> mapx(Function<? super A, ? extends T> f, Iterable<A> objs){
    return FunctionalMapUtil.mapx(f, ToIterUtil.to_iterable(objs));
}*/
@SafeVarargs
public static <A,T>
Iterable<T> mapx(Function<? super A, ? extends T> f, A... objs){
    return FunctionalMapUtil.mapx(f, ToIterUtil.to_iterable(objs));
}






//////////////
public class MapIterator<A,T> implements Iterator<T> {
    //private final IFunctionExc<A,T> f;
    private final Function<? super A, ? extends T> f;
    private final Iterator<A> iterator;
    public MapIterator(Function<? super A, ? extends T> f, Iterator<A> iterator){
        this.f = f;
        this.iterator = iterator;
    }
    public boolean hasNext(){
        return this.iterator.hasNext();
    }
    //public T next() throws Exception
    public T next() {
        return this.f.apply(this.iterator.next());
    }
} // MapIterator



public static class MapIterable<A,T> implements Iterable<T> {
    private final Function<? super A, ? extends T> f;
    private final Iterable<A> iterable;
    public MapIterable(Function<? super A, ? extends T> f, Iterable<A> iterable){
        this.f = f;
        this.iterable = iterable;
    }
    public Iterator<T> iterator(){
        return map(this.f, this.iterable.iterator());
    }


} // MapIterable


} // FunctionalMapUtil
