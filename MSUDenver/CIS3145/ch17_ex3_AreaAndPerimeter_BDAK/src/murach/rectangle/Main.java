/*
Name: Ben Karabinus
Project: Chapter 17 exercise 3
Date: 10/31/19
Description: This project shows basic understanding of writing to and printing
from a text file
*/
package murach.rectangle;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    //begining of the main method
    public static void main(String args[]) throws IOException {
        System.out.println("Welcome to the Area and Perimeter Calculator");
        System.out.println();
        
        //creation of the scanner object to take user input
        Scanner sc = new Scanner(System.in);
        String choice = "y";
        while (choice.equalsIgnoreCase("y")) {
            // get input from user
            System.out.print("Enter length: ");
            double length = Double.parseDouble(sc.nextLine());

            System.out.print("Enter width:  ");
            double width = Double.parseDouble(sc.nextLine());
          
            //create instance of the recatangle class
            Rectangle r = new Rectangle(length, width);
            
            // format and display output
            String message = 
                "Area:         " + r.getAreaNumberFormat() + "\n" +
                "Perimeter:    " + r.getPerimeterNumberFormat() + "\n";
            //read in and save relevant fields of the rectangle object 
            RectangleIO.save(r);
            System.out.println(message);

            // see if the user wants to continue
            System.out.print("Continue? (y/n): ");
            choice = sc.nextLine();
            System.out.println();
        }
        System.out.println("Bye!");
        System.out.println();
        //print contents of the rectangle.txt file to the console
        RectangleIO.printFile();
        
    }
}