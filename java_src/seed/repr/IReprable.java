package seed.repr;


public interface IReprable {
//used by Repr.append_repr

void __append_repr__(StringBuilder sb);

default String __repr__(){
    StringBuilder sb = new StringBuilder();
    __append_repr__(sb);
    return sb.toString();
}

}

