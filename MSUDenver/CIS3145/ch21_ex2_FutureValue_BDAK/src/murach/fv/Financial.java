/*
Name: Ben Karabinus
Project: Chapter 21 Exercise 2 Future Value
Date: 11/14/19
Description: This project shows basic understanding of creating GUI components
using the Java Swing Class.
Aside: no inline comments were added to this class ass no code was edited.
*/
package murach.fv;

public class Financial {

    public static double calculateFutureValue(double monthlyInvestment,
            double yearlyInterestRate, int years) {

        // convert yearly values to monthly values
        double monthlyInterestRate = yearlyInterestRate / 12 / 100;
        int months = years * 12;        
        
        // calculate the future value
        double futureValue = 0;
        for (int i = 1; i <= months; i++) {
            futureValue += monthlyInvestment;
            double monthlyInterestAmount = futureValue * monthlyInterestRate;
            futureValue += monthlyInterestAmount;            
        }
        
        return futureValue;
    }
}