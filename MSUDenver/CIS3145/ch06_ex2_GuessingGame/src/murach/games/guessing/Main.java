/*Author: Ben Karabinus
Project:ch06_ex2_GuessingGameBDAK
Date: 9/3/19
Description: This project was created to display basic understanding of 
how to use the Netbeans IDE to debug programs and use packages to keep 
programs structured and orgnized
*/

package murach.games.guessing;

import java.util.Scanner;
import murach.games.business.NumberGame;

public class Main {

    public static void main(String args[]) {
        System.out.println("Welcome to the Number Guessing Game");
        System.out.println();

        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter upper limit for guess: ");
        int upperLimit = Integer.parseInt(sc.nextLine());        
        NumberGame game = new NumberGame(upperLimit);
        System.out.println();        
        
        System.out.print("Enter your guess: ");
        int guess = Integer.parseInt(sc.nextLine());
        while (guess != game.getNumber()) {
            if (guess < game.getNumber()) {
                System.out.println("Your guess is too low.\n");
            } else if (guess > game.getNumber()) {
                System.out.println("Your guess is too high.\n");
            }
            game.incrementGuessCount();
            System.out.print("Enter your guess: ");
            //Set guess equal to user input for next guess
            // prior sturcture created an infinite loop (logic error)
            guess = Integer.parseInt(sc.nextLine());
            
            
        }
        // move correct, guess, and bye statements outside of loop
        //This fixes a logic error
        System.out.println("Correct!\n");
        System.out.println("You guessed the correct number in " +
                game.getGuessCount() + " guesses.\n");
        System.out.println("Bye!");
        
        
    
  }
//This error was fixed by adding a closing brace for the main class (})
//This  was a syntax error
}
    
    