
package phonenumberproject_xyz_bdak;

/**
 *
 * @author Ben Karabinus
 * Date: 9/26/19
 * Desc: Storing and formatting phone numbers
 */
public class PhoneNumberApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        long myPhoneNumber = 9871234560l; //important highlight "l" at the end
        
        
        PhoneNumber number1 = new PhoneNumber(myPhoneNumber);
        System.out.println("Thee first number is: "+ number1.getFormattedNumber());
        
        PhoneNumber number2 = new PhoneNumber("987-123-0456");
        System.out.println("The second number is: "+number2.getFormattedNumber());
        
    }
    
}
