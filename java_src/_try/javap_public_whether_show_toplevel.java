package _try;

import java.util.Collections;
import java.util.Arrays;
import java.util.List;
import java.util.Iterator;
public class javap_public_whether_show_toplevel{
    int i = 213_2;
    String s = "////////";
    javap_public_whether_show_toplevel__private_toplevel x;
    static class inner{
        public static int k = 0;
        public static void runnable(){}
        public void consumer1(){}
        public void consumer2(){}
        public void consumer3(){}
    }
    static {
        Arrays.asList(1, 2);
        inner.runnable();
        java.util.function.Consumer<inner> consumer = null;
        consumer = inner::consumer1;
        consumer.accept(null);
        consumer = inner::consumer2;
        consumer.accept(null);
        consumer = inner::consumer3;
        consumer.accept(null);
        //inner::consumer(null); inner.consumer(null); inner.consumer();
        System.out.println(inner.k);
    }
}
abstract class javap_public_whether_show_toplevel__private_toplevel
    implements Iterator{
    static {
        Collections.sort((List<String>)null);
    }
}

