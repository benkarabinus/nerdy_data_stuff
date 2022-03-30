/*
 * Ben Karabinus
 * CIS 3145 Project #2 "Dice Rolling Project
 * Date: 10/8/19
 * Description: This project shows basic understanding of multi-tiered applicatons
   written in Java
 */
package DiceCreation;

//import java.util.Random;
public class Die {
    //instance variables of the die class
    private int numSides;
    private int value;
    
    //6 sided die is constructed by default
    public Die(){
        numSides = 6;
    }
    
    //2nd constructor allows for user to choose number of sides
    public Die(int sides){
        numSides = sides;
    }
    
    //roll is simulated using random method of the Math class
    public void roll(){
        value = (int)(Math.random() * numSides + 1);
    }
    
    //value of the simulated roll is returned
    public int getValue(){
        return  value;
    }
    
}
