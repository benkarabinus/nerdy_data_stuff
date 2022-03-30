
package helloenumeration_bdak;

import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;

/**
 * Date: October 24, 2019
 * @author Ben Karabinus
 * Description: Creating a language Enumeration and process dates
 */
public class HelloDateApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Person person = new Person("Ben","Karabinus");
        System.out.println(person.getGreeting(LanguageType.ENGLISH));
        System.out.println(person.getGreeting(LanguageType.FRENCH));
        System.out.println(person.getGreeting(LanguageType.SPANISH));
        
        LocalDate localToday = LocalDate.now();
        LocalDate localXmas = LocalDate.of(2019, Month.DECEMBER, 25);
        
        DateTimeFormatter dtf_medium = DateTimeFormatter.ofLocalizedDate
        (FormatStyle.MEDIUM);
        
        System.out.println("Today's date is "+ dtf_medium.format(localToday));
        
        System.out.println("Christmas is on a "+localXmas.getDayOfWeek());
        
        long localTodayInDays = localToday.toEpochDay();
        System.out.println("The long value of today is: "+ localTodayInDays);
        
        long localXmasInDays = localXmas.toEpochDay();
        System.out.println("The long value of Xmas is: " + localXmasInDays);
        
        System.out.println("There are " + (localXmasInDays - localTodayInDays)
                + " days until Xmas");
    }
    
}
