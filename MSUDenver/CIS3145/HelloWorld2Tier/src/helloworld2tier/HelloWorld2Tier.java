/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package helloworld2tier;

import HelloBusiness.Person;
import java.util.Scanner;

/**
 *
 * @author owner
 */
public class HelloWorld2Tier {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Scanner sc = new Scanner(System.in);
  
        System.out.println("Welcome to the 2 tier hello world application!");
        System.out.println("Please enter your first name: ");
        String firstName = sc.nextLine();
        System.out.println("Please enter your last name: ");
        String lastName = sc.nextLine();
        
        Person defaultPerson = new Person();
        Person person = new Person(firstName, lastName);
        
        System.out.println("Your first name is "+person.getFirstName());
        System.out.println("YOur last name is " +person.getLastName());
        System.out.println("Your  full name is "+person.getFullName());
        
    }
    
}
