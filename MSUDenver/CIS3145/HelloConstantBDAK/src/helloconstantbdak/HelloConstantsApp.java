/*
 * Ben Karabinus
 * Date:9/12/19
 * Progrma using constants and modulous operations
 * 
 */
package helloconstantbdak;
import java.util.Scanner;

/**
 *
 * @author owner
 */
public class HelloConstantsApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int counter = 0;
        String firstName;
        String lastName;
        String middleName;
        char middleInitial;
        
        final String ENGLISH = "Hello";
        final String FRENCH = "Salut";
        final String SPANISH = "Hola";
        
        String greeting = "";
        Scanner sc = new Scanner(System.in);
        
        System.out.print("");
        System.out.print("");
        System.out.print("");
        
        String choice = "y";
        
        while(!choice.equalsIgnoreCase("n")){
            //ask for name input
            System.out.print("Please enter your first name ");
            firstName = sc.nextLine();
            System.out.print("Please enter your middle name ");
            middleName = sc.nextLine();
            System.out.print("Please enter your last name ");
            lastName = sc.nextLine();
            
            
            
            
            
            middleInitial = middleName.charAt(0);
            System.out.println(Integer.toString(middleInitial));
             if (middleInitial % 3 == 0){
                 greeting = ENGLISH;
             }
             
             else if (middleInitial %3 == 1)
                 greeting = FRENCH;
             else if (middleInitial % 3 ==2)
                     greeting = SPANISH;
             
             //Print Output
             
             String message = greeting + firstName + 
                     middleInitial + lastName;
             System.out.println();
             System.out.print(message+ "\n");
              counter ++;
             System.out.print("Would you like to continue?\n ");
            choice = sc.nextLine();
             
        } // end of while loop
        
        if (counter % 2 == 0)
            System.out.println("You displayed "+ counter+ "cnames. That's "
                    + "even better than I thpught.");
        else
            System.out.println("You displayed "+ counter+"names."
                    + "That's an odd thing to do.");
    }// end of main
    
}
