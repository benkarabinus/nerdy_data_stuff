/*
Name: Ben Karabinus
Project Name: CH_10_ex03
Date: 10/3/19
Description: This project shows basic understanding of two dimesional arrays in Java
*/

package murach.ui;

import murach.business.Product;
import murach.db.ProductDB;

public class Main {
    
    //Static method to create product object by code
    public static void main(String[] args) {
        Product product = ProductDB.getProductByCode("jsp");
        System.out.println("PRODUCT BY CODE");
        System.out.println("Code:        "+ product.getCode());//print code
        System.out.println("Description: "+ product.getDescription());//print description 
        System.out.println("Price:       "+ product.getPriceFormatted());//print price
        System.out.println("----------------------------------------------");
    //Static mehod to create product object by index   
        product = ProductDB.getProductByIndex(0);
        System.out.println("PRODUCT BY INDEX");
        System.out.println("Code:        "+product.getCode());//print code
        System.out.println("Description: "+product.getDescription());//print description
        System.out.println("Price:       "+product.getPriceFormatted());//print price
        System.out.println("----------------------------------------------");
        //create an array of product objects using static method getAllProducts
        Product[] products = ProductDB.getAllProducts();
        //Print the contents of the products array to the console
        System.out.println("LIST OF ALL PRODUCTS");//for loop cycles through products array
        for (int i = 0; i < products.length; i++) {
            System.out.println("Code:        "+products[i].getCode());//print code
            System.out.println("Description: "+products[i].getDescription());//print description
            System.out.println("Price:       "+products[i].getPriceFormatted());//print price        
            System.out.println();
        }            
        System.out.println("----------------------------------------------");        
    }    
}