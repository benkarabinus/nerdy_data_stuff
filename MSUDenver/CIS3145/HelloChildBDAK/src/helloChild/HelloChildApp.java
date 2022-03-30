/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package helloChild;

/**
 * create child class from the parent class
 * @author owner
 */
public class HelloChildApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Person defaultPerson = new Person();
        System.out.println(defaultPerson.getGreeting());
        
        Person newPerson = new Person("Ben","Karabinus");
        System.out.println(newPerson.getGreeting());
        
        FrenchPerson defaultFrenchPerson = new FrenchPerson();
        System.out.println(defaultFrenchPerson.getGreeting());
        
        FrenchPerson defaultFrenchie = new FrenchPerson("Jean","Louis");
        System.out.println(defaultFrenchie.getGreeting());
        
        Person testPerson = defaultFrenchie;// <- this is implicit assignment
        
        FrenchPerson testFrenchPerson = (FrenchPerson)newPerson; // requires explicit assignment
        
    }
    
}
