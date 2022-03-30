/*
Name: Ben Karabinus 
Project: Chapter 8 Exercise 3 Guessing Game
Date: 9/18/19
Description: This project shows low level understanding of conditional
             statements.
 No in-line comments were added to this class since I didn't edit the code
*/

package murach.games;

import java.util.Random;

public class NumberGame {
    private int upperLimit;
    private int number;
    private int guessCount;
    
    public NumberGame() {
        this(50);        
    }
    
    public NumberGame(int upperLimit) {
        this.upperLimit = upperLimit;
        Random random = new Random();
        number = random.nextInt(upperLimit + 1) ;
        guessCount = 1;
    }

    public int getNumber() {
        return number;
    }

    public int getGuessCount() {
        return guessCount;
    }
    
    public int getUpperLimit() {
        return upperLimit;
    }
    
    public void incrementGuessCount() {
        guessCount = guessCount + 1;
    }
}