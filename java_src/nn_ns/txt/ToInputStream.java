//ToInputStream
package nn_ns.txt;

//import java.nio.charset.StandardCharsets;
import java.nio.charset.Charset;

import java.nio.file.Path;
//import java.nio.file.Paths;
import java.io.File;
import java.nio.file.Files;
//import java.nio.file.StandardOpenOption;

import java.io.IOException;
import java.io.FileNotFoundException;

import java.io.BufferedReader;
//import java.io.BufferedWriter;

import java.io.InputStream;
import java.io.Reader;
import java.io.InputStreamReader;
import java.io.FileInputStream;

import java.net.URI;
import java.net.URL;



public class ToInputStream {
// static newInputStream
// static newBufferedReader
// static fromInputStream2BufferedReader

public static InputStream newInputStream(final Class cls, final String path)
throws IOException
{
    InputStream may_istream = cls.getResourceAsStream(path);
    if (may_istream == null){
        throw new FileNotFoundException(String.format("Class %s/../%s", cls.getCanonicalName(), path));
    }
    return may_istream;
}

public static InputStream newInputStream(final ClassLoader loader, final String path)
throws IOException
{
    InputStream may_istream = loader.getResourceAsStream(path);
    if (may_istream == null){
        throw new FileNotFoundException(String.format("ClassLoader %s/../%s", loader.toString(), path));
    }
    return may_istream;
}

///////////////////////////////////////
public static InputStream newInputStream(final URI path)
throws IOException
{
    return newInputStream(path.toURL());
}
public static InputStream newInputStream(final URL path)
throws IOException
{
    return path.openStream();
}
public static InputStream newInputStream(final File path)
throws IOException
{
    return new FileInputStream(path);
}
public static InputStream newInputStream(final Path path)
throws IOException
{
    return Files.newInputStream(path);
}




////////////////////////////////////////////////
public static Reader fromInputStream2Reader(final InputStream istream, final Charset encoding)
{
    return new InputStreamReader(istream, encoding);
}
public static BufferedReader fromReader2BufferedReader(final Reader reader)
{
    return new BufferedReader(reader);
}
public static BufferedReader fromInputStream2BufferedReader(final InputStream istream, final Charset encoding)
{
    return fromReader2BufferedReader(fromInputStream2Reader(istream, encoding));
}



/////////////////////////////////////// newBufferedReader
public static BufferedReader newBufferedReader(final Class cls, final String path, Charset encoding)
throws IOException
{
    return fromInputStream2BufferedReader(newInputStream(cls, path), encoding);
}
public static BufferedReader newBufferedReader(final ClassLoader loader, final String path, Charset encoding)
throws IOException
{
    return fromInputStream2BufferedReader(newInputStream(loader, path), encoding);
}
public static BufferedReader newBufferedReader(final URI path, Charset encoding)
throws IOException
{
    return fromInputStream2BufferedReader(newInputStream(path), encoding);
}
public static BufferedReader newBufferedReader(final URL path, Charset encoding)
throws IOException
{
    return fromInputStream2BufferedReader(newInputStream(path), encoding);
}
public static BufferedReader newBufferedReader(final File path, Charset encoding)
throws IOException
{
    return fromInputStream2BufferedReader(newInputStream(path), encoding);
}

public static BufferedReader newBufferedReader(final Path path)
throws IOException
{
    return Files.newBufferedReader(path);
}

} // class ToInputStream


