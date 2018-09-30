package nn_ns.parsers;

import nn_ns.abc.IParser;

import java.text.ParseException;
import java.util.Arrays;
import java.util.Collection;


public abstract class IChoiceParser<T> implements IParser<T> {

public abstract Collection<String> get_choices();
protected abstract T parse_choice(String choice) throws Exception;
public final T parse(String s) throws Exception{
    final Collection<String> choices = this.get_choices();
    if (choices.contains(s))
        return this.parse_choice(s);

    String err_msg = String.format("not in %s: %s", Arrays.toString(choices.toArray()), s);
    throw new ParseException(err_msg, 0);
}

} // IChoiceParser
