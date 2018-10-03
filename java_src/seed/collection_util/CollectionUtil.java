
/*
__all__:
    addAll
    py_sorted
    mkArrayList
    to_iterator
    to_iterable
    forEachExc
    append
    appendln
    string_repeat

*/
package seed.collection_util;

import seed.abc.IConsumerExc;
import seed.abc.IBiConsumerExc;

import java.util.Collections;
import java.util.Arrays;
import java.util.Collection;
import java.util.Map;
import java.util.ArrayList;
import java.util.Iterator;
import java.lang.Iterable;
import java.util.Comparator;

public interface CollectionUtil {

// addAll=py_extend
// py_sorted
// mkArrayList
public static <T> void addAll(Collection<T> c, Iterator<? extends T> iterator){
    iterator.forEachRemaining(e -> c.add(e));
}
public static <T> void addAll(Collection<T> c, Iterable<? extends T> iterable){
    addAll(c, iterable.iterator());
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
    //return mkArrayList(to_iterator(iterable));
    Iterator<? extends T> it = to_iterator(iterable);
    return mkArrayList(it);
}
public static <T>
ArrayList<T> mkArrayList(Collection<? extends T> c){
    return new ArrayList<T>(c);
}

@SafeVarargs
public static <T>
ArrayList<T> mkArrayList(T... array){
    return mkArrayList(to_iterator(array));
}








////////////////////// to_iterable/to_iterator
public static <T>
Iterable<T> to_iterable(Iterable<T> iterable){ return iterable; }
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






//////////////////// forEachExc
// forEachExc - forEach/forEachRemaining allow Exception
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
    forEachExc(to_iterator(iterable), action);
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
    forEachExc(to_iterator(iterable), action);
}
public static <K,V> void
forEachExc(Map<K,V> map
        , IBiConsumerExc<? super K,? super V> action)
throws Exception
{
    forEachExc(map.entrySet(), action);
}



///////////////////////// String
public static void append(StringBuilder s, Object... objs){
    for (Object obj : objs)
        s.append(obj);
}
public static void appendln(StringBuilder s, Object... objs){
    append(s, objs);
    s.append('\n');
}
public static void append_repeat(StringBuilder s, int times, Object... objs){
    while (times-->0)
        append(s, objs);
}
public static String string_repeat(String s, int times){
    //return new String(new char[count]).replace("\0", s);
    StringBuilder sb = new StringBuilder();
    append_repeat(sb, times, s);
    return sb.toString();
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
