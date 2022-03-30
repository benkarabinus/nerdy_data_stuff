/*
 * Ben Karabinus
 * Project: Chapter 11 exercise 4 Product
 * Date: 10/10/19
 * Description: This project demonstrates low level understanding of inheritance
 * using the Java programming language
 */
package murach.business;

import java.text.NumberFormat;

public class MyProduct extends Product {
    
    //default constructor calls constructor of the superclass
    public MyProduct(){
        super();
    }
    //getPrice accepts NumberFormat object nf and returns priceFormatted
    public String getPrice(NumberFormat nf){
        //to access price use the "this" keyword followed by get price method 
        String priceFormatted = nf.format(this.getPrice());
        return priceFormatted;
        
    }
    
}
