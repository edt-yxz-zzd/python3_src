
package seed.tuples;

public class Triple<T0, T1, T2> {
    public final T0 _0_;
    public final T1 _1_;
    public final T2 _2_;

    public static <T0, T1, T2> Triple<T0, T1, T2> mk(T0 t0, T1 t1, T2 t2){
        return new Triple<T0, T1, T2>(t0, t1, t2);
    }

    public Triple(T0 t0, T1 t1, T2 t2){
        this._0_ = t0;
        this._1_ = t1;
        this._2_ = t2;
    }

    public final T0 fst(){ return this._0_; }
    public final T1 snd(){ return this._1_; }

    public final T0 get0(){ return this._0_; }
    public final T1 get1(){ return this._1_; }
    public final T2 get2(){ return this._2_; }

} // class Triple

