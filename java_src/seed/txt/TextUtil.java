
/*
bug1 fixed:
    PrefixesRegex
    make_prefixes_regex_pattern()
        fixed: sort the prefixes before construct regex
        #The Pattern engine performs traditional NFA-based matching with ordered alternation as occurs in Perl 5.
        # !!!!!!!!!!!!!!!!"ordered alternation"!!!!!!!!!!!!!!!!!
bug2 fixed:
    PrefixesRegex
    make_prefixes_regex_pattern()
        len(prefixes) may be 0
        using dead_regex when 0
*/
package seed.txt;

import seed.collection_util.StringUtil;
import seed.collection_util.FunctionalMapUtil;
import seed.collection_util.CollectionUtil;


import java.util.Iterator;
import java.util.regex.MatchResult;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;



public class TextUtil {
private static final Pattern dead_regex = Pattern.compile("(?:(?!1)1)");

public static class PrefixesRegex{
    private Pattern regex;
    public PrefixesRegex(Iterator<String> prefixes){
        this.regex = make_prefixes_regex(prefixes);
    }

    public static String
    make_prefixes_regex_pattern(Iterator<String> prefixes){
        // "(?:<prefix0>|<prefix1>|...)"
        prefixes = CollectionUtil.py_sorted(prefixes, true).iterator();
        if (!prefixes.hasNext()){
            return TextUtil.dead_regex.pattern();
        }

        StringBuilder sb = new StringBuilder();
        sb.append("(?:");
        if (true)
            StringUtil.join(sb, "|", FunctionalMapUtil.map(Pattern::quote, prefixes));
        else{
        sb.append(Pattern.quote(prefixes.next()));
        /*
        if (prefixes.hasNext()){
            sb.append(Pattern.quote(prefixes.next()));
            // bug: once using "while" instead of "if" and forgot "break"
        }
        */

        while (prefixes.hasNext()){
            sb.append('|');
            sb.append(Pattern.quote(prefixes.next()));
        }
        }//else

        sb.append(")");
        String pattern = sb.toString();
        return pattern;
    }

    public static Pattern
    make_prefixes_regex(Iterator<String> prefixes){
        return Pattern.compile(make_prefixes_regex_pattern(prefixes));
    }
    public String find_maybe_longest_prefix(String s){
        Matcher m = this.regex.matcher(s);
        //System.out.println(s);
        //System.out.println(regex.pattern());
        //
        //bug:if (!m.find(0)) return null;
        if (!m.lookingAt()) return null;
        //System.out.println(m.group());
        //System.out.println(s.substring(0, m.end()));
        return m.group();
        //return m.lookingAt()? m.group() : null;
    }
}
public static String find_maybe_longest_prefix(
    Iterator<String> prefixes, String s){
    return new PrefixesRegex(prefixes).find_maybe_longest_prefix(s);
}
public static String find_maybe_longest_prefix(
    PrefixesRegex prefix_regex, String s){
    return prefix_regex.find_maybe_longest_prefix(s);
}


}//TextUtil


