/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package arraysorting_bdak;

import java.util.Arrays;

/**
 *
 * @author owner
 */
public class SortPeopleApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Person person01 = new Person("Sue","Smith");
        Person person02 = new Person("Bob","Burt");
        Person person03 = new Person("John", "Johnson");
        
        Person [] personArray = new Person[3];
        
        personArray[0] = person01;
        personArray[1] = person02;
        personArray[2] = person03;
        
        System.out.println("Unsorted List");
        
        for(int i =0; i < personArray.length; i++){
            
            System.out.println(personArray[i].getFirstName());
           
        }
        
        Arrays.sort(personArray);
        System.out.println("");
        System.out.println("Sorted Array");
        
        for (Person p : personArray) {
            System.out.println(p.getFirstName());
        }
    }
    
}
