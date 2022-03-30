/*
Author: Ben Karabinus
Project:ch04_ex4_GuessingGameBDAK
Date: 8/29/19
Description: This project was created to display basic understanding of classes and methods
*/
package murach.games;

import java.util.Random;


public class NumberGame{
    int upperL;
    int targetNum;
    int numGuess;
    Random random = new Random();
    /* In this class we have  multiple constructors 
       a default and a second constructor that constructs
       objects or instances of the class.
    */
    
    public NumberGame(){    //default constructor
        
    this(50);  // using this keyword to construct specific instance of class NumberGame
}
    
    public NumberGame(int upperLimit){
        upperL = upperLimit;
        targetNum = random.nextInt(upperLimit + 1);
        numGuess = 1; 
    }
    
    //Methods used to set and return traits of class objects 
    
    public int getUpperL(){
        return this.upperL;
    }
    
    public int getTargetNum(){
        return targetNum;
    }
    
    public int getNumGuesses(){
        return numGuess;
    }
    
    public void incrementGuessCount(){
        numGuess += 1;
    }
}

