/*
Name: Ben Karabinus
Project: Chapter 15 Exercise 3 Guessing Game
Date: 10/23/19
Description: This project shows basic understanding of creating and formatting 
date objects in Java 8
*/

package murach.games;

import java.util.Scanner;

public class Main {

    public static void main(String args[]) {
        System.out.println("Welcome to the Number Guessing Game");
        System.out.println();

        Scanner sc = new Scanner(System.in);
        NumberGame game = new NumberGame();
        System.out.println("I have selected a number between 0 and " +
                game.getUpperLimit());
        System.out.println();
        //Create a LocalDateTime object and store it in the NumberGame object
        //This object references the start of the game 
        game.setStartTime();
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
            guess = Integer.parseInt(sc.nextLine());
        }
        //Create a LocalDateTime object and store it in the NumberGame object
        //This object references the end of the game
        game.setEndTime();
        System.out.println("Correct!\n");
        
        System.out.println("You guessed the correct number in " +
                game.getGuessCount() + " guesses.\n");
        //Print the game duration to the console
        System.out.println("It took you "+game.getDuration()+ " seconds "
                + "to guess the correct number.");
        System.out.println("");
        //Print the current formatted date to the console
        System.out.println("This game was played on " +game.getDateFormatted()+".");
        System.out.println("");
        System.out.println("Bye!");
    }
}