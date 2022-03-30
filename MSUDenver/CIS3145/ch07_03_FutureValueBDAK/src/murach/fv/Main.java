/*
Name: Ben Karabinus
Project: Chapter 7 ex:3
Date: 9/10/19
Description: Practice using arithmetic operators and helper classes.
*/

package murach.fv;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // display a welcome message
        System.out.println("Welcome to the Future Value Calculator");
        System.out.println();

        Scanner sc = new Scanner(System.in);        
        String choice = "y";
        while (choice.equalsIgnoreCase("y")) {

            // get input from user
            System.out.print("Enter monthly investment:   ");
            double monthlyInvestment = Double.parseDouble(sc.nextLine());

            System.out.print("Enter yearly interest rate: ");
            double yearlyInterestRate = Double.parseDouble(sc.nextLine());

            System.out.print("Enter number of years:      ");
            int years = Integer.parseInt(sc.nextLine());                        
            
            // convert yearly values to monthly values
            double monthlyInterestRate = yearlyInterestRate / 12 / 100;
            int months = years * 12;        

            // calculate the future value
            double futureValue = 0;
            final double YEARLY_FEE = 50.00; // constant variable YEARLY_FEE
            int i = 1;
            while (i <= months) {
                // many different ways to condense the code below, 2 optons are shown 
                  futureValue = (futureValue += monthlyInvestment) // option #1 
                          + futureValue * monthlyInterestRate;
//                futureValue = ((futureValue = futureValue + monthlyInvestment) option #2
//                          + (futureValue * monthlyInterestRate));
//                double monthlyInterestAmount = 
//                      futureValue * monthlyInterestRate;
//                futureValue = futureValue + monthlyInterestAmount;

                if(i % 12 == 0){ //testing if value is divisible by 12
                    futureValue -= YEARLY_FEE; // if condition is true subtract yearly fee
                      //This value is subtracted at the end of the year
                      
//                    futureValue = futureValue - YEARLY_FEE; //Same code
                }
                i ++; //increment operator used to increment counter variable "i"
            }            

            // format and display the result
            System.out.println("Yearly Fee:                 "+
                    NumberFormat.getCurrencyInstance().format(YEARLY_FEE));
            System.out.println("Future value:               " + 
                    NumberFormat.getCurrencyInstance().format(futureValue));
            System.out.println();

            // Loop Control
            System.out.print("Continue? (y/n): ");
            choice = sc.nextLine();
            System.out.println();
        }
        System.out.println("Bye!");
    }
}