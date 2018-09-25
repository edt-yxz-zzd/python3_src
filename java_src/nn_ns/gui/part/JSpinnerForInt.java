package nn_ns.gui.part;

import javax.swing.SpinnerNumberModel;
import javax.swing.SpinnerModel;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import java.awt.Component;
//import javax.swing.event.ChangeEvent;
//import javax.swing.event.ChangeListener;


public class JSpinnerForInt extends JPanel {
private final JSpinner spinner;
//int value;

public JSpinnerForInt(final String may_label_text
                    , final int initial_value
                    , final int min, final int max, final int step){
    final SpinnerModel model = new SpinnerNumberModel
        (initial_value, min, max, step);

    this.spinner = new JSpinner(model);
    //this.value = initial_value;
    //Make the number be formatted without a thousands separator.
    spinner.setEditor(new JSpinner.NumberEditor(spinner, "#"));

    if (may_label_text != null) {
        final JLabel label = new JLabel(may_label_text);
        label.setLabelFor(spinner);
        this.add(label);
    }
    this.add(spinner);


    /*
    spinner.addChangeListener(new ChangeListener(){
        public void stateChanged(ChangeEvent e) {
            System.out.println("JSpinnerForInt stateChanged:" + spinner.getValue());

            final SpinnerModel model = spinner.getModel();
            if (model instanceof SpinnerNumberModel) {
                //((SpinnerNumberModel) spinner.getModel())).getNumber().intValue();
                JSpinnerForInt.this.value = ((Number)spinner.getValue()).intValue();
            }
        }
    });
    */
}

public int getIntValue(){
    final SpinnerModel model = spinner.getModel();
    if (model instanceof SpinnerNumberModel) {
        return ((Number)spinner.getValue()).intValue();
    }
    throw new RuntimeException("spinner's model changed");
}


public static Integer askMaybeInt(
    Component parentComponent
    , final String title
    , final String may_label_text
    , final int initial_value
    , final int min, final int max, final int step){

    final JSpinnerForInt message = new JSpinnerForInt(
            may_label_text, initial_value, min, max, step);

    final int n = JOptionPane.showConfirmDialog
            (parentComponent
            ,(Object)message
            ,title
            ,JOptionPane.OK_CANCEL_OPTION
            ,JOptionPane.QUESTION_MESSAGE
            );
    if (n == JOptionPane.OK_OPTION){
        return message.getIntValue();
    }
    //bug: else if (n == 1)
    else if (n == JOptionPane.CANCEL_OPTION){
        return null;
    }
    throw new RuntimeException("unknown case: OK_CANCEL_OPTION:" + n);
}


}//class JSpinnerForInt

