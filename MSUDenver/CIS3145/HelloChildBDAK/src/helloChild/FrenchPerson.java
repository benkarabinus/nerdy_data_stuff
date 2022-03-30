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
public class FrenchPerson extends Person {
    
    public FrenchPerson(){
        
        super("Marie", "Dupont");
    }
    
    
    public FrenchPerson (String firstName, String lastName){
        
        super(firstName,lastName);
    }
    
    @Override
     public String getGreeting (){
        return "Bonjur " + getFirstName();
    }
}

    