/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package helloenumeration_bdak;

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
        
  
        
        this.firstName = firstName;
        
    }
    
    public String getFirstName(){
       return this.firstName;
    }
    
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    
    public String getLastName(String lastName){
        return this.lastName;
        
    }
    
    public String getFullName(){
        return this.firstName+" "+this.lastName;
    }
    
    public String getGreeting(LanguageType language){
        String message = "";
        if(language == LanguageType.FRENCH)
            message = "Bongjour";
        else if( language == LanguageType.ENGLISH)
            message = "Hello";
        else if (language == LanguageType.SPANISH)
            message = "Hola";
    return message +" " +getFullName() + ". Your Language is "+
            language.toString();
}

    
    
    
    
    
}
    

