/*
Name: Ben Karabinus
Project: CIS 3145 Project 4
Date: 11/23/19
Description: This project shows basic understanding of multi-tiered applications 
in Java 8
 */
package Business_Logic;

public class Customer {
    
    //instance variables of the customer class
    private int userID;
    private String firstName;
    private String lastName;
    private String email;
    
    
    //default constructor
    public Customer (){
        
    }
    
    //overloaded constructor
    public Customer (int userID, String firstName, String lastName,String email){
        
        this.userID = userID;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }
    
    
    //set methods customer attributes
    public void setUserID (int userID){
        
        this.userID = userID;
    }
    
    
    public void setFirstName (String firstName){
        this.firstName = firstName;
    }
    
    public void setLastName (String lastName){
        this.lastName = lastName;
    }
    
    public void setEmail (String email){
        this.email = email;
    }
    
    //get methods customer attributes
    public int getUserID (){
        return userID;
    }
    
    
    public String getFirstName (){
        return firstName;
    }
    
    public String getLastName(){
        return lastName;
    }
    
    public String getEmail(){
        return email;
    }
}
