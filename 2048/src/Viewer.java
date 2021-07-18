/**
 * @author: Abhiraj Gogia
 * @date Apr 10, 2021
 * @name Viewer
 * @brief ASCII model viewer for 2048. Only to be used for debugging purposes.
 */

package src;

/**
 * @brief An ASCII model viewer for 2048
 * @details The Viewer object is represents a board, which is created using a BoardStatus object
 */
public class Viewer {

    private Integer[][] values;


    /**
     * @brief Constructor for Viewer. Retrieves the values of the BoardStatus object and stores it as
     * a state variable values.
     */
    public Viewer (){
        values = BoardStatus.getBoardValues();


    }

    /**
     * @brief Updates the state variable values by calling upon the BoardStatus object to once again
     * retrieve it's values
     */
    public void updatesValues(){
        values = BoardStatus.getBoardValues();
    }

    /**
     * @brief Prints out a representation of the board values to terminal.
     */
    public void printBoard(){
        updatesValues();
        System.out.println("________________");
        for (Integer[] i : values)
        {
            for (int j : i)
            {
                System.out.print(j + " ");
            }
            System.out.println();
        }
        System.out.println("________________");

    }



}

