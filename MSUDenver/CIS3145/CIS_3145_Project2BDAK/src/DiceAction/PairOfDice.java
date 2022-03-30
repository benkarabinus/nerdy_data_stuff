/*
 * Ben Karabinus
 * CIS 3145 Project #2 "Dice Rolling Project
 * Date: 10/8/19
 * Description: This project shows basic understanding of multi-tiered applicatons
   written in Java
 */
package DiceAction;

import DiceCreation.Die;

public class PairOfDice {
    //instance variables of the PairOfDice class
    private Die dieOne;
    private Die dieTwo;
    private int sum;
    
    //default constructor instantiates 2 6 sided die objects
    public PairOfDice(){
        dieOne = new Die();
        dieTwo = new Die();
    }
    
    //second constructor allows user to pick number of sides for the die
    public PairOfDice (int sides){
        dieOne = new Die(sides);
        dieTwo = new Die(sides);
    }
    
    //initiates the roll method of both die objects
    public void roll(){
        dieOne.roll();
        dieTwo.roll();
    }
    
    public int getValue1(){
        return dieOne.getValue();//return the value of dieOne
    }
    
    public int getValue2(){
        return dieTwo.getValue();//return the value of dieTwo
    }
    
    //add the value of dieOne and dieTwo returning the sum
    public int getSum(){
        sum = dieOne.getValue() + dieTwo.getValue();
        return sum;
    }
    
    
}
