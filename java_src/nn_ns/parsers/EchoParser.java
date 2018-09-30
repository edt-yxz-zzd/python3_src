package nn_ns.parsers;

import nn_ns.abc.IParser;


public class EchoParser implements IParser<String> {

//public EchoParser(){}
public String parse(String s) throws Exception{
    return s;
}


} // EchoParser
