call set_JAVA_SRC_ROOT
javac -cp %JAVA_SRC_ROOT% %JAVA_SRC_ROOT%/nn_ns/txt/ClipboardHandler.java
javac -cp %JAVA_SRC_ROOT% %JAVA_SRC_ROOT%/nn_ns/txt/ToInputStream.java
javac -cp %JAVA_SRC_ROOT% %JAVA_SRC_ROOT%/nn_ns/txt/TinyTextReadWriter.java
javac -cp %JAVA_SRC_ROOT% %JAVA_SRC_ROOT%/nn_ns/txt/IncrementalTextEditor.java
@rem java -cp %JAVA_SRC_ROOT% nn_ns.txt.IncrementalTextEditor test.txt utf8 "Anonymous Pro PLAIN 24"

jar cfe IncrementalTextEditor.jar nn_ns.txt.IncrementalTextEditor %JAVA_SRC_ROOT%/nn_ns
@rem java -jar IncrementalTextEditor.jar test.txt utf8 "Anonymous Pro PLAIN 24"

