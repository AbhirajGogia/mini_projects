/**
 * @author: Abhiraj Gogia
 * @date Apr 10, 2021
 * @name Main
 * @brief The Main class which intializes the game's methods and allows it begin
 */
package src;

/**
 * @brief Game starting class for 2048
 */
public class Main {

    /**
     * @brief Constructor for Main class.
     */
    public static void main(String[] args) {
        BoardStatus board = new BoardStatus();
        Viewer view = new Viewer();
        new InputReader();




    }
}

