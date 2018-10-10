
/*
__all__:
    addAll
    py_sorted
    mkArrayList
    forEachExc

    #see ToIterUtil
    to_iterator
    to_iterable

    #see StringUtil
    append
    appendln
    string_repeat
    join_tails
    join
    enclosed_join

    #see FunctionalMapUtil
    map
    mapx

*/
package seed.collection_util;

import seed.abc.IConsumerExc;
import seed.abc.IBiConsumerExc;
import seed.collection_util.ToIterUtil;
import seed.collection_util.StringUtil;
import seed.collection_util.FunctionalMapUtil;

import java.util.Collections;
import java.util.Arrays;
import java.util.Collection;
import java.util.Map;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.stream.Stream;
import java.util.stream.BaseStream;
import java.lang.Iterable;
import java.util.Comparator;

import java.util.function.Function;

public interface CollectionUtil
// useless, interface's static methods cannot be access via subclass
extends ToIterUtil, StringUtil, FunctionalMapUtil
{

// addAll=py_extend
// py_sorted
// mkArrayList
public static <T> void addAll(Collection<T> c, Iterator<? extends T> iterator){
    iterator.forEachRemaining(e -> c.add(e));
}
public static <T> void addAll(Collection<T> c, Iterable<? extends T> objs){
    addAll(c, ToIterUtil.to_iterator(objs));
}
public static <T> void addAll(Collection<T> c, Stream<? extends T> objs){
    addAll(c, ToIterUtil.to_iterator(objs));
}
@SafeVarargs
public static <T> void addAll(Collection<T> c, T... objs){
    addAll(c, ToIterUtil.to_iterator(objs));
}


public static <T extends Comparable<? super T>>
ArrayList<T> py_sorted(Iterator<T> iterator, boolean reverse){
    return py_sorted(iterator, reverse, Comparator.naturalOrder());
}
public static <T>
ArrayList<T> py_sorted(Iterator<T> iterator, boolean reverse, Comparator<? super T> cmp){
    ArrayList<T> ls = mkArrayList(iterator);
    //ls.sort(cmp);
    Collections.sort(ls, cmp);
    if (reverse)
        Collections.reverse(ls);
    return ls;
}



// Arrays.asList

public static <T>
ArrayList<T> mkArrayList(Iterator<? extends T> iterator){
    ArrayList<T> ls = new ArrayList<>();
    CollectionUtil.addAll(ls, iterator);
    return ls;
}
public static <T>
ArrayList<T> mkArrayList(Iterable<? extends T> iterable){
    //return mkArrayList(ToIterUtil.to_iterator(iterable));
    Iterator<? extends T> it = ToIterUtil.to_iterator(iterable);
    return mkArrayList(it);
}
public static <T>
ArrayList<T> mkArrayList(Collection<? extends T> c){
    return new ArrayList<T>(c);
}

@SafeVarargs
public static <T>
ArrayList<T> mkArrayList(T... array){
    return mkArrayList(ToIterUtil.to_iterator(array));
}

public static <T,I extends T,S extends BaseStream<I,S>>
ArrayList<T> mkArrayList(BaseStream<I,S> stream){
    return mkArrayList(ToIterUtil.to_iterator(stream));
}








//////////////////// forEachExc
// forEachExc - allow Exception
//              Iterable.forEach
//              Iterator.forEachRemaining
//              Stream.forEachOrdered
public static <T> void
forEachExc(Iterator<T> iterator, IConsumerExc<? super T> action)
throws Exception
{
    while (iterator.hasNext()) {
        action.accept(iterator.next());
    }
}
public static <T> void
forEachExc(Iterable<T> iterable, IConsumerExc<? super T> action)
throws Exception
{
    forEachExc(ToIterUtil.to_iterator(iterable), action);
}


public static <K,V> void
forEachExc(Iterator<Map.Entry<K,V>> iterator
        , IBiConsumerExc<? super K,? super V> action)
throws Exception
{
    forEachExc(iterator, (item)->{
        action.accept(item.getKey(), item.getValue());
    });
}
public static <K,V> void
forEachExc(Iterable<Map.Entry<K,V>> iterable
        , IBiConsumerExc<? super K,? super V> action)
throws Exception
{
    forEachExc(ToIterUtil.to_iterator(iterable), action);
}
public static <K,V> void
forEachExc(Map<K,V> map
        , IBiConsumerExc<? super K,? super V> action)
throws Exception
{
    forEachExc(map.entrySet(), action);
}

public static <T,S extends BaseStream<T,S>> void
forEachExc(BaseStream<T,S> stream, IConsumerExc<? super T> action)
throws Exception
{
    //stream.iterator() <==> stream.forEachOrdered()???
    forEachExc(ToIterUtil.to_iterator(stream), action);
}





/*
public static <K,V>
void update(Map<K,V> map, Object[]... pairs){
    for (Object[] pair : pairs){
        if (pair.length != 2)
            throw new Exception("update map from pairs, pair.length != 2");
        K k = null;
        V v = null;
        if (pair[0] instanceof K) k = (K)pair[0]; # "instanceof K" fail!!
        else
            throw new Exception("update map from pairs, pair.fst is not K");
        if (pair[1] instanceof V) v = (V)pair[1];
        else
            throw new Exception("update map from pairs, pair.snd is not V");
        map.put(k,v);
    }
}
*/


} // class CollectionUtil
