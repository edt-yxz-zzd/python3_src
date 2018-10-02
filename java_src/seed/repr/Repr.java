
package seed.repr;

//import seed.collection_util.CollectionUtil; // to_iterator
//  avoid dependencies

import seed.repr.IReprable;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.Map;



public final class Repr{
// like Python.repr
// https://stackoverflow.com/questions/1350397/java-equivalent-of-python-repr
private static final char CONTROL_LIMIT = ' ';
private static final char PRINTABLE_LIMIT = '\u007e';
private static final char[] HEX_DIGITS = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };

private //final
char[] hexbuf;
private final
StringBuilder sb;
public Repr(StringBuilder sb){
    this.hexbuf = null; // new char[4];
    this.sb = sb;
}

public final StringBuilder getStringBuilder(){ return this.sb; }



public static String repr(IReprable obj) {
    return obj.__repr__();
}
public static String repr(Object obj) {
    StringBuilder sb = new StringBuilder();
    Repr self = new Repr(sb);

    self.append_repr_dynamic(obj);
    return sb.toString();
}




////////////////////////////

public final void append_basic_repr(String source) {
    // not include '""'
    final int limit = source.length();
    for (int i = 0; i < limit; ++i)
        append_basic_repr(source.charAt(i));
}

public final void append_basic_repr(byte[] bs) {
    for (byte b : bs) append_basic_repr(b);
}
public final void append_basic_repr(char[] cs) {
    for (char c : cs) append_basic_repr(c);
}


public final void append_basic_repr(byte b) {
    // not include "''"
    append_basic_repr((char)b);
}
public final void append_basic_repr(char ch) {
    // not include "''"
    switch (ch) {
    case '\0': sb.append("\\0"); break;
    case '\t': sb.append("\\t"); break;
    case '\n': sb.append("\\n"); break;
    case '\r': sb.append("\\r"); break;
    case '\"': sb.append("\\\""); break;
    case '\\': sb.append("\\\\"); break;

    default:
        if (CONTROL_LIMIT <= ch && ch <= PRINTABLE_LIMIT)
            sb.append(ch);
        else {

            sb.append("\\u");

            if (this.hexbuf == null)
                this.hexbuf = new char[4];

            for (int offs = 4; offs > 0;) {
                hexbuf[--offs] = HEX_DIGITS[ch & 0xf];
                ch >>>= 4;
            }

            sb.append(hexbuf, 0, 4);
        }
    }
}



public final void append_repr(IReprable obj) {
    obj.__append_repr__(this.sb);
}
public final void append_repr(String source) {
    sb.append('"');
    append_basic_repr(source);
    sb.append('"');
}
public final void append_repr(char ch) {
    sb.append('\'');
    append_basic_repr(ch);
    sb.append('\'');
}

public final void append_repr(int i) {
    sb.append(i);
}
public final void append_repr(boolean b) {
    sb.append(b);
}
public final void append_repr(double d) {
    sb.append(d);
}
public final void append_repr(byte b) {
    sb.append('b');
    sb.append('\'');
    append_basic_repr(b);
    sb.append('\'');
}
public final void append_repr(byte[] bs) {
    sb.append('b');
    sb.append('\'');
    append_basic_repr(bs);
    sb.append('\'');
}
public final void append_repr(char[] cs) {
    sb.append('\"');
    append_basic_repr(cs);
    sb.append('\"');
}

/////////////////////////////////////////
//public final void append_repr(Object obj) { append_repr_dynamic(obj); }
public final void append_basic_repr_dynamic(Object obj){
    // py::object.__repr__
    sb.append('<');

    // class name
    Class<?> cls = obj.getClass();
    String class_name = cls.getName();

    String may_parent_name = "";
    if (cls.isAnonymousClass()){
        Class<?> cparent = cls.getSuperclass();
        Class<?>[] may_iparents = cls.getInterfaces();
        assert may_iparents.length < 2;

        Class<?> parent = null;
        if (!cparent.equals(Object.class) || may_iparents.length == 0)
            parent = cparent;
        else {
            assert may_iparents.length == 1;
            parent = may_iparents[0];
        }

        may_parent_name = String.format("(%s)", parent.getName());
    }

    sb.append(String.format("%s%s@%x "
        , may_parent_name
        , class_name
        , System.identityHashCode(obj))
        );
    append_repr(obj.toString()); //sb.append(repr(obj.toString()));
    sb.append('>');
}
public final void append_repr_dynamic(Object obj){
    // case type of obj
    if (obj instanceof IReprable)
        append_repr((IReprable)obj);
    // IReprable must be first!!!
    else if (obj instanceof String)
        append_repr((String)obj);
    else if (obj instanceof Object[])
        append_repr((Object[])obj);
    else if (obj instanceof List)
        append_repr__list((List)obj);
    else if (obj instanceof Set)
        append_repr__set((Set)obj);
    else if (obj instanceof Map)
        append_repr__map((Map)obj);
    else if (obj instanceof char[])
        append_repr((char[])obj);
    else if (obj instanceof byte[])
        append_repr((byte[])obj);
    else if (obj instanceof Character)
        append_repr((Character)obj);
    else if (obj instanceof Integer)
        append_repr((Integer)obj);
    else if (obj instanceof Double)
        append_repr((Double)obj);
    else{
        append_basic_repr_dynamic(obj);
    }
}

public final boolean
append_basic_repr__elems(Iterator it, boolean head) {
    // not include "[]" or "{}"
    // return whether next iterator is at front
    if (!it.hasNext()) return head;

    if (head) append_repr_dynamic(it.next());
    while (it.hasNext()) {
        sb.append(", ");
        append_repr_dynamic(it.next());
    }
    return false;
}
public final void
append_basic_repr__item(Map.Entry item){
    append_repr_dynamic(item.getKey());
    append_repr(":");
    append_repr_dynamic(item.getValue());
}
public final boolean
append_basic_repr__items(Iterator<Map.Entry> it, boolean head) {
    // return whether next iterator is at front
    if (!it.hasNext()) return head;

    if (head) append_basic_repr__item(it.next());
    while (it.hasNext()) {
        sb.append(", ");
        append_basic_repr__item(it.next());
    }
    return false;
}

public final <T> void append_repr(T[] ls) {
    append_basic_repr('[');
    //append_basic_repr__elems(CollectionUtil.to_iterator(ls), true);
    append_basic_repr__elems(Arrays.asList(ls).iterator(), true);
    append_basic_repr(']');
}
public final <T> void append_repr(List<T> ls) {
    append_repr__list(ls);
}
public final void append_repr__list(List ls) {
    append_basic_repr('[');
    append_basic_repr__elems(ls.iterator(), true);
    append_basic_repr(']');
}
public final <T> void append_repr(Set<T> s) {
    append_repr__set(s);
}
public final void append_repr__set(Set s) {
    append_basic_repr('{');
    append_basic_repr__elems(s.iterator(), true);
    append_basic_repr('}');
}

public final <K,V> void append_repr(Map<K,V> map) {
    append_repr__map(map);
}
public final void append_repr__map(Map map) {
    append_basic_repr('{');
    Iterator it = map.entrySet().iterator();
    @SuppressWarnings("unchecked")
        Iterator<Map.Entry> items = (Iterator<Map.Entry>)it;
    append_basic_repr__items(items, true);
    append_basic_repr('}');
}



} // Repr



