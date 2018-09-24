javac -cp . nn_ns/txt/ClipboardHandler.java
javac -cp . nn_ns/txt/ToInputStream.java
javac -cp . nn_ns/txt/TinyTextReadWriter.java
javac -cp . nn_ns/txt/IncrementalTextEditor.java
@rem java -cp . nn_ns.txt.IncrementalTextEditor test.txt utf8 "Anonymous Pro PLAIN 24"

jar cfe IncrementalTextEditor.jar nn_ns.txt.IncrementalTextEditor nn_ns
@rem java -jar IncrementalTextEditor.jar test.txt utf8 "Anonymous Pro PLAIN 24"

