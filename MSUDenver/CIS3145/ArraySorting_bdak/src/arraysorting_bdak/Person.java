/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package arraysorting_bdak;

/**
 *
 * @author owner
 */
public class Person implements Comparable {
    
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
    
    public String getFullName(String firsName, String lastName){
        return this.firstName+""+this.lastName;
    }

    @Override
    public int compareTo(Object o) {
         int compareResult = 0;
         
         Person p = (Person) o;
         compareResult = this.lastName.compareTo(p.lastName);
         
         // this > p -> +1
         //this = p -> 0
         // this< p ->-1
         
         return compareResult;
    }

    
    
    
    
    
    
}
    

