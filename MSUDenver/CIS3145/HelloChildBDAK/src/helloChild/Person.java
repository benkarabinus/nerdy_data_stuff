/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package helloChild;

/**
 *
 * @author owner
 */
public class Person {
    
    private String firstName;
    private String lastName;
    
    public Person(){
        
        //this("Jane", "Doe");
        this.firstName = "Jane";
        this.lastName = "Doe";
        //versus 
        
    }
    
    public Person(String firstName, String lastName){
        
        this.firstName = firstName; // this instance of the first name. This keyword refers to module level variable
        this.lastName = lastName;
    }
    
    public void setFirstNAme(String firstName){
        
        if (firstName.equals(""))
            System.out.println("first name must not be blank");
        
        this.firstName = firstName;
        
    }
    
    public String getFirstName(){
       return this.firstName;
    }
    
    public void setLastName(){
        this.lastName = lastName;
    }
    
    public String getLastName(String lastName){
        return this.lastName;
        
    }
    
    public String getFullName(String firstName, String lastName){
        return this.firstName+""+this.lastName;
    }

    public String getGreeting (){
        return "Hello " + getFirstName();
    }
    
    
    
    
    
}
    

