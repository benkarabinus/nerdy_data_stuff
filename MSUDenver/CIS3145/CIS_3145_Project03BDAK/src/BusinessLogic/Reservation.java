/*
Name: Ben Karabinus
Project Name: CIS 3145 Project 3
Date: 10/29/2019
Descripton: This Project shows basic understanding of working with dates in java 8
 */
package BusinessLogic;

import java.text.NumberFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;


public class Reservation {
    
    //declaration of instance variables for the class Reservation
    private LocalDate arrivalDate;
    private LocalDate departureDate;
    private static final double NIGHTLY_RATE = 95.00;
    
    //create DateTimeFormatter object 
    DateTimeFormatter dtf = DateTimeFormatter
                .ofLocalizedDate(FormatStyle.LONG);
    //create NumberFormat object 
    NumberFormat currency = NumberFormat.getCurrencyInstance();
    
    //default constructor
    public Reservation (){
        
    }
    
    //set method for the arrivalDate variable
    public void setArrivalDate(LocalDate arrivalDate){
        this.arrivalDate = arrivalDate;
    }
    
   //set method for the departureDate variable
   public void setDepartureDate(LocalDate departureDate){
       this.departureDate = departureDate;
   }
   
   //get method for the arrivalDate variable
   public LocalDate getArrivalDate(){
       return arrivalDate;
   }
   
   //get method for the departureDate variable
   public LocalDate getDepartureDate(){
       return departureDate;
   }
   
   //return the arrivalDate variable formatted
   public String getArrivalDateFormatted(){
       return dtf.format(arrivalDate);
   }
   
   //return the departureDate variable formatted
   public String getDepartureDateFormatred(){
        return dtf.format(departureDate);
   }
   
   //return the difference (in days) between departure and arrival date
   public int getNumberOFNights(){
       
       long arrival = arrivalDate.toEpochDay();
       long departure = departureDate.toEpochDay();
       
       return (int) (departure - arrival);
   }
   
   //return the total cost of the guests stay
   public double getTotalPrice(){
        
       return (getNumberOFNights() * NIGHTLY_RATE);
   }
   
   //return the pricePerNight variable formatted
   public String getPricePerNightFormatted(){
       
       return currency.format(NIGHTLY_RATE); 
   }
   
   //return the output of the getTotalPrice method formatted
   public String getTotalPriceFormatted(){
       return currency.format(this.getTotalPrice());
   }
    
    
}
