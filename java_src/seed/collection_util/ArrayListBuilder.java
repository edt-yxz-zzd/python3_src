
package seed.collection_util;

import seed.collection_util.CollectionUtil;

import java.util.Arrays;
import java.util.Iterator;
import java.util.ArrayList;

public final class ArrayListBuilder<T> extends ArrayList<T> {

//public ArrayListBuilder(){}

@SafeVarargs
public ArrayListBuilder(T... ts){
    super(Arrays.asList(ts));
}
public ArrayListBuilder(Iterator<T> ts){
    super();
    CollectionUtil.addAll(this, ts);
}


///////////////
@SafeVarargs
public final ArrayListBuilder<T>
iadd(T... ts){
    //this.add(t);
    //return this;
    return iaddAll(ts);
}

public final ArrayListBuilder<T>
iaddAll(T[] ts){
    this.addAll(Arrays.asList(ts));
    return this;
}
public final ArrayListBuilder<T>
iaddAll(Iterator<T> ts){
    CollectionUtil.addAll(this, ts);
    return this;
}

@SafeVarargs
public static <T> ArrayListBuilder<T>
mk(T... ts){
    return new ArrayListBuilder<T>(ts);
}

private static ArrayList<String>
    __ls = mk("0", "1").iadd("2").iadd("3", "4");
static{
    assert __ls.size() == 5;
}

}//class


