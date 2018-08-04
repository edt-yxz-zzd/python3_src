/*
    1) arg = [decrypt|encrypt], but they are not distinguishable for RC4

    2) input two lines (many times)
        each line encode bytes as hexdigits in uppercase
        first for key
        second for cleartext
        output a hexdigit line as hex encoded ciphertext

example:
    let key = '121212ABAB'
    let text = 'EFEF343434ACAC'
    then output = '6AA017E18F9BC2'
    let key = '1212121212'
    let text = '11'
    then output = '6C'
    assume current directory contains RC4.class
    > java -cp .. subprog.RC4_bat decrypt
    121212ABAB
    EFEF343434ACAC
    6AA017E18F9BC2
    1212121212
    11
    6C
    121212ABAB
    EFEF343434ACAC
    6AA017E18F9BC2
    ^Z<enter>

*/


package subprog;
import subprog.RC4;
import javax.crypto.Cipher;
import java.security.NoSuchAlgorithmException;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.util.NoSuchElementException;

import java.util.Scanner;
import java.util.Arrays;
import java.math.BigInteger;

public class RC4_bat extends RC4 {
    public static void main(String[] args) { //try{// throws Exception {
try{
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
        String key_str = null;
        String ciphertext_str = null;
        Cipher c = Cipher.getInstance("RC4");
    while (in.hasNextLine()){
        key_str = null;
        ciphertext_str = null;
        try {
            key_str = in.nextLine();
            ciphertext_str = in.nextLine();
        }
        catch (NoSuchElementException e){
            if (key_str == null){
                System.exit(0); return;
            }
            throw new Exception("key without data", e);
        }
        assert key_str != null;
        assert ciphertext_str != null;


        try {
            Key key = new SecretKeySpec(decodeFromHex(key_str), "RC4");
            byte[] ciphertext = decodeFromHex(ciphertext_str);
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
            e.printStackTrace(System.err);
            print_err(e);
            print_err("key:", key_str);
            print_err("text:", ciphertext_str);
            System.exit(2); return;
        }
    }
        /* */
        System.exit(0); return;
} catch (Exception e){
    e.printStackTrace(System.err);
    print_err(e);
    System.exit(3); return;
} // end try-catch
    } // end main
} // end class

