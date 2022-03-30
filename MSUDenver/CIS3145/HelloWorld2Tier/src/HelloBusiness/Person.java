/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package HelloBusiness;

/**
 *
 * @author owner
 */
public class Person {
    
    String firstName;
    String lastName;
    
    public Person(){
        firstName = "Jane";
        lastName = "Doe";
    }
    
    public Person(String firstName, String lastName){
        
        this.firstName =firstName;
        this.lastName = lastName;
    }
    
    public void setFirstName(){
        this.firstName = firstName;
    }
    
    public void setLastName(){
        this.lastName = lastName;
    }
    
    public String getFirstName(){
        return this.firstName;
    }
    
    public String getLastName(){
        return this.lastName;
    }
    
    public String getFullName(){
        return (this.firstName+""+this.lastName);
    }
}
