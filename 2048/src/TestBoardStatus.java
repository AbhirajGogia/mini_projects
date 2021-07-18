/**
 * @author: Abhiraj Gogia
 * @date Apr 10, 2021
 * @name TestBoardStatus
 * @brief A module for testing BoardStatus.
 */
package src;
import org.junit.*;

import java.util.Arrays;

import static org.junit.Assert.*;

public class TestBoardStatus {

    BoardStatus board;
    Viewer view;
    InputReader reader;

    @Before
    public void setUp(){
        board = new BoardStatus();

    }

    @After
    public void tearDown(){
        board = null;
    }

    @Test
    public void testGetBoardValues(){
        Integer[][] case_1 = new Integer[4][4];
        for (int i = 0 ; i < 4; i++){
            for (int j = 0 ; j < 4; j ++){
                case_1[i][j] = 2;
            }
        }
        Integer[][] expected = new Integer[][] {{2,2,2,2}, {2,2,2,2},
                {2,2,2,2}, {2,2,2,2}};
        BoardStatus.setBoardValues(case_1);

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }

    }
    @Test
    public void testGetScore() {
        BoardStatus.setScore(50);
        assertEquals(BoardStatus.getScore(), (Integer) 50);
        BoardStatus.setScore(1000);
        assertEquals(BoardStatus.getScore(), (Integer) 1000);
    }

    @Test
    public void testIncreaseScore() {
        BoardStatus.setScore(50);
        BoardStatus.increaseScore(50);
        assertEquals(BoardStatus.getScore(), (Integer) 100);
        BoardStatus.setScore(1000);
        BoardStatus.increaseScore(2000);
        assertEquals(BoardStatus.getScore(), (Integer) 3000);
    }



    @Test
    public void testBoardFull() {
        Integer[][] values = new Integer[][] {{2,2,2,2}, {2,2,2,2},
                {2,2,2,2}, {2,2,2,2}};
        Integer[][] values_2 = new Integer[][] {{2,2,2,2}, {2,2,2,2},
                {2,2,0,2}, {2,2,2,2}};

        BoardStatus.setBoardValues(values);
        assertTrue(BoardStatus.boardFull());

        BoardStatus.setBoardValues(values_2);
        assertFalse(BoardStatus.boardFull());


    }

    @Test
    public void testHorizontalCombine(){
        Integer[][] values = new Integer[][] {{0,0,0,0}, {2,0,0,0},
                {0,0,0,0}, {0,0,0,0}};

        BoardStatus.setBoardValues(values);
        BoardStatus.horizontalCombine(0, 1, 1);
        Integer[][] expected = new Integer[][] {{0,0,0,0}, {0,2,0,0},
                {0,0,0,0}, {0,0,0,0}};

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }
    }

    @Test
    public void testVerticalCombine(){
        Integer[][] values = new Integer[][] {{2,0,0,0}, {0,0,0,0},
                {0,0,0,0}, {0,0,0,0}};

        BoardStatus.setBoardValues(values);
        BoardStatus.verticalCombine(0, 1, 0);
        Integer[][] expected = new Integer[][] {{0,0,0,0}, {2,0,0,0},
                {0,0,0,0}, {0,0,0,0}};

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }
    }

    @Test
    public void testShiftRight(){
        Integer[][] values = new Integer[][] {{2,0,0,0}, {2,0,0,0},
                {2,0,0,0}, {2,0,0,0}};

        BoardStatus.setBoardValues(values);
        try
        {
            BoardStatus.shiftRight();}
        catch (Exception NullPointerException){}

        Integer[][] expected = new Integer[][] {{0,0,0,2}, {0,0,0,2},
                {0,0,0,2}, {0,0,0,2}};

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }
    }

    @Test
    public void testShiftLeft(){
        Integer[][] values = new Integer[][] {{0,0,0,2}, {0,0,0,2},
                {0,0,0,2}, {0,0,0,2}};

        BoardStatus.setBoardValues(values);
        try
        {
            BoardStatus.shiftLeft();}
        catch (Exception NullPointerException){}

        Integer[][] expected = new Integer[][] {{2,0,0,0}, {2,0,0,0},
                {2,0,0,0}, {2,0,0,0}};

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }
    }

    @Test
    public void testShiftDown(){
        Integer[][] values = new Integer[][] {{2,2,2,2}, {0,0,0,0},
                {0,0,0,0}, {0,0,0,0}};

        BoardStatus.setBoardValues(values);
        try
        {
            BoardStatus.shiftDown();}
        catch (Exception NullPointerException){}

        Integer[][] expected = new Integer[][] {{0,0,0,0}, {0,0,0,0},
                {0,0,0,0}, {2,2,2,2}};

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }
    }

    @Test
    public void testShiftUp(){
        Integer[][] values = new Integer[][] {{0,0,0,0}, {0,0,0,0},
                {0,0,0,0}, {2,2,2,2}};

        BoardStatus.setBoardValues(values);
        try
        {
            BoardStatus.shiftUp();}
        catch (Exception NullPointerException){}

        Integer[][] expected = new Integer[][] {{2,2,2,2}, {0,0,0,0},
                {0,0,0,0}, {0,0,0,0}};

        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                assertEquals(BoardStatus.getBoardValues()[i][j],expected[i][j]);
            }
        }
    }

    @Test
    public void testNewElement(){
        Integer[][] values = new Integer[][] {{2,2,2,2}, {2,2,2,2},
                {2,2,0,2}, {2,2,2,2}};

        BoardStatus.setBoardValues(values);
        try
        {
            BoardStatus.newElement();}
        catch (Exception NullPointerException){}

        assertTrue(BoardStatus.boardFull());
    }











}

