
package seed.tuples;


public class Pair<T0, T1> {
    public final T0 _0_;
    public final T1 _1_;
    public Pair(T0 t0, T1 t1){
        this._0_ = t0;
        this._1_ = t1;
    }

    public static <T0, T1> Pair<T0, T1> mk(T0 t0, T1 t1){
        return new Pair<T0, T1>(t0, t1);
    }

    public final T0 fst(){ return this._0_; }
    public final T1 snd(){ return this._1_; }

    public final T0 get0(){ return this._0_; }
    public final T1 get1(){ return this._1_; }

} // class Pair

