
//clipboard
//http://www.avajava.com/tutorials/lessons/how-do-i-copy-a-string-to-the-clipboard.html
//http://www.javapractices.com/topic/TopicAction.do?Id=82

package nn_ns.txt;

import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;

import java.awt.datatransfer.Transferable;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.io.IOException;


class ClipboardHandler {

static public void setClipboardContents(final String string){
    if (string == null) return;
    StringSelection stringSelection = new StringSelection(string);
    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    //clipboard.setContents(stringSelection, this);
    clipboard.setContents(stringSelection, null);
}

// -> Maybe String
static public String getClipboardContents() {
    String result = null;
    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    //odd: the Object param of getContents is not currently used
    Transferable contents = clipboard.getContents(null);
    boolean hasTransferableText =
        (contents != null) &&
        contents.isDataFlavorSupported(DataFlavor.stringFlavor)
    ;
    if (hasTransferableText) {
        try {
            result = (String)contents.getTransferData(DataFlavor.stringFlavor);
        }
        catch (UnsupportedFlavorException | IOException ex){
            ex.printStackTrace();
            System.err.println(ex);
            // return null;
        }
    }
    return result; // maybe null
}

} // class ClipboardHandler
