package Business_Action;
/*
 *Author: Ben Karabinus
 *Project: CIS 3145 Project #1
 *Date: 9/10/19
 *Description: This project demonstrates low level understanding of
 * multi-tiered applications
 */

public class Customer {
    //instance variable declaration for customer object
    private String name;
    private String address;
    private String city;
    private String state;
    private String zip;
    
    //default constructor (technically not needed java will create for you)
    public Customer(){
        
    }
    //Customer constructor
    public Customer(String name, String address, String city, String state, String zip){
        
        this.name = name;
        this.address = address;
        this.city = city;
        this.state = state;
        this.zip = zip;
    }
    //Set methods
    public void setName(String name){
        this.name = name;
    }
    
    public void setAddress(String address){
        this.address = address;
    }
    
    public void setCity(String city){
        this.city = city;
    }
    
    public void setState(String state){
        this.state = state;
    }
    
    public void setZip(String zip){
        this.zip = zip;
    }
    //Get methods
    public String getName(){
        return name;
    }
    
    public String getAddress(){
        return address;
    }
    
    public String getCity(){
        return city;
    }
    
    public String getState(){
        return state;
    }
    
    public String getZip(){
        return zip;
    }
    //Special get method to return formatted customer attributes
    public String getNameAndAddress(){
        
        String nameAddressFormatted = name + "\n" + address + "\n" + city + ", " + state + " "+ zip;
        
        return nameAddressFormatted;           
    }
}
