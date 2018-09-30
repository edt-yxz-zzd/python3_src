/*

cli:
    <exe> -i=<input> -e=<encoding> -h
    no positional parameters
    each arg in java.main.args (i.e. c.main.argv[1:])
        should be "{prefix}{value}"
        e.g.
            arg="-e=utf8"
                prefix="-e="
                value="utf8"

            arg="-h"
                prefix="-h"
                value=""
        donot support "-e:utf8", "-e utf8" or [..."-e","utf8"...]


parse_all_prefixed_arguments
    :: [String]
    -> {String:String}
    -> {String:(Maybe String, String->Object, String)}
    -> (override=Bool)
    -> ({String:Object}, [String])

    # may_default==null ==>> required
    :: args
    -> {prefix:option_name}
    -> {option_name:(may_default, parser, help)}
    -> (override=false)
    -> ({prefix:result}, remaining_args)

e.g.
    arg_str = "{prefix}{arg}"
        match the longest prefix
    prefix = "--encoding=" | "-e"
    option_name = "encoding"
    override=true ==>> prefix can occur at most once

*/
package nn_ns.cli.argparser;

import seed.tuples.Pair;        // fst
import seed.collection_util.CollectionUtil;
import seed.collection_util.Repr;
import nn_ns.abc.IParser;
import nn_ns.parsers.IChoiceParser;

import java.util.Collections; // unmodifiableMap,  binarySearch
import java.util.Iterator;
//import java.util.Comparator;
import java.util.ArrayList;
import java.util.Map;
//import java.util.TreeMap;
import java.util.HashMap;
import java.util.TreeSet;

public interface ParseAllPrefixedArguments{


public static OptionArgs
mkOptionArgs(String may_default, IParser<?> parser, String help){
    return new OptionArgs(may_default, parser, help);
}
public static class OptionArgs {
    final String may_default;
    final IParser<?> parser;
    final String help;

    public OptionArgs(String may_default, IParser<?> parser, String help){
        this.may_default = may_default;
        this.parser = parser;
        this.help = help;
    }
}
public static class ParseAllPrefixedArgumentsException extends Exception {
    public ParseAllPrefixedArgumentsException() { super(); }
    public ParseAllPrefixedArgumentsException(String message) { super(message); }
    public ParseAllPrefixedArgumentsException(String message, Throwable cause) { super(message, cause); }
    public ParseAllPrefixedArgumentsException(Throwable cause) { super(cause); }
}

public static String
make_help_string
    (Map<String, String>
        prefix2option_name
    ,Map<String, OptionArgs>
        option_name2option_args
    ,String description
    )throws ParseAllPrefixedArgumentsException{
    Map<String, ArrayList<String>>
        option_name2prefixes = make_option_name2prefixes(prefix2option_name);

    // require sorted to show
    TreeSet<String> option_names
        = new TreeSet<>(option_name2prefixes.keySet());
    if (!option_name2option_args.keySet().containsAll(option_names)){
        option_names.removeAll(option_name2option_args.keySet());
        assert !option_names.isEmpty();
        throw new ParseAllPrefixedArgumentsException(String.format(
            "option_name2option_args miss option_names: %s"
            ,option_names));
    }

    StringBuilder help = new StringBuilder();
    String indent = "\t";
    String endl = "\n";

    CollectionUtil.appendln(help, "Description:");
    CollectionUtil.appendln(help, indent, description);
    CollectionUtil.appendln(help);

    CollectionUtil.appendln(help, "Options:");
    for (String option_name : option_names){
        ArrayList<String> prefixes
            = option_name2prefixes.get(option_name);
        OptionArgs option_args
            = option_name2option_args.get(option_name);

        if (null==option_args.may_default) {
            CollectionUtil.append(help, indent, option_name); // no endl
        }
        else {
            String default_result_str = option_args.may_default;
            String s = String.format("%s=%s"
                , option_name, Repr.repr(default_result_str));
            CollectionUtil.append(help, indent, s); // no endl
        }

        if (option_args.parser instanceof IChoiceParser){
            IChoiceParser parser = (IChoiceParser)option_args.parser;
            CollectionUtil.append(help, " from ", parser.get_choices());
        }
        help.append(endl);

        CollectionUtil.append(help, indent, indent, prefixes, endl);
        CollectionUtil.append(help, indent, indent, "# ", option_args.help, endl);
    }
    return help.toString();
}



public static Map<String, ArrayList<String>>
make_option_name2prefixes(Map<String, String> prefix2option_name){
    HashMap<String, ArrayList<String>>
        option_name2prefixes = new HashMap<>();

    prefix2option_name.forEach((prefix, option_name) -> {
        ArrayList<String> prefixes =
            option_name2prefixes.computeIfAbsent(option_name, (name)->
                new ArrayList<>()
            );
        prefixes.add(prefix);
    });
    return option_name2prefixes;
}

public static
Pair<Map<String, Object>, ArrayList<String>>
parse_all_prefixed_arguments
    (Iterator<String>
        args
    ,Map<String, String>
        prefix2option_name
    ,Map<String, OptionArgs>
        option_name2option_args
    ,boolean override
    ) throws Exception {
    /*
    TreeMap<String, String> _prefix2option_name_ =
        // to avoid non-natural-ordering
        //  TreeMap(Map) not TreeMap(SortedMap)
        new TreeMap<>(prefix2option_name);
        prefix2option_name = null;
    ArrayList<String> _args_ = CollectionUtil.py_sorted(args, false);
        args = null;

    final ArrayList<String> sorted_prefixes = CollectionUtil
            .mkArrayList(_prefix2option_name_.keySet());
    */

    final ArrayList<String> sorted_prefixes = CollectionUtil
            .py_sorted(prefix2option_name.keySet().iterator(), false);

    ArrayList<String> remaining_args = new ArrayList<>();
    Map<String, Object> option_name2result = new HashMap<>();

    // bug: for (String arg : args) # iterator not in "for"
    // args.forEachRemaining(arg -> # action donot throw
    // for (String arg : CollectionUtil.mkArrayList(args))
    CollectionUtil.forEachExc(args, arg -> {
        int i = Collections.binarySearch(sorted_prefixes, arg);
        if (i >= 0)
            // good
            ;
        else {
            final int insert_point = -i-1;
            i = -1;
            // assert 0 <= insert_point <= sorted_prefixes.size();
            if (insert_point == 0)
                // bad
                ;
            else if (arg.startsWith(sorted_prefixes.get(insert_point-1)))
                // good
                i = insert_point-1;
            else
                // bad
                ;
        }

        if (i < 0){
            // bad
            remaining_args.add(arg);
        }
        else {
            // good
            assert arg.startsWith(sorted_prefixes.get(i));
            // maybe arg.startsWith(sorted_prefixes[i-1]);
            // but we find the longest prefix
            final String prefix = sorted_prefixes.get(i);
            final String option_name = prefix2option_name.get(prefix);
            if (!override && option_name2result.containsKey(option_name)){
                throw new ParseAllPrefixedArgumentsException(
                    String.format("option_name:\"%s\" ocurr more than once in arguments"
                    ,option_name));
            }

            final OptionArgs
                    option_args = option_name2option_args.get(option_name);
            final String result_str = arg.substring(prefix.length());
            Object result = option_args.parser.parse(result_str);
            option_name2result.put(option_name, result);
        }
    }); // for arg in args

    if (option_name2result.size() != option_name2option_args.size()){
        // eval omit option_name by default string
        //
        // option_name2option_args.forEach((option_name, option_args) ->
        //for (Map.Entry<String, OptionArgs>
        //    item : option_name2option_args.entrySet()){
        //    final String option_name = item.getKey();
        //    final OptionArgs
        //            option_args = item.getValue();
        //    item = null;
        CollectionUtil.forEachExc(option_name2option_args
            , (option_name, option_args) -> {
            ///////////////////
            if (option_name2result.containsKey(option_name))
                //continue;
                return;
            final String may_default = option_args.may_default;
            if (may_default == null){
                throw new ParseAllPrefixedArgumentsException(
                    String.format(
                        "option_name:\"%s\" is required! but does not ocurr."
                        ,option_name));
            }

            final String default_result_str = may_default;
            Object result = option_args.parser.parse(default_result_str);
            option_name2result.put(option_name, result);
        });
    }

    //return Pair.mk(option_name2result, remaining_args);
    return new Pair<>(option_name2result, remaining_args);
}



}//class ParseAllPrefixedArguments

