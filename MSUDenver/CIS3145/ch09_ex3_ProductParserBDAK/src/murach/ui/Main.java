/*
Name: Ben Karabinus
Project Name: CH_09_ex03
Date: 9/26/19
Description: This project shows basic understanding of String manipulation
*/

package murach.ui;

import java.util.HashSet;
import java.util.Set;
import murach.business.Product;


public class Main {

    public static void main(String[] args) {
        String productString1 = "java:Murach's Java Programming:57.50";
        String productString2 = "mysql:Murach's MySQL:54.50";
         
        Product product1 = new Product();      
        Product product2 = new Product();
        
        //TODO: process the productString variables and populate fields of 
        //product objects in the parseString method
        product1 = parseString(productString1, product1);
        product2 = parseString(productString2, product2);
        
        System.out.println("Code:        " + product1.getCode()); //print product1 code to console
        System.out.println("Description: " + product1.getDescription());//print product1 description to console
        System.out.println("Price:       " + product1.getPriceFormatted());//print product1 price to console
        System.out.println("");
        
        System.out.println("Code:        " + product2.getCode());//print product2 code to console
        System.out.println("Description: " + product2.getDescription());//print product2 description to console
        System.out.println("Price:       " + product2.getPriceFormatted());//print product2 price to console
        System.out.println("");
    }    
    
    public static Product parseString (String inputString, Product inputProduct){
        // use String class 'index' amd substring methods to parse the input string parameter 
        // and then set the properties of the inputProduct object
        
        // Method #1 using String class
        int index1 = inputString.indexOf(":");
        int index2 = inputString.indexOf(":",index1+1);
        inputProduct.setCode(inputString.substring(0, index1));
        inputProduct.setDescription(inputString.substring(index1+1,index2));
        inputProduct.setPrice(Double.parseDouble(inputString.substring(index2+1)));
        
         // Method #2 using StringBuilder class
//        StringBuilder input = new StringBuilder(inputString);
//        inputProduct.setCode(input.substring(0, index1));
//        inputProduct.setDescription(input.substring(index1+1,index2));
//        inputProduct.setPrice(Double.parseDouble(input.substring(index2+1)));
        
        
        return inputProduct;
          
    }
}