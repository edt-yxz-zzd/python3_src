

/*

why Haskell can use
    Either a b = (a->r) -> (b->r) -> r
    either :: (a->r) -> (b->r) -> Either a b -> r
    ??
    because
        1. all datatypes in it are immutable
        2. has not "instanceof"
    so Java cannot implement as below:
        public interface Either<A, B> {
            // https://stackoverflow.com/questions/48143268/java-tagged-union-sum-types
            <R> R either(Function<? super A, ? extends R> left
                        ,Function<? super B, ? extends R> right);
        }

    we have to make sure:
        * Either is immutable
        * dont use "instanceof"


*/

package seed.unions;

import java.util.function.Function;

public abstract class Either<A, B> {
private Either(){}

public abstract <R>
R either(Function<? super A, ? extends R> left
        ,Function<? super B, ? extends R> right);

public static <A,B,R>
R eitherS(Either<A,B> e, Function<A,R> left, Function<B,R> right){
    return e.either(left, right);
}



public final boolean is_right(){ return either((a)->false, (b)->true); }

public static <A,B> Left<A,B> mkLeft(A a){ return new Left<>(a); }
public static <A,B> Right<A,B> mkRight(B b){ return new Right<>(b); }
public Either<B,A> flip(){
    //return either((A a)->mkRight(a), (B b)->mkLeft(b)); error??
    // return eitherS(this, (A a)->mkRight(a), (B b)->mkLeft(b)); error??
    // fine:
    //Function<A, Either<B,A>> f = (A a)->mkRight(a);
    //Function<B, Either<B,A>> g = (B b)->mkLeft(b);
    Function<A, Either<B,A>> f = Either::mkRight;
    Function<B, Either<B,A>> g = Either::mkLeft;
    return either(f, g);
}


public final <R>
Either<A,R> fmap(Function<? super B, ? extends R> f){
    return fmap_right(f);
}
public final <R>
Either<A,R> fmap_right(Function<? super B, ? extends R> f){
    //return either(Either::mkLeft, (B b)->mkRight(f.apply(b))); //error??
    Function<A, Either<A,R>> g = Either::mkLeft;
    Function<B, Either<A,R>> h = (B b)->mkRight(f.apply(b));
    return either(g, h);
}
public final <R>
Either<R,B> fmap_left(Function<? super A, ? extends R> f){
    Function<A, Either<R,B>> g = (A a)->mkLeft(f.apply(a));
    Function<B, Either<R,B>> h = Either::mkRight;
    return either(g, h);
}

//////////////////////////

public static final class Left<A, B> extends Either<A, B> {
    private final A value;
    public Left(A value) { this.value = value; }

    public final <R>
    R either(Function<? super A, ? extends R> left
            ,Function<? super B, ? extends R> right){
        return left.apply(value);
    }

}//Left

public static final class Right<A, B> extends Either<A, B> {
    private final B value;
    public Right(B value) { this.value = value; }

    public final <R>
    R either(Function<? super A, ? extends R> left
            ,Function<? super B, ? extends R> right){
        return right.apply(value);
    }
}//Right

}//Either

/*
final class Right<A, B> extends Either<A, B> {
    private final B value;
    public Right(B value) { this.value = value; }

    public <R> R either(Function<? super A, ? extends R> left
                        ,Function<? super B, ? extends R> right){
        return right.apply(value);
    }
}//global.Right
*/
