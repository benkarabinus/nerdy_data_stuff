
package phonenumberproject_xyz_bdak;

/**
 *
 * @author Ben Karabinus
 * Date: 9/26/19
 * Desc: Storing and formatting phone numbers
 */
public class PhoneNumber {
    
    private String areaCode;
    private String exchange;
    private String number;
    
    public PhoneNumber(long phoneNumberInput){
        //Good example of the StringBuilder class
        StringBuilder myNumber = new StringBuilder(Long.toString(phoneNumberInput));
        
        areaCode = myNumber.substring(0, 3); // up to but not including 3 !!!
        exchange = myNumber.substring(3, 6); // including 3 up to but not including 6 !!!
        number = myNumber.substring(6);
    }// end of long constructor
    
    public PhoneNumber(String phoneNumberInput){
        
        int firstDash = phoneNumberInput.indexOf("-");
        int secondDash = phoneNumberInput.lastIndexOf("-");
        
        areaCode = phoneNumberInput.substring(0,firstDash);
        exchange = phoneNumberInput.substring(firstDash,secondDash);
        number = phoneNumberInput.substring(secondDash+1);
    }
    
    public String getAreaCode(){
        return areaCode;
    }
    
    public String getExchange(){
        return exchange;
    }
    
    public String getNumber(){
        return number;
    }
    
    public String getFormattedNumber(){
        return "(" +areaCode +")"  +exchange+ "-" + number;
    }
    
    
} // end of class

