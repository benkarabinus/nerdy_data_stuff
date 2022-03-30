/*
Name: Ben Karabinus
Project: Chapter 20 exercise 4 Product Manager
Date: 11/7/19
Description: This project demonstrates the ability to connect to a MySQL database
using a Java 8 application.
*/

package murach.business;

import java.text.NumberFormat;

public class Product {
    //instance variables of the Product class
    private long id;
    private String code;
    private String description;
    private double price;
    private String note;
    
    // product object is created using default constructor
    
    /*
    the 10 methods below are used to either set or return the 
    values of instance variables
    */
    
    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String name) {
        this.description = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
    
    //set method of the note instance variable
    public void setNote(String note){
        this.note = note;
    }
    
    //get method of the note instance variable
    public String getNote(){
        return note;
    }
    
    // the method below returns the price vriable formatted
    
    public String getPriceFormatted() {
        NumberFormat currencyFormatter =
                NumberFormat.getCurrencyInstance();
        return currencyFormatter.format(getPrice());
    }    

}