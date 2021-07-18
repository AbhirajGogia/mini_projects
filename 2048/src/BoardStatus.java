/**
 * @author: Abhiraj Gogia
 * @date Apr 10, 2021
 * @name BoardStatus
 * @brief A model for holding all information regarding the state of a board as well as the mechanics of
 * any tiles/numbers shifting.
 */

package src;
import java.util.Random;


/**
 * @brief A model for holding board information and movements.
 * @details The board is represented by a 4 x 4 matrix of positive integers.
 */
public class BoardStatus {

    private static Integer[][] boardValues = new Integer[4][4];
    private static Integer score;

    /**
     * @brief Constructor for BoardStatus.
     * @details Initializes the matrix representing the board and initializes all of its values to zero.
     * Then it choses 2 random starting tiles and assigns them values of 2.
     */
    public BoardStatus(){
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                boardValues[i][j] = 0;
            }
        }
        score = 0;
        int[] temp  = new int[]{0,1,2,3};
        Random rand = new Random();
        int[] start = new int[4];
        start[0] = rand.nextInt(3);
        start[1] = rand.nextInt(3);
        start[2] = rand.nextInt(3);
        start[3] = rand.nextInt(3);
        while (start[0] == start[2] && start[1] == start[3]){
            start[2] = rand.nextInt(4);
            start[3] = rand.nextInt(4);
        }
        boardValues[start[0]][start[1]] = 2;
        boardValues[start[2]][start[3]] = 2;

    }
    /**
     * @brief Getter function for the board values.
     * @returns Returns a 4x4 matrix filled with values representing the values of the board.
     */
    public static Integer[][] getBoardValues(){
        return boardValues;
    }


    /**
     * @brief Horizontal combiner for two values in the same row.
     * @details If two tiles in the same row are the same, the values combine and are shifted to the second tile. The
     * GUI scoreboard is updated with an increase equal to the combined number formed. Furthermore, if the second
     * tile is 0, the first tile value shifts over to the second tile.
     */
    public static void horizontalCombine(int index1, int index2, int row){
        if (boardValues[row][index1].equals(boardValues[row][index2])){
            boardValues[row][index1] = 0;
            boardValues[row][index2] = 2 * boardValues[row][index2];
            increaseScore(2 * boardValues[row][index2]);
            InputReader.itemLabel.setText("2048 | Score: " +  Integer.toString( BoardStatus.getScore()));
        }
        else if (boardValues[row][index1] != 0 && boardValues[row][index2] == 0){
            boardValues[row][index2] = boardValues[row][index1];
            boardValues[row][index1] = 0;

        }

    }
    /**
     * @brief Vertical combiner for two values in the same column.
     * @details If two tiles in the same column are the same, the values combine and are shifted to the second tile. The
     * GUI scoreboard is updated with an increase equal to the combined number formed. Furthermore, if the second
     * tile is 0, the first tile value shifts over to the second tile.
     */
    public static void verticalCombine(int index1, int index2, int column){
        if (boardValues[index1][column].equals(boardValues[index2][column])){
            boardValues[index1][column] = 0;
            boardValues[index2][column] = 2 * boardValues[index2][column];
            increaseScore(2 * boardValues[index2][column]);
            InputReader.itemLabel.setText("2048 | Score: " +  Integer.toString( BoardStatus.getScore()));
        }
        else if (boardValues[index1][column] != 0 && boardValues[index2][column] == 0){
            boardValues[index2][column] = boardValues[index1][column];
            boardValues[index1][column] = 0;

        }

    }

    /**
     * @brief Applies a horizontal combine in the rightward direction of the board to all elements.
     * @details Iterates from left to right combining elements if possible. At the end of this shift, a new element
     * is called upon to be added.
     */
    public static void shiftRight(){
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 3; j++){
                horizontalCombine(j, j + 1, i);
            }
        }
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 3; j++){
                horizontalCombine(j, j + 1, i);
            }
        }
        newElement();
    }

    /**
     * @brief Applies a horizontal combine in the leftward direction of the board to all elements.
     * @details Iterates from right to left combining elements if possible. At the end of this shift, a new element
     * is called upon to be added.
     */
    public static void shiftLeft(){
        for (int i = 0; i < 4; i++){
            for (int j = 3; j > 0; j--){
                horizontalCombine(j, j - 1, i);
            }
        }
        for (int i = 0; i < 4; i++){
            for (int j = 3; j > 0; j--){
                horizontalCombine(j, j - 1, i);
            }
        }
        newElement();
    }
    /**
     * @brief Applies a vertical combine in the downward direction of the board to all elements.
     * @details Iterates from top to bottom combining elements if possible. At the end of this shift, a new element
     * is called upon to be added.
     */
    public static void shiftDown(){
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 3; j++){
                verticalCombine(j, j + 1, i);
            }
        }
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 3; j++){
                verticalCombine(j, j + 1, i);
            }
        }
        newElement();
    }
    /**
     * @brief Applies a vertical combine in the upward direction of the board to all elements.
     * @details Iterates from bottom to top combining elements if possible. At the end of this shift, a new element
     * is called upon to be added.
     */
    public static void shiftUp(){
        for (int i = 0; i < 4; i++){
            for (int j = 3; j > 0; j--){
                verticalCombine(j, j - 1, i);
            }
        }
        for (int i = 0; i < 4; i++){
            for (int j = 3; j > 0; j--){
                verticalCombine(j, j - 1, i);
            }
        }
        newElement();
    }

    /**
     * @brief Checks to see whether all spaces in the board are occupied.
     * @returns A boolean value representing whether or not the board is full.
     */
    public static boolean boardFull(){
        for (int i = 0; i < 4; i ++) {
            for (int j = 0; j < 4; j++) {
                if (boardValues[i][j] == 0){
                    return false;
                }

            }
        }
        return true;
    }
    /**
     * @brief If the board is not full, a new element is added.
     * @details In the case that the board is full, the method checks to see if any legal moves can be made
     * to combine any of the tiles. If legal moves can be made, nothing occurs. If no legal moves can be made, the
     * game ends and message saying game over is displayed. If the board is not full, a new randomized element is added
     * to a random empty spot in the board. There is a 90% chance this added number is 2, and a 10% chance this added
     * number is 4. When a new element is added, the players score increases by the same number of the element added.
     */
    public static void newElement(){
        if (boardFull()){
            for (int i = 0; i < 4; i++){
                for (int j = 0; j < 3; j++){
                    if (boardValues[i][j].equals(boardValues[i][j + 1])){
                        return;

                    }
                }
            }
            for (int i = 0; i < 4; i++){
                for (int j = 0; j < 3; j++){
                    if (boardValues[j][i].equals(boardValues[j+1][i])){
                        return;
                    }
                }
            }
            InputReader.itemLabel.setText("2048 | Score: " +  Integer.toString( BoardStatus.getScore()) + " | GAME OVER");
            return;

        }
            Random rand = new Random();
            int value = rand.nextInt(10);
            int index1 = rand.nextInt(4);
            int index2 = rand.nextInt(4);
            while (boardValues[index1][index2] != 0) {
                index1 = rand.nextInt(4);
                index2 = rand.nextInt(4);
            }

            if (value == 0){
                boardValues[index1][index2] = 4;
                increaseScore(4);
                InputReader.itemLabel.setText("2048 | Score: " +  Integer.toString( BoardStatus.getScore()));

            }
            else{
                boardValues[index1][index2] = 2;
                increaseScore(2);
                InputReader.itemLabel.setText("2048 | Score: " +  Integer.toString( BoardStatus.getScore()));
            }
        }

    /**
     * @brief Getter function for the player's score
     * @returns A integer value representing the player's score
     */
    public static Integer getScore(){
        return score;
    }
    /**
     * @brief A setter function for increasing the player's score.
     * @param x An integer value representing the amount the player's score will increase by.
     */
    public static void increaseScore(Integer x){
        score += x;
    }

    /**
     * @brief A function solely for testing and debugging purposes to pre-set the board values to a known combination
     * @param values A matrix of Integers that represent the values of a board.
     */
    public static void setBoardValues(Integer[][] values){
        boardValues = values;


    }
    /**
     * @brief A function solely for testing and debugging purposes to pre-set a specific cell of the board to
     *  a known value.
     * @param value An integer that represents the value being inserted.
     * @param rowIndex The index of the row of where the value is being inserted.
     * @param columnIndex The index of the column of where the value is being inserted.
     */
    public static void setCell(int value, Integer rowIndex, Integer columnIndex){
        boardValues[rowIndex][columnIndex] = value;

    }
    /**
     * @brief A function solely for testing and debugging purposes to pre-set the game score.
     * @param value An integer representing the game score being set.
     */
    public static void setScore(Integer value){
        score = value;
    }


}



