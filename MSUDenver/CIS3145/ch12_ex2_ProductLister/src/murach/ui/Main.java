/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
*/

package murach.ui;

import murach.business.Product;
import murach.db.IProductConstants;
import murach.db.IProductDB;
import murach.db.ProductDB;
import murach.db.ProductDB2;

//implements keyword makes IProductConstants interface available to main class
public class Main implements IProductConstants  {

    public static void main(String args[]) {
//the code below instantiates IProductDB object "db"
//comment or uncomment to use either productDB class
        //IProductDB db =new ProductDB();
        IProductDB db = new ProductDB2();
        System.out.println("Welcome to the Product Lister\n");
        
        
        // set up display string
        StringBuilder list = new StringBuilder();
        list.append(StringUtil.pad("Code", CODE_WIDTH));
        list.append(StringUtil.pad("Description", DESC_WIDTH));
        list.append(StringUtil.pad("Price", PRICE_WIDTH));        
        list.append("\n");

        list.append(
            StringUtil.pad("=========", CODE_WIDTH));
        list.append(
            StringUtil.pad("=================================", DESC_WIDTH));
        list.append(
            StringUtil.pad("=========", PRICE_WIDTH));        
        list.append("\n");        
        
        String choice = "y";
        while (choice.equalsIgnoreCase("y")) {
            // get the input from the user
            String productCode = Console.getString("Enter product code: ");

            Product product = db.get(productCode);
            
            list.append(
                StringUtil.pad(product.getCode(), CODE_WIDTH));
            list.append(
                StringUtil.pad(product.getDescription(), DESC_WIDTH));
            list.append(
                StringUtil.pad(product.getPriceFormatted(), PRICE_WIDTH));
            list.append("\n");
            

            // see if the user wants to continue
            System.out.println();
            choice = Console.getString("Another product? (y/n): ");
            System.out.println();
        }
        System.out.println(list);
    }
}