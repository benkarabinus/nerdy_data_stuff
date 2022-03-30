/*
Name: Ben Karabinus
Project Name: CH_10_ex03
Date: 10/3/19
Description: This project shows basic understanding of two dimesional arrays in Java
*/

package murach.db;

import java.util.HashSet;
import java.util.Set;
import murach.business.Product;

public class ProductDB {
    private static String[][] productsArray = {
        {"java", "Murach's Java Programming", "57.50"},
        {"jsp", "Murach's Java Servlets and JSP", "57.50"},
        {"mysql", "Murach's MySQL", "54.50"},
        //the line below may be uncommented for testing purposes
       // {"Python", "Murach's Python", "55.00"}
    };
    
    public static Product getProductByIndex(int i) {
        // TODO: Add code here to return Product object
        
        //construct new product object
        Product product = new Product();
        
        //Set fields or attributes of product object based upon index "i"
        //The provided "i" will be the row index of productsArray
        /* If more fields where added to the Product class code would need to be 
        editied regardless. For the purpose of this project the solution below
        achieves the objective.
        */
        product.setCode(productsArray[i][0]);//set code 
        product.setDescription(productsArray[i][1]);//set description
        product.setPrice(Double.parseDouble(productsArray[i][2]));//set price
        
        return product;
    }
    
    public static Product getProductByCode(String code) {
        // TODO: Add code here to return Product object
        
        //Construct new Product object
        Product product = new Product();
        
        //enhanced for loop used to cycle through 2 dimesional array 
        for(String[] row:productsArray){
            for(String column: row){
                
                //test for string equality to match codes
                if (column.equalsIgnoreCase(code)){
                    
                    //set fields or attributes if above condition is true
                    product.setCode(row[0]);//set code
                    product.setDescription(row[1]);//set description
                    product.setPrice(Double.parseDouble(row[2]));//set price
                }
            }
        }
        return product;
    }
    
    public static Product[] getAllProducts() {
        // TODO: Add code here to return array of Product object
        
        //Create an array for product objects dynamically sized
        Product [] products = new Product[productsArray.length];
        
        //Method #1 using regualr for loop
//        for (int i = 0; i < 3; i++){
//                Product product = new Product();
//                product.setCode(productsArray[i][0]);
//                product.setDescription(productsArray[i][1]);
//              
//                product.setPrice(Double.parseDouble(productsArray[i][2]));
//                products[i] = product;
//            }

        //Method #2 using enhanced for loop and variable i
        
        int i = 0;// declaration variable "i"
        
        for( String[] myProduct : productsArray){
            
            //new Product object is created each iteration
            Product product = new Product();
            product.setCode(myProduct[0]);//set code
            product.setDescription(myProduct[1]);//set description
            product.setPrice(Double.parseDouble(myProduct[2]));//set price
            products[i] = product;//add product object to products[i]
            i++;
            /* The variable i ensures that each new Product object is added to the 
               next available index in the array products. This variable is
               incremented with each iteration
            */
            
        }
     
        
        return products;
    }    
}