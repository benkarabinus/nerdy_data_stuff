/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculatepayapp;

import java.text.NumberFormat;
import java.util.Currency;
import java.util.Scanner;

/**
 *
 * @author owner
 */
public class CalculatePayApp {
    
    
    
    
    

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Scanner sc = new Scanner(System.in);
        final int WORK_WEEK = 40;
        final double PAY_RATE =11.25;
        final double OVERTIME_RATE = 1.5;
        double hoursWorked = 0;
        double pay = 0;
        
        //ask for input
        while (hoursWorked != 999){
            try{
                System.out.println("Enter the hours worked  ");
                hoursWorked = sc.nextDouble();
            }catch(NumberFormatException e){
                System.out.println("Error in input "+ e.toString());
            }catch(Exception e) {
             System.out.println("Error in input: "+ e.toString());
            }
            //calculate pay
           
            if (hoursWorked <= WORK_WEEK)
                pay = hoursWorked * PAY_RATE;
            else if (hoursWorked > WORK_WEEK)
                pay = WORK_WEEK * PAY_RATE +
                        (hoursWorked - WORK_WEEK) * PAY_RATE * OVERTIME_RATE;
            NumberFormat currency = NumberFormat.getCurrencyInstance();
            System.out.println("Pay is: "+ currency.format(pay));
            
        }//end of while loop
        
        
    }
         
    
}
