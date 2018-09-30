/*

example:
HashMap<K,V> = new PairsBuilder<K,V>()
                .iadd(key1, value1)
                .iadd(key2, value2)
                .mkHashMap();

*/

package seed.collection_util;

import seed.collection_util.CollectionUtil;
import seed.tuples.Pair;

import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;
import java.util.HashMap;
import java.util.Iterator;

public final class PairsBuilder<K,V>{

public ArrayList<Pair<K,V>> pairs;

public PairsBuilder(){
    this.pairs = new ArrayList<>();
}
public PairsBuilder(Iterator<Pair<K,V>> iterator){
    this.pairs = CollectionUtil.mkArrayList(iterator);
}


//////////////////
public final PairsBuilder<K,V>
iadd(K k, V v){
    this.pairs.add(Pair.mk(k,v));
    return this;
}

public final Map<K,V>
iupdate_map(Map<K,V> map){
    pairs.forEach((pair) -> {
        map.put(pair.fst(), pair.snd());
    });
    return map;
}
public final HashMap<K,V>
mkHashMap(){
    Map<K,V> map = iupdate_map(new HashMap<K,V>());
    if (map instanceof HashMap)
        return (HashMap<K,V>)map;
    throw new RuntimeException();
}

public final TreeMap<K,V>
mkTreeMap(){
    //return (TreeMap)iupdate_map(new TreeMap<K,V>());
    Map<K,V> map = iupdate_map(new TreeMap<K,V>());
    if (map instanceof TreeMap)
        return (TreeMap<K,V>)map;
    throw new RuntimeException();
}

private static HashMap<Character, String>
    __map = new PairsBuilder<Character, String>()
            .iadd('a', "A")
            .iadd('b', "B")
            .mkHashMap();

static
{
    assert __map.size() == 2;
}

}// class


