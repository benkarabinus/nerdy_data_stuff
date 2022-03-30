/*Author: Ben Karabinus
Project:ch06_ex2_GuessingGameBDAK
Date: 9/3/19
Description: This project was created to display basic understanding of 
how to use the Netbeans IDE to debug programs and use packages to keep 
programs structured and orgnized
*/
package murach.games.business;

import java.util.Random;

public class NumberGame {
    // This error was fixed by correcting the spelling of int in instance variable declaration (int)
    // This was a syntax error
    private int number;
    private int guessCount;
    
    public NumberGame(int upperLimit) {
        Random random = new Random();
        number = random.nextInt(upperLimit + 1);
        guessCount = 1;
    }

    public int getNumber() {
        //This error was fixed by ending the statement with a semicolon (;)
        //This was a syntax error
        return number; 
    }

    public int getGuessCount() {
        return guessCount;
    }
    
    public void incrementGuessCount() {
        guessCount = guessCount + 1;
    }
}