
//IStringBluePrint
//Append/AppendLn/Repeat/Join/JoinTail/JoinInitial/Enclose/EnclosedJoinEx
//mkEnclosedJoin
//
// append/appendln/append_repeat/string_repeat
// join_tails/join/enclosed_join

package seed.collection_util;

import seed.collection_util.ToIterUtil;

import java.util.Iterator;
//import java.util.stream.Stream;
import java.util.stream.BaseStream;
import java.lang.Iterable;

public interface StringUtil{


///////////////////////// IStringBluePrint
//IStringBluePrint
//Append/AppendLn/Repeat/Join/JoinTail/JoinInitial/Enclose/EnclosedJoinEx
//mkEnclosedJoin
public interface IStringBluePrint{
    public void append_to(StringBuilder s);
    public static void append1(StringBuilder s, IStringBluePrint obj){
        obj.append_to(s);
    }
    public static void append1(StringBuilder s, Object obj){
        if (obj instanceof IStringBluePrint){
            ((IStringBluePrint)obj).append_to(s); // avoid genenrate temp string
        }else{
            s.append(obj);
        }
    }
    public static void appends(StringBuilder s, Iterator<?> objs){
        objs.forEachRemaining(obj-> append1(s, obj));
    }
    public static void appends(StringBuilder s, Object... objs){
        appends(s, ToIterUtil.to_iterator(objs));
    }
    public static void appends(StringBuilder s, Iterable<?> objs){
        appends(s, ToIterUtil.to_iterator(objs));
    }
    public static <I,S extends BaseStream<I,S>>
    void appends(StringBuilder s, BaseStream<I,S> objs){
        appends(s, ToIterUtil.to_iterator(objs));
    }
    public default String mkString(){
        StringBuilder s = new StringBuilder();
        this.append_to(s);
        return s.toString();
    }
    //public default final String toString() # not allow "final"
    /* not allow override "toString"
    public default String toString(){
        return this.mkString();
    }
    */
}
public abstract class StringBluePrintABC implements IStringBluePrint{
    public final String toString(){
        return this.mkString();
    }
}
public abstract class StringBluePrintABC__objs extends StringBluePrintABC {
    protected final Iterable<?> objs;
    public StringBluePrintABC__objs(Iterable<?> objs){
        this.objs = objs;
    }
    public StringBluePrintABC__objs(Object... objs){
        this(ToIterUtil.to_iterable(objs));
    }
}
public abstract class StringBluePrintABC__sep_objs extends StringBluePrintABC__objs {
    protected final Object sep;
    public StringBluePrintABC__sep_objs(Object sep, Iterable<?> objs){
        super(objs);
        this.sep = sep;
    }
    public StringBluePrintABC__sep_objs(String sep, Object... objs){
        this(sep, ToIterUtil.to_iterable(objs));
    }
}
public class Append extends StringBluePrintABC__objs {
    public Append(Iterable<?> objs){ super(objs); }
    public Append(Object... objs){ super(objs); }
    public void append_to(StringBuilder s){
        //append(s, this.objs);//to avoid temp string
        IStringBluePrint.appends(s, this.objs);
    }
}
public class AppendLn extends Append {
    public AppendLn(Iterable<?> objs){ super(objs); }
    public AppendLn(Object... objs){ super(objs); }
    public void append_to(StringBuilder s){
        //appendln(s, this.objs);
        super.append_to(s);
        s.append('\n');
    }
}

public class Repeat extends StringBluePrintABC {
    private final int times;
    private final Object obj;
    public Repeat(int times, Iterable<?> objs){
        this.times = times;
        this.obj = new Append(objs);
    }
    public Repeat(int times, Object... objs){
        if (objs.length == 0){
            this.times = 0;
            this.obj = null;
        } else if (objs.length == 1){
            this.times = times;
            this.obj = objs[0];
        } else{
            //this(times, ToIterUtil.to_iterable(objs));
            this.times = times;
            this.obj = new Append(objs);
        }
    }

    public void append_to(StringBuilder s){
        int times = this.times;
        while (times --> 0){
            //append(s, this.obj);
            IStringBluePrint.append1(s, this.obj);
        }
    }
}


public class Join extends StringBluePrintABC__sep_objs {
    // EnclosedJoinEx("",""  ,"",""  ,"",""  ,sep,objs)
    public Join(Object sep, Iterable<?> objs){ super(sep, objs); }
    public Join(String sep, Object... objs){ super(sep, objs); }
    public void append_to(StringBuilder s){
        Iterator<?> it = ToIterUtil.to_iterator(this.objs);
        if (!it.hasNext()) return;
        IStringBluePrint.append1(s, it.next());
        while (it.hasNext()) {
            IStringBluePrint.append1(s, this.sep);
            IStringBluePrint.append1(s, it.next());
        }
    }
}
public class JoinTail extends StringBluePrintABC__sep_objs {
    // EnclosedJoinEx("",""  ,sep,""  ,"",""  ,sep,objs)
    public JoinTail(Object sep, Iterable<?> objs){ super(sep, objs); }
    public JoinTail(String sep, Object... objs){ super(sep, objs); }
    public void append_to(StringBuilder s){
        Iterator<?> it = ToIterUtil.to_iterator(this.objs);
        while (it.hasNext()) {
            IStringBluePrint.append1(s, this.sep);
            IStringBluePrint.append1(s, it.next());
        }
    }
}
public class JoinInitial extends StringBluePrintABC__sep_objs {
    // EnclosedJoinEx("",""  ,"",sep  ,"",""  ,sep,objs)
    public JoinInitial(Object sep, Iterable<?> objs){ super(sep, objs); }
    public JoinInitial(String sep, Object... objs){ super(sep, objs); }
    public void append_to(StringBuilder s){
        Iterator<?> it = ToIterUtil.to_iterator(this.objs);
        while (it.hasNext()) {
            IStringBluePrint.append1(s, it.next());
            IStringBluePrint.append1(s, this.sep);
        }
    }
}
public class EnclosedJoinEx extends StringBluePrintABC__sep_objs {
    private final Object always_global_open;
    private final Object always_global_close;
    private final Object optional_global_open;
    private final Object optional_global_close;
    private final Object local_open;
    private final Object local_close;
    public EnclosedJoinEx(
        Object always_global_open, Object always_global_close
        , Object optional_global_open, Object optional_global_close
        , Object local_open, Object local_close
        , Object sep, Iterable<?> objs)
    {
        super(sep, objs);
        this.always_global_open = always_global_open;
        this.always_global_close = always_global_close;
        this.optional_global_open = optional_global_open;
        this.optional_global_close = optional_global_close;
        this.local_open = local_open;
        this.local_close = local_close;
    }
    public EnclosedJoinEx(
        String always_global_open, String always_global_close
        , String optional_global_open, String optional_global_close
        , String local_open, String local_close
        , String sep, Object... objs)
    {
        this(always_global_open, always_global_close
                , optional_global_open, optional_global_close
                , local_open, local_close
                , sep, ToIterUtil.to_iterable(objs));
    }

    public void append_to(StringBuilder s){
        IStringBluePrint.append1(s, this.always_global_open);
        Iterator<?> it = ToIterUtil.to_iterator(this.objs);
        if (it.hasNext()){
            IStringBluePrint.append1(s, this.optional_global_open);
            IStringBluePrint.append1(s, it.next());
            while (it.hasNext()) {
                IStringBluePrint.append1(s, this.sep);
                IStringBluePrint.append1(s, it.next());
            }
            IStringBluePrint.append1(s, this.optional_global_close);
        }
        IStringBluePrint.append1(s, this.always_global_close);
    }
}
public class Enclose extends StringBluePrintABC {
    // EnclosedJoinEx(open,close  ,"",""  ,"",""  ,"",[middle])
    private final Object open;
    private final Object close;
    private final Object middle;
    public Enclose(Object open, Object close, Object middle){
        this.open = open;
        this.close = close;
        this.middle = middle;
    }
    public void append_to(StringBuilder s){
        IStringBluePrint.append1(s, this.open);
        IStringBluePrint.append1(s, this.middle);
        IStringBluePrint.append1(s, this.close);
    }
}
public static IStringBluePrint
mkEnclosedJoin(Object open, Object close, Object sep, Iterable<?> middle_objs){
    // EnclosedJoinEx(open,close  ,"",""  ,"",""  ,sep,middle_objs)
    return new Enclose(open, close, new Join(sep, middle_objs));
}
/*
public static IStringBluePrint
mkJoinTail(Object sep, Iterable<?> objs){
    //bug:return new Append(sep, new Join(sep, objs));
}*/

///////////////////////// String
// append/appendln/append_repeat/string_repeat
// join_tails/join/enclosed_join
public static void append(StringBuilder s, Iterator<?> objs){
    objs.forEachRemaining((obj)->s.append(obj));
}
public static void append(StringBuilder s, Object... objs){
    append(s, ToIterUtil.to_iterator(objs));
}
public static void append(StringBuilder s, Iterable<?> objs){
    append(s, ToIterUtil.to_iterator(objs));
}
public static <T,S extends BaseStream<T,S>>
void append(StringBuilder s, BaseStream<T,S> objs){
    append(s, ToIterUtil.to_iterator(objs));
}



public static void appendln(StringBuilder s, Iterator<?> objs){
    append(s, objs);
    s.append('\n');
}
public static void appendln(StringBuilder s, Iterable<?> objs){
    appendln(s, ToIterUtil.to_iterator(objs));
}
public static void appendln(StringBuilder s, Object... objs){
    appendln(s, ToIterUtil.to_iterator(objs));
}



//bug: public static void append_repeat(StringBuilder s, int times, Iterator<Object> objs)
public static void append_repeat(StringBuilder s, int times, Iterable<?> objs){
    while (times --> 0)
        append(s, objs);
}
public static void append_repeat(StringBuilder s, int times, Object... objs){
    append_repeat(s, times, ToIterUtil.to_iterable(objs));
}
public static String string_repeat(String s, int times){
    //return new String(new char[count]).replace("\0", s);
    StringBuilder sb = new StringBuilder();
    append_repeat(sb, times, s);
    return sb.toString();
}




public static void join_tails(StringBuilder s, String sep, Iterator<?> objs){
    objs.forEachRemaining((obj)->{
        s.append(sep);
        s.append(obj);
    });
}
public static void join_tails(StringBuilder s, String sep, Object... objs){
    join_tails(s, sep, ToIterUtil.to_iterator(objs));
}
public static void join_tails(StringBuilder s, String sep, Iterable<?> objs){
    join_tails(s, sep, ToIterUtil.to_iterator(objs));
}




public static void join(StringBuilder s, String sep, Iterator<?> objs){
    if (!objs.hasNext()) return;

    s.append(objs.next());
    join_tails(s, sep, objs);
}
public static void join(StringBuilder s, String sep, Iterable<?> objs){
    join(s, sep, ToIterUtil.to_iterator(objs));
}
public static void join(StringBuilder s, String sep, Object... objs){
    join(s, sep, ToIterUtil.to_iterator(objs));
}

public static String join(String sep, Iterator<?> objs){
    StringBuilder s = new StringBuilder();
    join(s, sep, ToIterUtil.to_iterator(objs));
    return s.toString();
}
public static void enclosed_join(StringBuilder s, String open, String close, String sep, Iterator<?> objs){
    s.append(open);
    join(s, sep, ToIterUtil.to_iterator(objs));
    s.append(close);
}
public static String enclosed_join(String open, String close, String sep, Iterator<?> objs){
    StringBuilder s = new StringBuilder();
    enclosed_join(s, open, close, sep, objs);
    return s.toString();
}




}
