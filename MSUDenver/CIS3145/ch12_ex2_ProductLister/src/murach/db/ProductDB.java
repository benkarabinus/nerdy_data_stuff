/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
*/

package murach.db;

import murach.business.Product;

//delcare the class ProductDB and implement IProdcutDB interface
public class ProductDB implements IProductDB { 

//comment out the original code listed below
//    public Product getProductByCode(String productCode) {
        // In a more realistic application, this code would
        // get the data for the product from a file or database
        // For now, this code just uses if/else statements
        // to return the correct product

        // create the Product object
//        Product product = new Product();

        // fill the Product object with data
//        product.setCode(productCode);
//        if (productCode.equalsIgnoreCase("java")) {
//            product.setDescription("Murach's Java Programming");
//            product.setPrice(57.50);
//        } else if (productCode.equalsIgnoreCase("jsp")) {
//            product.setDescription("Murach's Java Servlets and JSP");
//            product.setPrice(57.50);
//        } else if (productCode.equalsIgnoreCase("mysql")) {
//            product.setDescription("Murach's MySQL");
//            product.setPrice(54.50);
//        } else {
//            product.setDescription("Unknown");
//        }
//        return product;
//    }
    
    
    
    //override allows for customization of IProductDB interface get method
    @Override 
    
    public Product get(String productCode) {
        Product product = new Product();//construct Product object
        
        // fill the Product object with data
        product.setCode(productCode);
        if (productCode.equalsIgnoreCase("java")) {
            product.setDescription("Murach's Java Programming");
            product.setPrice(57.50);
        } else if (productCode.equalsIgnoreCase("jsp")) {
            product.setDescription("Murach's Java Servlets and JSP");
            product.setPrice(57.50);
        } else if (productCode.equalsIgnoreCase("mysql")) {
            product.setDescription("Murach's MySQL");
            product.setPrice(54.50);
        } else {
            product.setDescription("Unknown");
        }
        return product;
    }
    
}