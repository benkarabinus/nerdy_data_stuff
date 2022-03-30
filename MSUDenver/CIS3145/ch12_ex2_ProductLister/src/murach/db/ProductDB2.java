/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
*/

package murach.db;

import murach.business.Product;

//delcare the class ProductDB2 and implement IProdcutDB interface
public class ProductDB2 implements IProductDB {
    
    private String[][] productsArray = {
        {"java", "Murach's Java Programming", "57.50"},
        {"jsp", "Murach's Java Servlets and JSP", "57.50"},
        {"android", "Murach's Android Programming", "57.50"},
        {"mysql", "Murach's MySQL", "54.50"}
    };
//comment out the original code listed below   
//    public Product getProduct(String productCode) {
//        for (String[] row : productsArray) {
//            String code = row[0];
//            if (productCode.equals(code)) {
//                String description = row[1];
//                String price = row[2];        
//                Product p = new Product(
//                        code, description, Double.parseDouble(price));                
//                return p;
//            }
//        }
//        return null;
//    }
//    
    @Override //override allows for customization of IProductDB get method
    public Product get(String productCode){
       for (String[] row : productsArray) {
            String code = row[0];
            if (productCode.equals(code)) {
                String description = row[1];
                String price = row[2];        
                Product p = new Product(
                        code, description, Double.parseDouble(price));
                return p;
            }
        
                
            }
       //this return statement was added to handle null pointer exception
       //this addition was not reqired for successful completion of the project
       Product p = new Product(productCode);
                return p;
        //return null;
    }
}