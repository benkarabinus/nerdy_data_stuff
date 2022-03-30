/*
 * Ben Karabinus
 * Project: Chapter 11 exercise 4 Product
 * Date: 10/10/19
 * Description: This project demonstrates low level understanding of inheritance
 * using the Java programming language
 */

package murach.db;

import murach.business.MyProduct;
import murach.business.Product;

public class ProductDB {

    public Product getProduct(String productCode) {
        // In a more realistic application, this code would
        // get the data for the product from a database
        // For now, this code just uses if/else statements
        // to return the correct product data

        //new code creates MyProduct object
        MyProduct mProduct = new MyProduct();

        //fill the MyProduct object with data
        mProduct.setCode(productCode);
        if (productCode.equalsIgnoreCase("java")) {
            mProduct.setDescription("Murach's Java Programming");
            mProduct.setPrice(57.50);
        } else if (productCode.equalsIgnoreCase("jsp")) {
            mProduct.setDescription("Murach's Java Servlets and JSP");
            mProduct.setPrice(57.50);
        } else if (productCode.equalsIgnoreCase("mysql")) {
            mProduct.setDescription("Murach's MySQL");
            mProduct.setPrice(54.50);
        } else {
            mProduct.setDescription("Unknown");
        }
        //return the MyProduct object
        return mProduct;
    }
}