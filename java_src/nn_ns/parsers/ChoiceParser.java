package nn_ns.parsers;

import nn_ns.abc.IParser;
import nn_ns.parsers.IChoiceParser;

import java.text.ParseException;
import java.util.Arrays;
import java.util.Collection;

public class ChoiceParser<T> extends IChoiceParser<T> {
    private final IParser<T> parser;
    private final Collection<String> choices;
public ChoiceParser(IParser<T> parser, Collection<String> choices){
    this.parser = parser;
    this.choices = choices;
}
public Collection<String> get_choices(){
    return this.choices;
}
protected T parse_choice(String choice) throws Exception{
    return this.parser.parse(choice);
}


} // ChoiceParser
