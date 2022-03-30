package murach.fv;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.NumberFormat;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

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
            int i = 1;
            while (i <= months) {
                futureValue = futureValue + monthlyInvestment;
                double monthlyInterestAmount = 
                        futureValue * monthlyInterestRate;
                futureValue = futureValue + monthlyInterestAmount;            
                i = i + 1;
            }            

            // format and display the result
            System.out.println("Future value:               " + 
                    NumberFormat.getCurrencyInstance().format(futureValue));
            System.out.println();

            // see if the user wants to continue
            System.out.print("Continue? (y/n): ");
            choice = sc.nextLine();
            System.out.println();
            
            try {
                //connect to file
                FileOutputStream outputStream = new FileOutputStream("FutureValue.bin",true);
                BufferedOutputStream bufferedOutput = new BufferedOutputStream(outputStream);
                DataOutputStream out = new DataOutputStream(bufferedOutput);
                out.writeDouble(monthlyInvestment);
                out.writeDouble(yearlyInterestRate);
                out.close();
            } catch (FileNotFoundException ex) {
                System.out.println("File not found" + ex.getMessage());
            } catch (IOException ex) {
                System.out.println("IO exception occured. Oops");
            }
        }
        
        try {
            FileInputStream inputStream = new FileInputStream("FutureValue.bin");
            BufferedInputStream bufferIn = new BufferedInputStream(inputStream);
            DataInputStream in = new DataInputStream(bufferIn);
            
            while(in.available()> 0){
                System.out.println("Monthly Investment: \t" +in.readDouble());
                System.out.println("Yearly Interest Rate: \t" + in.readDouble());
                System.out.println("number of years: \t"+ in.readInt());
                System.out.println("Future Value: \t" +in.readDouble());
            }
        } catch (FileNotFoundException ex) {
            System.out.println("File not Found. Sorry");
        } catch (IOException ex) {
            System.out.println("IO exception occured. oops");
        }
        System.out.println("Bye!");
    }
}