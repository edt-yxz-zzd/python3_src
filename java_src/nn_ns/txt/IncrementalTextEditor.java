/*
IncrementalTextEditor

command:
    IncrementalTextEditor -i <text_fname> -e <encoding> --fonts <fonts> -bg <color> -fg <color>

    root/nn_ns/txt>javac -cp ../.. ClipboardHandler.java
    root/nn_ns/txt>javac -cp ../.. TinyTextReadWriter.java
    root/nn_ns/txt>javac -cp ../.. IncrementalTextEditor.java
    root/nn_ns/txt>java -cp ../.. nn_ns.txt.IncrementalTextEditor ../../test.txt utf8 "Anonymous Pro PLAIN 24"

    root>javac -cp . nn_ns/txt/ClipboardHandler.java
    root>javac -cp . nn_ns/txt/ToInputStream.java
    root>javac -cp . nn_ns/txt/TinyTextReadWriter.java
    root>javac -cp . nn_ns/txt/IncrementalTextEditor.java
    root>java -cp . nn_ns.txt.IncrementalTextEditor test.txt utf8 "Anonymous Pro PLAIN 24"

    root>jar cfe IncrementalTextEditor.jar nn_ns.txt.IncrementalTextEditor nn_ns
    root>java -jar IncrementalTextEditor.jar test.txt utf8 "Anonymous Pro PLAIN 24"

window:
    |-----------------------|
    |                 _ O X |
    |-----------------------|
    | File | Edit           |
    |-----------------------|
    |  -------------------  |
    | |                   | |
    | | Area to show file | |
    | | text (saved text) | |
    | |                   | |
    |  -------------------  |
    |  -------------------  |
    | |                   | |
    | | Area to show      | |
    | | editting text     | |
    | |                   | |
    |  -------------------  |
    |-----------------------|

menu:
    File
        Save
        Quit
        Save & Quit
        Quit without Save
    Edit
        Copy
        Cut
        Paste
        ----------          # JMenu::addSeparator()
        Select All
    Font
        Choose Font Family  # -> JOptionPane.showInputDialog
        Font Style
            PLAIN           # -> JRadioButtonMenuItem+ButtonGroup
            BOLD            # -> JRadioButtonMenuItem::setSelected(true)
            ITALIC
            BOLD+ITALIC
                            #"PLAIN", "BOLD", "BOLDITALIC", or "ITALIC"
        Choose Font Size    # -> JOptionPane.showConfirmDialog(message=JSpinner)


*/

package nn_ns.txt;

import nn_ns.txt.ClipboardHandler;
import nn_ns.txt.TinyTextReadWriter;
import nn_ns.gui.Dialogs;

import nn_ns.cli.argparser.PrefixedArgumentsParser;
import static nn_ns.cli.argparser.PrefixedArgumentsParser.mkOptionArgs;
import static nn_ns.cli.argparser.PrefixedArgumentsParser.make_help_string;
import static nn_ns.cli.argparser.PrefixedArgumentsParser.OptionArgs;
import static nn_ns.cli.argparser.PrefixedArgumentsParser.ParseAllPrefixedArgumentsException;

import nn_ns.parsers.EchoParser;
import nn_ns.parsers.ChoiceParser;
import nn_ns.abc.IParser;
//import seed.collection_util.CollectionUtil;//to_iterator
import seed.collection_util.PairsBuilder;
import seed.tuples.Pair;


import java.awt.*;
import javax.swing.*;
import java.io.*;
import java.awt.event.*;
import javax.swing.plaf.metal.*;
import javax.swing.text.*;

import java.nio.charset.StandardCharsets;
import java.nio.charset.Charset;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;
//import java.nio.file.Files;
//import java.nio.file.StandardOpenOption;

import java.awt.Font; // decode
import java.awt.GraphicsEnvironment;
import java.awt.Color;

import javax.swing.JOptionPane;


import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;



public class IncrementalTextEditor extends JFrame
    implements ActionListener
    //, PrefixedArgumentsParser
    //  //can access to its static classes!!
    //  //cannot access to its static methods!!
{
    // Text component
    JTextArea area_to_show;
        // does_scroll_to_last_row
        //
        // getCaretPosition
        // setCaretPosition
        // moveCaretPosition ==>> select text
        // modelToView
    JTextArea area_to_edit;
    JTextArea saved_last_focus_area;
    Font _font;
    final boolean does_scroll_to_last_row;

    // Frame
    JFrame frame;

    // File
    Path _txt_path;
    Charset _encoding;

    // constant colors
    static final Color color_PeachPuff = new Color(0xFFDAB9);
    static final Color color_Peach = new Color(0xFFE5B4);
    static final Color color_show_bg = color_PeachPuff;
    static final Color color_show_fg = Color.BLACK;
    static final Color color_edit_bg = Color.GRAY.brighter();
    static final Color color_edit_fg = Color.BLACK;

    // constant strings
    static final String str_File = "File";
    static final String str_Edit = "Edit";
    static final String str_Font = "Font";

    static final String str_Save = "Save";
    static final String str_Quit = "Quit";
    static final String str_SaveAndQuit = "Save & Quit";
    static final String str_QuitWithoutSave = "Quit without Save";

    static final String str_Cut = "Cut";
    static final String str_Copy = "Copy";
    static final String str_Paste = "Paste";
    static final String str_SelectAll = "Select All";

    static final String str_ChooseFontFamily = "Choose Font Family";
    static final String str_FontStyle = "Font Style";
        static final String str_style_prefix = "style ";
        static final String str_style_PLAIN = "style PLAIN";
        static final String str_style_BOLD = "style BOLD";
        static final String str_style_ITALIC = "style ITALIC";
        static final String str_style_BOLDITALIC = "style BOLD+ITALIC";
    static final String str_ChooseFontSize = "Choose Font Size";

    JMenuBar make_menu()
    {
        JMenuBar menu_bar = new JMenuBar();

        // Create menu for menu
        JMenu menu_File = new JMenu(str_File);
        JMenu menu_Edit = new JMenu(str_Edit);
        JMenu menu_Font = new JMenu(str_Font);

        // Create menu items
        JMenuItem menu_item_Save = new JMenuItem(str_Save);
        JMenuItem menu_item_Quit = new JMenuItem(str_Quit);
        JMenuItem menu_item_SaveAndQuit = new JMenuItem(str_SaveAndQuit);
        JMenuItem menu_item_QuitWithoutSave = new JMenuItem(str_QuitWithoutSave);

        JMenuItem menu_item_Cut = new JMenuItem(str_Cut);
        JMenuItem menu_item_Copy = new JMenuItem(str_Copy);
        JMenuItem menu_item_Paste = new JMenuItem(str_Paste);
        JMenuItem menu_item_SelectAll = new JMenuItem(str_SelectAll);

        // menu structure
        menu_bar.add(menu_File);
        menu_bar.add(menu_Edit);
        menu_bar.add(menu_Font);

        menu_File.add(menu_item_Save);
        menu_File.add(menu_item_Quit);
        menu_File.add(menu_item_SaveAndQuit);
        menu_File.add(menu_item_QuitWithoutSave);

        menu_Edit.add(menu_item_Cut);
        menu_Edit.add(menu_item_Copy);
        menu_Edit.add(menu_item_Paste);
        menu_Edit.addSeparator();
        menu_Edit.add(menu_item_SelectAll);

        // menu listeners
        menu_item_Save.addActionListener(this);
        menu_item_Quit.addActionListener(this);
        menu_item_SaveAndQuit.addActionListener(this);
        menu_item_QuitWithoutSave.addActionListener(this);
        menu_item_Cut.addActionListener(this);
        menu_item_Copy.addActionListener(this);
        menu_item_Paste.addActionListener(this);
        menu_item_SelectAll.addActionListener(this);

        // Font
        /*
        // too many fonts!!
        for (String font_name : GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames()){
            JMenuItem menu_item = new JMenuItem(font_name);
            menu_Font.add(menu_item);
            menu_item.addActionListener(this);
        }
        */

        /*
        HashMap<Character, ArrayList<String> > initial_char2font_names = new HashMap<Character, ArrayList<String> >();
        for (String font_name : GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames()){
            if (font_name.isEmpty()){
                System.err.println("font_name.isEmpty()!!");
                continue;
            }
            Character ch = font_name.charAt(0);
            if (!initial_char2font_names.containsKey(ch))
                initial_char2font_names.put(ch, new ArrayList<String>());
            ArrayList<String> font_names = initial_char2font_names.get(ch);
            font_names.add(font_name);
        }

        for (final Map.Entry<Character, ArrayList<String> > pair : initial_char2font_names.entrySet()){
            final String submenu_name = pair.getKey().toString();
            final ArrayList<String> font_names = pair.getValue();
            JMenu submenu = new JMenu(submenu_name);
            menu_Font.add(submenu);
            for (final String font_name : font_names){
                JMenuItem menu_item = new JMenuItem(font_name);
                submenu.add(menu_item);
                menu_item.addActionListener(this);
            }
        }
        */

        JMenuItem menu_item_ChooseFontFamily = new JMenuItem(str_ChooseFontFamily);
        JMenu submenu_FontStyle = new JMenu(str_FontStyle);
            JRadioButtonMenuItem menu_item_style_PLAIN
                = new JRadioButtonMenuItem(str_style_PLAIN);
            JRadioButtonMenuItem menu_item_style_BOLD
                = new JRadioButtonMenuItem(str_style_BOLD);
            JRadioButtonMenuItem menu_item_style_ITALIC
                = new JRadioButtonMenuItem(str_style_ITALIC);
            JRadioButtonMenuItem menu_item_style_BOLDITALIC
                = new JRadioButtonMenuItem(str_style_BOLDITALIC);
        JMenuItem menu_item_ChooseFontSize = new JMenuItem(str_ChooseFontSize);

        menu_Font.add(menu_item_ChooseFontFamily);
        menu_Font.add(submenu_FontStyle);
            submenu_FontStyle.add(menu_item_style_PLAIN);
            submenu_FontStyle.add(menu_item_style_BOLD);
            submenu_FontStyle.add(menu_item_style_ITALIC);
            submenu_FontStyle.add(menu_item_style_BOLDITALIC);
        menu_Font.add(menu_item_ChooseFontSize);

        ButtonGroup group_FontStyle = new ButtonGroup();
            group_FontStyle.add(menu_item_style_PLAIN);
            group_FontStyle.add(menu_item_style_BOLD);
            group_FontStyle.add(menu_item_style_ITALIC);
            group_FontStyle.add(menu_item_style_BOLDITALIC);

        menu_item_ChooseFontFamily.addActionListener(this);
        menu_item_ChooseFontSize.addActionListener(this);

        menu_item_style_PLAIN.addActionListener(this);
        menu_item_style_BOLD.addActionListener(this);
        menu_item_style_ITALIC.addActionListener(this);
        menu_item_style_BOLDITALIC.addActionListener(this);


        // selected style
        final int style = this._font.getStyle();
        JRadioButtonMenuItem selected = null;
        switch (style){
        case Font.PLAIN: selected = menu_item_style_PLAIN; break;
        case Font.BOLD: selected = menu_item_style_BOLD; break;
        case Font.ITALIC: selected = menu_item_style_ITALIC; break;
        case Font.BOLD+Font.ITALIC: selected = menu_item_style_BOLDITALIC; break;
        default:
            throw new RuntimeException("unknown style:" + style);
        }
        selected.setSelected(true);
        return menu_bar;
    }

    void set_look_and_feel()
    {
        try {
            // Set metl look and feel
            UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");

            // Set theme to ocean
            MetalLookAndFeel.setCurrentTheme(new OceanTheme());
        }
        catch (Exception e) {
        }
    }

    void setTextFont(Font font)
    {
        this._font = font;
        area_to_show.setFont(font);
        area_to_edit.setFont(font);
        //frame.revalidate();
        //frame.repaint();
    }

    // Constructor
    IncrementalTextEditor(
        final Path txt_path
        , final Charset encoding, final Font font
        , final boolean does_scroll_to_last_row)
    throws IOException
    {
        this.does_scroll_to_last_row = does_scroll_to_last_row;
        init(txt_path.normalize().toString(), font);
        open(txt_path, encoding);
    }
    void init(final String title, final Font font)
    {
        // Create a frame
        this.frame = new JFrame(title);

        this.set_look_and_feel();

        // Text component
        this.area_to_show = new JTextArea(250, 500);
        this.area_to_edit = new JTextArea(250, 500);
        this.saved_last_focus_area = null;

        JScrollPane scroll_panel_to_show = new JScrollPane(area_to_show);
        area_to_show.setEditable(false);

        JScrollPane scroll_panel_to_edit = new JScrollPane(area_to_edit);
        area_to_edit.setEditable(true);

        area_to_show.setBackground(color_show_bg);
        area_to_show.setForeground(color_show_fg);
        area_to_edit.setBackground(color_edit_bg);
        area_to_edit.setForeground(color_edit_fg);
        this.setTextFont(font); // before make_menu!

        assert area_to_show.isFocusable();
        FocusAdapter aFocusAdapter = new FocusAdapter(){
            public void focusGained(FocusEvent e){
                IncrementalTextEditor.this.saved_last_focus_area
                    = (JTextArea)e.getComponent();
            }
        };
        area_to_show.addFocusListener(aFocusAdapter);
        area_to_edit.addFocusListener(aFocusAdapter);

        // Create a menubar
        JMenuBar menu_bar = this.make_menu();

        // frame structure
        frame.setJMenuBar(menu_bar);

        // Container panel = this.getContentPane();
        JPanel panel = new JPanel(); frame.add(panel);
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.add(scroll_panel_to_show);
        //panel.add(new JButton("sfa"));
        panel.add(scroll_panel_to_edit);



        // set normal size
        frame.setSize(500, 500);
        // fullscreen
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        // frame.setUndecorated(true);

        // frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setVisible(true);

        // after frame.setVisible
        area_to_edit.requestFocusInWindow();
    }

    void open(final Path txt_path, final Charset encoding)
    throws IOException
    {
        try {
            final String txt = TinyTextReadWriter.read_txt(txt_path, encoding);
            area_to_show.setText(txt);
            area_to_edit.setText("");
            assert area_to_show.getText().equals(txt);
        }
        catch (IOException e){
            on_QuitWithoutSave();
            throw e;
        }
        assert area_to_show.getCaretPosition() == 0;
        if (this.does_scroll_to_last_row)
            area_to_show.setCaretPosition(area_to_show.getText().length());

        this._txt_path = txt_path;
        this._encoding = encoding;
        update_font_family(this._font.getFamily());
    }

    public void actionPerformed(ActionEvent e)
    {
        final String s = e.getActionCommand();

        if (s.equals(str_Save))
            this.on_Save();
        else if (s.equals(str_Quit))
            this.on_Quit();
        else if (s.equals(str_SaveAndQuit))
            this.on_SaveAndQuit();
        else if (s.equals(str_QuitWithoutSave))
            this.on_QuitWithoutSave();
        else if (s.equals(str_Cut))
            this.on_Cut();
        else if (s.equals(str_Copy))
            this.on_Copy();
        else if (s.equals(str_Paste))
            this.on_Paste();
        else if (s.equals(str_SelectAll))
            this.on_SelectAll();
        else if (s.equals(str_ChooseFontFamily))
            this.on_ChooseFontFamily();
        else if (s.equals(str_ChooseFontSize))
            this.on_ChooseFontSize();
        else if (s.startsWith(str_style_prefix))
            this.on_ChooseFontStyle(s);
        else {
            System.err.println("logic error: menu event: " + s);
            assert "logic error".isEmpty();
            return;
            // font
            //System.err.println("font_name: " + s);
            //final String font_name = s;
            //update_font_family(font_name);
        }

    }

    void update_font_family(final String maybe_font_name){
        if (maybe_font_name == null) return;
        final String font_name = maybe_font_name;
        final Font new_font = new Font(font_name, this._font.getStyle(), this._font.getSize());

        //System.err.println(font_name);
        //System.err.println(new_font.getFamily());
        //bug: if (new_font.getFamily() == font_name)
        if (new_font.getFamily().equals(font_name)) {
            // new_font may be "Dialog" if font_name not exists
            this.setTextFont(new_font);
            //System.err.println("here");
        }
    }
    void update_font_style(final int style){
        if (this._font.getStyle() == style) return;
        this.setTextFont(this._font.deriveFont(style));
    }
    void update_font_size(final float size){
        if (this._font.getSize2D() == size) return;
        this.setTextFont(this._font.deriveFont(size));
    }

    void on_Save()
    {
        final String new_txt = area_to_edit.getText();
        if (new_txt.isEmpty()) return;

        final String old_txt = area_to_show.getText();
        final boolean prefix_newline = !old_txt.isEmpty() && (old_txt.charAt(old_txt.length()-1) != '\n');
        final Path txt_path = this._txt_path;
        final Charset encoding = this._encoding;

        try {
            TinyTextReadWriter.append_txt(prefix_newline, new_txt, txt_path, encoding);
            //TinyTextReadWriter.append_txt(true, new_txt, txt_path, encoding);
        }
        catch (IOException e){
            e.printStackTrace();
            System.err.println("fail to append text");
            JOptionPane.showMessageDialog
                (frame
                ,"fail to append text."
                ,"Error"
                ,JOptionPane.ERROR_MESSAGE
                );
            return;
        }

        try {
            open(txt_path, encoding); // reopen
        }
        catch (IOException e){
            e.printStackTrace();
            System.err.println("fail to reopen text");
            JOptionPane.showMessageDialog
                (frame
                ,"fail to reopen text."
                ,"Error"
                ,JOptionPane.ERROR_MESSAGE
                );
            //on_QuitWithoutSave();
            return; // user may copy text to another file
        }

    }
    void on_Quit(){
        frame.dispatchEvent(new WindowEvent(frame, WindowEvent.WINDOW_CLOSING));
    }
    void on_SaveAndQuit(){
        on_Save();
        on_QuitWithoutSave();
    }
    void on_QuitWithoutSave(){
        frame.dispose();
    }
    void on_Cut(){
        if (area_to_edit != saved_last_focus_area) return;
        final String txt = area_to_edit.getSelectedText();
        if (txt == null) return;

        ClipboardHandler.setClipboardContents(txt);
        area_to_edit.requestFocusInWindow();
        area_to_edit.replaceSelection("");
    }
    void on_Copy(){
        /*
        System.err.println(area_to_edit.isFocusOwner());
        System.err.println(area_to_show.isFocusOwner());
        //both not focus

        String txt = null;
        if (area_to_edit.isFocusOwner())
            txt = area_to_edit.getSelectedText();
        else if (area_to_show.isFocusOwner())
            txt = area_to_show.getSelectedText();
        else
            return;
        */
        if (saved_last_focus_area == null) return;
        final String txt = saved_last_focus_area.getSelectedText();

        if (txt == null) return; // getSelectedText() -> Maybe String
        ClipboardHandler.setClipboardContents(txt);
        saved_last_focus_area.requestFocusInWindow();
    }
    void on_Paste(){
        final String txt = ClipboardHandler.getClipboardContents();
        if (txt == null) return;
        area_to_edit.requestFocusInWindow();
        area_to_edit.replaceSelection(txt);
    }
    void on_SelectAll(){
        area_to_edit.requestFocusInWindow();
        area_to_edit.selectAll();
    }
    void on_ChooseFontFamily(){
        String[] choices = GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames();
        //fail: if (choices.contains(this._font.getFamily()))
        //fail: if (java.util.Collections.unmodifiableCollection(choices).contains(this._font.getFamily()))
            //TODO
            ;
        String maybe_font_name = (String) JOptionPane.showInputDialog
                (frame
                ,"Choose Font Family"   // promt label
                ,"Choose..."            // title
                ,JOptionPane.QUESTION_MESSAGE
                ,null                   // Use default icon
                ,choices                // Array of choices
                //,choices[0]             // Initial choice
                ,this._font.getFamily()
                );
        //if (maybe_font_name == null) return;
        update_font_family(maybe_font_name);
    }

    void on_ChooseFontStyle(final String s){
        int style = 0;
        if (s.equals(str_style_PLAIN))
            style = Font.PLAIN;
        else if (s.equals(str_style_BOLD))
            style = Font.BOLD;
        else if (s.equals(str_style_ITALIC))
            style = Font.ITALIC;
        else if (s.equals(str_style_BOLDITALIC))
            style = Font.BOLD + Font.ITALIC;
        else {
            System.err.println("logic error: menu event: unknown font style : " + s);
            assert "logic error".isEmpty();
            return;
        }

        update_font_style(style);
    }
    void on_ChooseFontSize(){
        final Integer may_n = Dialogs.askMaybeIntByJSpinner(
                frame
                ,"Ask Font Size"
                ,"input font size:"
                , this._font.getSize(), 4, 10000, 2);
        if (may_n != null)
            update_font_size(may_n);
    }

    // Main class
    public static void main(String args[])
    throws Exception // IOException
    {
        final String example = "example:\n\tjava -cp . nn_ns.txt.IncrementalTextEditor -i=\"test.txt\" -e=\"utf8\" --font=\"Anonymous Pro PLAIN 24\"";
        final String description = "IncrementalTextEditor: text grows only";
        final String help_option_name = "does_show_help";

        Map<String, String> prefix2option_name =
            new PairsBuilder<String,String>()
                .iadd("-i=", "input_text_path")
                .iadd("--input=", "input_text_path")
                .iadd("-e=", "encoding")
                .iadd("--encoding=", "encoding")
                .iadd("--font=", "font")
                .iadd("--scroll_to_last_row=", "does_scroll_to_last_row")
                .iadd("-h=", help_option_name)
                .iadd("--help=", help_option_name)
                .mkHashMap();


        IParser<String> echo_parser = new EchoParser();
        IParser<Boolean> bool_parser = new ChoiceParser<>(
                //bug:(s)->(s=="true"), Arrays.asList("false", "true"));
                (s)->s.equals("true"), Arrays.asList("false", "true"));

        Map<String, OptionArgs> option_name2option_args =
            new PairsBuilder<String,OptionArgs>(
            ).iadd("input_text_path"
                ,mkOptionArgs(null, echo_parser
                    , "input_text_path, show in upper window")
            ).iadd("encoding"
                ,mkOptionArgs("utf8", echo_parser
                    , "encoding of input_text_path")
            ).iadd("font"
                ,mkOptionArgs("", echo_parser
                    , "font family")
             ).iadd("does_scroll_to_last_row"
                ,mkOptionArgs("false", bool_parser
                    , "scroll upper windows to last row")
           ).iadd(help_option_name
                ,mkOptionArgs("false", bool_parser
                    , "show help and exit")
            ).mkHashMap();

        final boolean override = false;
        PrefixedArgumentsParser parser = new PrefixedArgumentsParser
                (prefix2option_name
                ,option_name2option_args
                ,help_option_name
                ,description
                ,example
                ,override
                );

        Pair<Map<String, Object>, ArrayList<String>> result_pair = null;
        try{
            result_pair = parser.parse_args(args);
            ArrayList<String> remaining_args = result_pair.snd();
            if (!remaining_args.isEmpty()){
                throw new ParseAllPrefixedArgumentsException(String
                    .format("unknown arguments: %s", remaining_args));
            }
        } catch(Exception e){
            System.err.println(parser.the_help_string);
            throw e;
        }

        Map<String, Object> option_name2result = result_pair.fst();
        boolean does_show_help = (Boolean)(option_name2result
                .get(help_option_name));
        if (does_show_help) {
            System.out.println(parser.the_help_string);
            return;
        }

        boolean does_scroll_to_last_row = (Boolean)(option_name2result
                .get("does_scroll_to_last_row"));

        Path txt_path = Paths.get((String)(option_name2result
                .get("input_text_path")));
        Charset encoding = Charset.forName((String)(option_name2result
                .get("encoding")));
        Font font = Font.decode((String)(option_name2result
                .get("font")));

        IncrementalTextEditor editer = new IncrementalTextEditor(
            txt_path, encoding, font, does_scroll_to_last_row);
        //editer.frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        editer.frame.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        editer.frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                //System.exit(0);
                //editer.quit_dialog();
                //editer.on_Quit();
                editer.on_Quit__impl();
            }
        });
        return;
    }

    void on_Quit__impl(){
        final String new_txt = area_to_edit.getText();
        if (new_txt.isEmpty())
            System.exit(0);
        quit_dialog();
    }
    void quit_dialog()
    {
        int n = JOptionPane.showConfirmDialog
                (frame
                ,"Would you like to save text before quit?"
                ,"Save before Quit?"
                ,JOptionPane.YES_NO_CANCEL_OPTION
                ,JOptionPane.QUESTION_MESSAGE
                );
        if (n == JOptionPane.YES_OPTION){
            // save & quit
            on_SaveAndQuit();
        }
        else if (n == JOptionPane.NO_OPTION){
            // quit without save
            on_QuitWithoutSave();
        }
        else if (n == JOptionPane.CANCEL_OPTION){
            // neither save nor quit
            // no-op; pass
        }
        else {
            assert "logic error".isEmpty();
        }
    }
} // class IncrementalTextEditor



