/*
 * Ben Karabinus
 * CIS 3145 Project #2 "Dice Rolling Project"
 * Date: 10/8/19
 * Description This project shows basic understanding of multi-tiered applicatons
   written in Java
 */
package PlayerUI;

import DiceAction.PairOfDice;
import java.util.Scanner;


public class DiceRollerApp {

    public static void main(String[] args) { //beggining main method
        
        
        System.out.print("Welcome to the Paradise Roller \n");//welcome message
        System.out.print("");    
        //create scanner object to get user input
        Scanner sc = new Scanner(System.in);
        //user initiates the game
        System.out.print("\nRoll the dice? (y/n):  ");
        System.out.print("");
        //choice will be used as loop control variable
        String choice = sc.nextLine();
        
        //intiate rollNum to track the number of times the user has rolled the die
        int rollNum = 1;
        
        //control loop 
        while(choice.equalsIgnoreCase("y")){
            // create new PAirOfDice object each time the user rolls
            PairOfDice currentGame = new PairOfDice();
            
            //call PairOfDice "roll" method
            currentGame.roll();
            //print results to the screen
            System.out.print("\nRoll " +rollNum+ ": " +currentGame.getValue1()+ " & "+currentGame.getValue2()+"\n");
            //conditional statements print message to screen based upon roll
            if (currentGame.getSum() == 7){
                System.out.print("Craps!\n");
                System.out.print("");
            }
            if (currentGame.getSum() == 2){
                System.out.print("Snake Eyes!\n");
                System.out.print("");
            }
            if (currentGame.getSum() == 12){
                System.out.print("Box Cars!\n");
                System.out.print("");
            }
            //rollNum is incremented
            rollNum++;
            //user initiates new game 
            System.out.print("\nRoll again? (y/n):  ");
            System.out.print("");
            choice = sc.nextLine();
            
            
           
        }
        
    }
    
}
