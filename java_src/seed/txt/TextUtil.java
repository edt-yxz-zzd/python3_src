
package seed.txt;

import java.util.Iterator;
import java.util.regex.MatchResult;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;



public class TextUtil {

public static class PrefixesRegex{
    private Pattern regex;
    public PrefixesRegex(Iterator<String> prefixes){
        this.regex = make_prefixes_regex(prefixes);
    }

    public static String
    make_prefixes_regex_pattern(Iterator<String> prefixes){
        // "(?:<prefix0>|<prefix1>|...)"
        StringBuilder sb = new StringBuilder();
        sb.append("(?:");
        while (prefixes.hasNext()){
            sb.append(Pattern.quote(prefixes.next()));
            // bug: continue
            break;
        }
        while (prefixes.hasNext()){
            sb.append('|');
            sb.append(Pattern.quote(prefixes.next()));
        }
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


