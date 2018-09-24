package nn_ns.gui;

import nn_ns.gui.part.JSpinnerForInt;
import java.awt.Component;



public class Dialogs {

public static Integer askMaybeIntByJSpinner(
    Component parentComponent
    , final String title
    , final String may_label_text
    , final int initial_value
    , final int min, final int max, final int step){
    return JSpinnerForInt.askMaybeInt(
            parentComponent
            ,title
            ,may_label_text
            ,initial_value
            ,min, max, step
            );
}




} // public class Dialogs

