//TinyTextReadWriter
package nn_ns.txt;

//import java.nio.charset.StandardCharsets;
import java.nio.charset.Charset;

import java.nio.file.Path;
//import java.nio.file.Paths;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;

import java.io.IOException;

import java.io.BufferedReader;
import java.io.BufferedWriter;

import java.io.InputStream;
import java.io.Reader;
//import java.io.InputStreamReader;
//import java.io.FileInputStream;

import java.net.URI;
import java.net.URL;

import nn_ns.txt.ToInputStream;


public class TinyTextReadWriter {
private static final int len = 1024;

public static void append_txt(final boolean prefix_newline, final String txt, final Path txt_path, final Charset encoding)
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



///////////////////////////////////////////////////// Class

public static String read_txt(final Class cls, final String txt_path, final Charset encoding)
throws IOException
{
    return read_txt(ToInputStream.newInputStream(cls, txt_path), encoding);
}
public static String read_txt(final ClassLoader loader, final String txt_path, final Charset encoding)
throws IOException
{
    return read_txt(ToInputStream.newInputStream(loader, txt_path), encoding);
}
///////////////////////////////////////////////////// paths
public static String read_txt(final URI txt_path, final Charset encoding)
throws IOException
{
    return read_txt(ToInputStream.newInputStream(txt_path), encoding);
}
public static String read_txt(final URL txt_path, final Charset encoding)
throws IOException
{
    return read_txt(ToInputStream.newInputStream(txt_path), encoding);
}
public static String read_txt(final File txt_path, final Charset encoding)
throws IOException
{
    return read_txt(ToInputStream.newInputStream(txt_path), encoding);
}
public static String read_txt(final Path txt_path, final Charset encoding)
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

    try(BufferedReader fin = Files.newBufferedReader(txt_path, encoding)){
        return read_txt(fin);
    }
}




///////////////////////////////////////////////////// InputStream
public static String read_txt(final InputStream istream, final Charset encoding)
throws IOException
{
    return read_txt(ToInputStream.fromInputStream2BufferedReader(istream, encoding));
}
public static String read_txt(final Reader reader)
throws IOException
{
    return read_txt(ToInputStream.fromReader2BufferedReader(reader));
}
public static String read_txt(final BufferedReader reader)
throws IOException
{
    StringBuffer buf = new StringBuffer();
    //reader.read(buf); // StringBuffer is not CharBuffer
    char[] cbuf = new char[len];
    while (true){
        int size = reader.read(cbuf); //IOException
        if (size < 1) break;
        buf.append(cbuf, 0, size);
    }
    return buf.toString();

}


} // class TinyTextReadWriter

