/*
Name: Ben Karabinus 
Project: Chapter 8 Exercise 3 Guessing Game
Date: 9/18/19
Description: This project shows low level understanding of conditional
             statements.
*/

package murach.games;

import java.util.Scanner;


public class Main {

    public static void main(String args[]) {
        System.out.println("Welcome to the Number Guessing Game");
        System.out.println();

        Scanner sc = new Scanner(System.in);
        NumberGame game = new NumberGame();
        System.out.println("I have selected a number between 0 and " +game.getUpperLimit()+ ".");
        System.out.println();
        
//        while (guess != game.getNumber()) {
          while (true){  //Setting condition "TRUE" creates infinite loop
              System.out.print("\nEnter your guess: ");
//            if (guess < game.getNumber()) {
//                System.out.println("Your guess is too low.\n");
              int guess;
              try{
                  guess = Integer.parseInt(sc.nextLine()); 
              }catch (Exception e) {
                  System.out.print("\nError! Invalid number\n");
                          continue;
              }
              
              if (guess > game.getUpperLimit() || guess < 0){
                  System.out.print("\nPlease enter a number between 0 and "
                   +game.getUpperLimit() +".\n");
                  continue;
                }else if (guess == game.getNumber()){ //Loop control
                  break;
                } else if (guess > game.getNumber()) {
                    //nested if  statement
                    if ((guess - game.getNumber()) > 10){
                        System.out.print("\nWay too high!\n");
                    }else
                        System.out.println("\nYour guess is too high.");
                }else
                    System.out.println("\nYour guess is to low.");
            game.incrementGuessCount();
            
//            System.out.print("Enter your guess: ");
//            guess = Integer.parseInt(sc.nextLine());
        }        
        System.out.println("\nCorrect!\n");
        
        System.out.println("You guessed the correct number in " +
                game.getGuessCount() + " guesses.\n");
        
        // if block displays message based on # of guesses
        if (game.getGuessCount()> 3 && game.getGuessCount() <= 7){
            System.out.print("You've got potential.\n");
        }else if(game.getGuessCount()<=3){
            System.out.print("You're ready for differential equations.\n");
        }else
            System.out.print("Math is hard.\n");
         
        System.out.println("\nBye!");
    }
}