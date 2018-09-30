
package seed.collection_util;

public interface Repr{

static String repr(String s){
    return __ReprPrivate.toPrintableRepresentation(s);
}


}// Repr


class __ReprPrivate{
// https://stackoverflow.com/questions/1350397/java-equivalent-of-python-repr
private static final char CONTROL_LIMIT = ' ';
private static final char PRINTABLE_LIMIT = '\u007e';
private static final char[] HEX_DIGITS = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };

public static String toPrintableRepresentation(String source) {

    if( source == null ) return null;
    else {

        final StringBuilder sb = new StringBuilder();
        final int limit = source.length();
        char[] hexbuf = null;

        int pointer = 0;

        sb.append('"');

        while( pointer < limit ) {

            int ch = source.charAt(pointer++);

            switch( ch ) {

            case '\0': sb.append("\\0"); break;
            case '\t': sb.append("\\t"); break;
            case '\n': sb.append("\\n"); break;
            case '\r': sb.append("\\r"); break;
            case '\"': sb.append("\\\""); break;
            case '\\': sb.append("\\\\"); break;

            default:
                if( CONTROL_LIMIT <= ch && ch <= PRINTABLE_LIMIT ) sb.append((char)ch);
                else {

                    sb.append("\\u");

                    if( hexbuf == null )
                        hexbuf = new char[4];

                    for( int offs = 4; offs > 0; ) {

                        hexbuf[--offs] = HEX_DIGITS[ch & 0xf];
                        ch >>>= 4; 
                    }

                    sb.append(hexbuf, 0, 4);
                }
            }
        }

        return sb.append('"').toString();
    }
}

} // __ReprPrivate



