package Database;
import Business_Action.Customer;
/*
 *Author: Ben Karabinus
 *Project: CIS 3145 Project #1
 *Date: 9/10/19
 *Description: This project demonstrates low level understanding of
 * multi-tiered applications
 */
public class CustomerDB {
    //Static method used to create customer object
    public static Customer getCustomer(int custNum){
        
        //Create new customer object
        Customer customer = new Customer();
        
        //Customer Data store
            if(custNum == 123){
                customer.setName("Michael Martin");
                customer.setAddress("1376 Hill Street");
                customer.setCity("Luckey");
                customer.setState("OH");
                customer.setZip("43443");  
            }
            else if(custNum == 124){
                customer.setName("Marjorie Galvin");
                customer.setAddress("3144 Hillcrest Avenue");
                customer.setCity("Cambridge");
                customer.setState("MA");
                customer.setZip("02141"); 
            }
        
            else if(custNum == 125){
                customer.setName("Rebecca Cain");
                customer.setAddress("3572 New Street");
                customer.setCity("Jefferson");
                customer.setState("OR");
                customer.setZip("97352");
            }
            else if(custNum == 126){
                customer.setName("Ben Karabinus");
                customer.setAddress("1234 Some Street");
                customer.setCity("Denver");
                customer.setState("CO");
                customer.setZip("12345");
            }
            //Return customer object
            return customer;
    
    }
}