/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
*/

package murach.business;

import java.text.NumberFormat;

public class Product {

    private String code;
    private String description;
    private double price;
 
    //new default constructor
    public Product(){
        this("","",0);
    }
//this constructor was added to deal with null pointer exception
//this addition was not required for the completion of this project
    public Product(String productCode) {
        code = productCode;
        description = "unknown";
        price = 0;
    }
    
    
    //product object constructor
    public Product(String code, String description, double price) {
        this.code = code;
        this.description = description;
        this.price = price;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getPrice() {
        return price;
    }

    public String getPriceFormatted() {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        return currency.format(price);
    }

}