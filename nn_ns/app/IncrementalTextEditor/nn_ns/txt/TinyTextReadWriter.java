//TinyTextReadWriter
package nn_ns.txt;

import java.nio.charset.StandardCharsets;
import java.nio.charset.Charset;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.io.BufferedReader;
import java.io.BufferedWriter;

class TinyTextReadWriter {

    static void append_txt(final boolean prefix_newline, final String txt, final Path txt_path, final Charset encoding)
    throws IOException
    {
        try(BufferedWriter fout = Files.newBufferedWriter(
                txt_path, encoding
                , StandardOpenOption.CREATE
                , StandardOpenOption.APPEND
                , StandardOpenOption.WRITE
            )){
            if (prefix_newline) fout.write('\n');
            fout.write(txt);
            //out.flush();
        }
    }
    static String read_txt(final Path txt_path, final Charset encoding)
    throws IOException
    {
        /*
        StringBuffer buf = new StringBuffer();
        for (String line : Files.readAllLines(txt_path, encoding)){
            buf.append(line);
            buf.append('\n');
        }
        // bug: always "" or ".*\n", not good!!
        return buf.toString();
        */

        StringBuffer buf = new StringBuffer();
        BufferedReader fin = Files.newBufferedReader(txt_path, encoding);
        //fin.read(buf); // StringBuffer is not CharBuffer
        final int len = 1024;
        char[] cbuf = new char[len];
        while (true){
            int size = fin.read(cbuf);
            if (size < 1) break;
            buf.append(cbuf, 0, size);
        }
        return buf.toString();
    }


} // class TinyTextReadWriter

