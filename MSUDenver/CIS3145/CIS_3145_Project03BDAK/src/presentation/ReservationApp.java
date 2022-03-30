/*
Name: Ben Karabinus
Project Name: CIS 3145 Project 3
Date: 10/29/2019
Descripton: This Project shows basic understanding of working with dates in java 8
 */
package presentation;
import BusinessLogic.Reservation;
import java.time.LocalDate;
import java.util.Scanner;

public class ReservationApp {

    
    public static void main(String[] args) { //begining brace of the main method
        
        //Print welcome message to the console
        System.out.println("Reservation Calculation System Startup");
        System.out.println();
        
        //create scanner object to take user input
        Scanner sc = new Scanner(System.in);
        //create reservation object to store and manipulate reservation data
        Reservation reservation = new Reservation();
        
        //choice is the loop control variable
        String choice = "y";
        
        
        
        //control loop allows the user to end or continue the program
        while (choice.equalsIgnoreCase("y")){
            
            //prompt the user for arrival info
            
            try{
                System.out.print("Enter the arrival month (1-12): ");
                int arrivalMonth = Integer.parseInt(sc.nextLine());
                 System.out.print("Enter the arrival day (1-31): ");
                int arrivalDay = Integer.parseInt(sc.nextLine());
                System.out.print("Enter the arrival year: ");
                int arrivalYear = Integer.parseInt(sc.nextLine());
                //create a LocalDate object to store the arrival date
                LocalDate arrivalDate = LocalDate.of(arrivalYear,arrivalMonth,
                arrivalDay);
                //set the arrival date
                reservation.setArrivalDate(arrivalDate);
            }catch(NumberFormatException e){
                System.out.println();
                System.out.print("Please enter a valid number.\n");
                System.out.print("Would you like to try again (y/n): ");
                choice = sc.nextLine();
                System.out.println();
                continue;
            }
           
            System.out.println();
            
            //prompt the user for departure info
            try{
                System.out.print("Enter the departure month (1-12): ");
                int departureMonth = Integer.parseInt(sc.nextLine());
                System.out.print("Enter the departure day (1-31): ");
                int departureDay = Integer.parseInt(sc.nextLine());
                System.out.print("Enter the departure year: ");
                int departureYear = Integer.parseInt(sc.nextLine());
                //create a LocalDate object to store the departure date
                LocalDate departureDate = LocalDate.of(departureYear,departureMonth,
                    departureDay);
                //set the departure date
                reservation.setDepartureDate(departureDate);
                System.out.println();
            }catch(NumberFormatException e){
                System.out.println();
                System.out.print("Please enter a valid number.\n");
                System.out.print("Would you like to try again (y/n): ");
                choice = sc.nextLine();
                System.out.println();
                continue;
            }
            
            //print reservation details to the console
            System.out.println("Arrival Date: "+reservation.getArrivalDateFormatted());
            System.out.println("Departure Date: "+reservation.
                getDepartureDateFormatred());
            System.out.println("Price "+reservation.
                    getPricePerNightFormatted()+ " per night");
            System.out.println("Total price " +reservation.
                    getTotalPriceFormatted()+ " for "+
                    reservation.getNumberOFNights()+ " nights");
            System.out.println();
            
            //prompt the user to continue using the app
            System.out.print("Continue (y/n): ");
            choice = sc.nextLine();
            System.out.println();
        }
        
    }
    
}
