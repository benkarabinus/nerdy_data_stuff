package CustomerUI;
/*
 *Author: Ben Karabinus
 *Project: CIS 3145 Project #1
 *Date: 9/10/19
 *Description: This project demonstrates low level understanding of
 * multi-tiered applications
 */
import Business_Action.Customer;
import Database.CustomerDB;
import java.util.Scanner;
public class CustomerViewerApp {

   
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in); //create scanner object "sc"
        
        System.out.println("Customer Viewer: version 1.0");
        
        
        String choice = "y"; //Control variable
        
        while (choice.equalsIgnoreCase("y")){   // Main control loop
            
            // user enters a customer number to select a  record
            System.out.print("\nEnter a customer number:  "); 
            int custNum = Integer.parseInt(sc.nextLine());
            
            // If no customer is found a "null" customer object is returned
            //The user is informed the record doesn't exist
            Customer customer = CustomerDB.getCustomer(custNum);
            if (customer.getName() == null){
                System.out.print("\nThere is no customer number " +custNum+ " to display.\n");
            }
            
            //If valid customer object is returned customer info is displayed 
            else{
                System.out.println("\n" +customer.getNameAndAddress());
            }
                System.out.print("");
                
            //Loop Control
            System.out.print("\nDisplay another customer number? (y/n):  ");
            choice = sc.nextLine();
        }
        
        System.out.println("\nGoodbye!\n");
    }
    
}
