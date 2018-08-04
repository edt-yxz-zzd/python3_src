/*
    1) arg = [decrypt|encrypt], but they are not distinguishable for RC4

    2) input two lines
        each line encode bytes as hexdigits in uppercase
        first for key
        second for cleartext
        output a hexdigit line as hex encoded ciphertext

example:
    let key = '121212ABAB'
    let text = 'EFEF343434ACAC'
    then output = '6AA017E18F9BC2'
    assume current directory contains RC4.class
    > java -cp .. subprog.RC4 decrypt
    121212ABAB
    EFEF343434ACAC
    6AA017E18F9BC2

*/


package subprog;
import javax.crypto.Cipher;
import java.security.NoSuchAlgorithmException;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;


import java.util.Scanner;
import java.util.Arrays;
import java.math.BigInteger;

public class RC4 {
    static void println(Object... ss){
        for (Object s : ss)
            System.out.println(s);
    }
    static void print(Object... ss){print_(System.out, ss);}
    static void print_err(Object... ss){print_(System.err, ss);}
    static void print_(java.io.PrintStream out, Object... ss){
        for (Object s : ss){
            out.print(s);
            out.print("  ");
        }
        out.println();
    }

    public static <T> int len(T[] bs){
        return bs.length;
    }
    public static int len(byte[] bs){
        return bs.length;
    }
    public static int len(String s){
        return s.length();
    }
    public static String encodeToHex(byte[] bs){
        // Note: cleartext is byte[]; ciphertext is String!!
        byte[] bs1 = new byte[len(bs)+1];
        bs1[0] = 1;
        System.arraycopy(bs, 0, bs1, 1, len(bs));
        BigInteger i = new BigInteger(bs1);
        String hex = i.toString(16).substring(1).toUpperCase();
        if (len(hex) % 2 != 0)
            hex = "0" + hex;
        return hex;
    }
    public static byte[] decodeFromHex(String s) throws Exception{
        if (len(s) % 2 != 0)
            throw new Exception("decodeFromHex: len(string) % 2 != 0");
        BigInteger i = new BigInteger("1" + s, 16);
        byte[] bs = i.toByteArray();
        assert (len(bs) - 1)*2 == len(s);
        byte[] _bs = Arrays.copyOfRange(bs, 1, len(bs));
        return _bs;
    }
    public static void main(String[] args){
        // System.out.println("");
        // print(java.nio.charset.Charset.availableCharsets().keySet());
        //*
        //
        // println(args);
        boolean b = true;
        int mode = -1;
        if (len(args) != 1) b = false;
        // bug: ".equals" instead of "=="
        //  else if (args[0] == "decrypt") mode = Cipher.DECRYPT_MODE;
        else if (args[0].equals("decrypt")) mode = Cipher.DECRYPT_MODE;
        else if (args[0].equals("encrypt")) mode = Cipher.ENCRYPT_MODE;
        else b = false;
        if (! b) {
            print("usage: " +
                "call \"RC4 [decrypt|encrypt]\" and input 2 lines" +
                "(one line for key and another for cleartext" +
                ", both hex-encoded, uppercase)"
                );
            System.exit(1);
            return;
        }
        Scanner in = new Scanner(System.in);
        String key_str = in.nextLine();
        String ciphertext_str = in.nextLine();
        try {
            Key key = new SecretKeySpec(decodeFromHex(key_str), "RC4");
            byte[] ciphertext = decodeFromHex(ciphertext_str);
            Cipher c = Cipher.getInstance("RC4");
            // if (c == null) println("fail"); else print("success");
            c.init(mode, key);
            byte[] cleartext = c.doFinal(ciphertext);
            System.out.println(encodeToHex(cleartext));
            /*
            c.init(Cipher.ENCRYPT_MODE, key);
            byte[] cleartext2 = c.doFinal(ciphertext);
            c.init(Cipher.DECRYPT_MODE, key);
            byte[] cleartext3 = c.doFinal(ciphertext);
            assert cleartext2 == cleartext3;
            /* */
        } catch (Exception e){
            print_err(e);
            print_err("key:", key_str);
            print_err("text:", ciphertext_str);
            System.exit(2);
            return;
        }
        /* */
        System.exit(0);
        return;
    }
}

