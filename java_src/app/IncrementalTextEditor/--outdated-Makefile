
JC = javac
JFLAGS = -cp .
JCF = $(JC) $(JFLAGS)

all_classes = nn_ns/txt/ClipboardHandler.class nn_ns/txt/ToInputStream.class nn_ns/txt/TinyTextReadWriter.class nn_ns/txt/IncrementalTextEditor.class

default: IncrementalTextEditor.jar $(all_classes)

IncrementalTextEditor.jar: $(all_classes)
	jar cfe IncrementalTextEditor.jar nn_ns.txt.IncrementalTextEditor nn_ns
nn_ns/txt/ClipboardHandler.class: nn_ns/txt/ClipboardHandler.java
	$(JCF) nn_ns/txt/ClipboardHandler.java
nn_ns/txt/ToInputStream.class: nn_ns/txt/ToInputStream.java
	$(JCF) nn_ns/txt/ToInputStream.java
nn_ns/txt/TinyTextReadWriter.class: nn_ns/txt/TinyTextReadWriter.java
	$(JCF) nn_ns/txt/TinyTextReadWriter.java
nn_ns/txt/IncrementalTextEditor.class: nn_ns/txt/IncrementalTextEditor.java
	$(JCF) nn_ns/txt/IncrementalTextEditor.java


#no clean

