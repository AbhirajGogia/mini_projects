/**
 * @author: Abhiraj Gogia
 * @date Apr 10, 2021
 * @name InputReader
 * @brief A Controller and GUI class for the 2048 game.
 */

package src;
import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableCellRenderer;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

/**
 * @brief Controller and GUI class for the 2048 game.
 * @details The controller reads arrow key inputs to control shifts. The GUI is supported by Swing.
 */
public class InputReader{
    Integer[][] data;
    protected static JFrame frame;
    protected static JTable table;
    protected int size;
    protected static JLabel itemLabel;
    protected static JPanel finalPanel;
    protected static JLabel label;


    /**
     * @brief Constructor for InputReader class
     * @details Involves the initialization and setting of various GUI related design variables. These include
     * a table to store the values of BoardStatus, A frame that displays the game and holds the table. Panels for
     * display messages and a pane to layer various objects on the frame.
     */
    public InputReader() {
        size = 40;
        frame = new JFrame();
        frame.setVisible(true);
        frame.setBackground(new Color(244,226,198));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(12*size,12*size);
        frame.setBounds(0,0,12*size, 12*size);
        frame.setFocusable(true);
        finalPanel = new JPanel();
        label = new JLabel();

        data = BoardStatus.getBoardValues();
        String[] columnNames = {"", "", "", ""};
        DefaultTableModel model =  new DefaultTableModel(data, columnNames);
        table = new JTable(model){

            /**
             * @brief A color renderer for the cells of table of board values.
             * @param renderer The Renderer object responsible for rendering the table.
             * @param rowIndex An int representing the specific row index of the cell.
             * @param columnIndex An int representing the specific column index of the cell.
             * @details Depending on the value of the cell, the method will call upon auxiliary functions
             * to pick the color of the cell background and font color.
             * @returns A component representing the updated cell
             */
            @Override
            public Component prepareRenderer(TableCellRenderer renderer, int rowIndex,
                                             int columnIndex) {
                JComponent component = (JComponent) super.prepareRenderer(renderer, rowIndex, columnIndex);
                Object value = getValueAt(rowIndex, columnIndex);
                component.setForeground(fontChoose((int) value));
                component.setBackground(colorChoose((int) value));
                return component;
            }
        };

        table.setFont(new Font("Monospaced", Font.BOLD, size));
        table.setRowHeight(size*5/2);
        table.getColumnModel().getColumn(0).setPreferredWidth(3* size);
        table.getColumnModel().getColumn(1).setPreferredWidth(3* size);
        table.getColumnModel().getColumn(2).setPreferredWidth(3* size);
        table.getColumnModel().getColumn(3).setPreferredWidth(3* size);
        table.setBackground(new Color (204, 192, 179));
        table.setForeground(Color.BLACK);
        table.setGridColor(new Color (204, 192, 179));
        table.setShowGrid(true);

        DefaultTableCellRenderer centerRenderer = new DefaultTableCellRenderer();
        centerRenderer.setHorizontalAlignment(SwingConstants.CENTER);
        for (int i=0; i<table.getColumnCount();i++){
            table.setDefaultRenderer(table.getColumnClass(i),centerRenderer);
        }

        table.updateUI();

        itemLabel = new JLabel("2048 | Score: " +  Integer.toString( BoardStatus.getScore()), JLabel.CENTER);

        frame.add(itemLabel, BorderLayout.PAGE_END);
        table.setBounds(0,0, 12* size, 12*size);
        JScrollPane pane = new JScrollPane(table);
        pane.setBackground(new Color (204, 192, 179));
        frame.setBackground(new Color (204, 192, 179));
        frame.add(pane);
        frame.setVisible(true);
        frame.pack();
        table.setCellSelectionEnabled(true);
        frame.addKeyListener(new KeyListener(){

            /**
             * @brief An abstract method of the abstract class KeyListener for when a key is typed.
             * @details Is not supported by this GUI.
             */
            @Override
            public void keyTyped(KeyEvent e){ }
            /**
             * @brief An abstract method of the abstract class KeyListener for when a key is pressed.
             * @details Is not supported by this GUI.
             */
            @Override
            public void keyPressed(KeyEvent e){ }


            /**
             * @brief An abstract method of the abstract class KeyListener for when a key is released. When an arrow
             * key is released, depending on which key, a specific shift occurs. The resulting new board of this shift
             * is then used to update the GUI table.
             * @details Calls upon a shiftUp when the up arrow is released, calls upon a shiftDown when the down arrow
             * is released, calls upon a shiftRight when the right arrow is released, and calls upon a shiftLeft when
             * the left arrow is released.
             */
            @Override
            public void keyReleased (KeyEvent e){
                    if (e.getKeyCode() == KeyEvent.VK_UP){
                        BoardStatus.shiftUp();
                        setVal(BoardStatus.getBoardValues());}

                    if (e.getKeyCode() == KeyEvent.VK_DOWN){
                        BoardStatus.shiftDown();
                        setVal(BoardStatus.getBoardValues()); }

                    if (e.getKeyCode() == KeyEvent.VK_RIGHT){
                        BoardStatus.shiftRight();
                        setVal(BoardStatus.getBoardValues()); }

                    if (e.getKeyCode() == KeyEvent.VK_LEFT){
                        BoardStatus.shiftLeft();
                        setVal(BoardStatus.getBoardValues());}
                }
            /**
             * @brief A setter method for updating the GUI table's values.
             * @param data A matrix of integers representing the new values that the table is to be updated to.
             */
            public void setVal(Integer[][] data){
                for (int i = 0; i < 4; i++){
                    for (int j = 0; j < 4; j ++){
                        table.setValueAt(data[i][j], i, j);
                    }
                }
            }
        });

    }
    /**
     * @brief A setter method for changing the colour of the font in a table cell.
     * @param value The value of the number in the cell, which is used to determine font's colour.
     * @details Normalizes the value of the cell using a pre-set function, and then selects specific font colours
     * which correspond to what the set background colour would be.
     */
    private Color fontChoose(int value) {
        int n = normalize(value);
        if ( n > 2 ){
            return Color.WHITE;
        }
        else if(n == 0){
            return new Color (204, 192, 179);
        }
        else{
            return Color.BLACK;
        }
    }

    /**
     * @brief A setter method for changing the colour of the background in a table cell.
     * @param value The value of the number in the cell, which is used to determine backgrounds's colour.
     * @details Normalizes the value of the cell using a pre-set function, and then selects specific background colour
     * for it. Normalization allows for there to be a finite number of colours in the list, as when a value becomes
     * large enough that it all the colours have been passed through, the colour list loops, skipping the base colour.
     */
    private Color colorChoose(int value) {
        int n = normalize(value);

        Color[] colors = new Color[]{
                new Color (204, 192, 179),
            new Color (238, 228, 218),
            new Color (237, 224, 200),
            new Color (242, 177, 121),
            new Color (245, 149, 99),
            new Color (246, 124, 95),
            new Color (246, 94, 59),
            new Color (237, 207, 114),
            new Color (237, 204, 97),
            new Color (237, 200, 80),
            new Color (237, 197, 63),
            new Color (237, 194, 46),
            new Color (237, 175, 0),
                new Color (237, 150, 0),
                new Color (237, 125, 0)};
            return colors[n];
        }

    public int normalize(int value){
        int n;
        if (value != 0) {
            n = (int) (Math.log(value) / Math.log(2));
        }
        else{
            n = 0;
        }
        while (n > 15){
            n -= 16;
            if (n == 0){
                n++;
            }
        }
        return n;
    }


}

