/*
 * Ben Karabinus
 * Project: Chapter 11 exercise 4 Product
 * Date: 10/10/19
 * Description: This project demonstrates low level understanding of inheritance
 * using the Java programming language
 */
package murach.ui;

import java.text.NumberFormat;
import java.util.Scanner;
import murach.business.MyProduct;
import murach.db.ProductDB;

public class ProductApp {

    public static void main(String args[]) {
        // display a welcome message
        System.out.println("Welcome to the Product Viewer");
        System.out.println();

        // create 1 or more line items
        Scanner sc = new Scanner(System.in);
        String choice = "y";
        while (choice.equalsIgnoreCase("y")) {
            // get input from user
            System.out.print("Enter product code: ");
            String productCode = sc.nextLine();

            // Use a ProductReader object to get the Product object
            ProductDB db = new ProductDB();
            //this code was changed to create a "MyProduct" object
            MyProduct mProduct = (MyProduct) db.getProduct(productCode);
            
            // Number format object "nf" created to format the variable "price"
            NumberFormat nf = NumberFormat.getCurrencyInstance();
            
            //all code below has been changed to reference a MyProduct object
            String message = "\nPRODUCT\n" +
                "Code:        " + mProduct.getCode() + "\n" +
                "Description: " + mProduct.getDescription() + "\n" +
                "Price:       " + mProduct.getPrice(nf) + "\n";
            System.out.println(message);

            // see if the user wants to continue
            System.out.print("Continue? (y/n): ");
            choice = sc.nextLine();
            System.out.println();
        }
        System.out.println("Bye!");
    }    
}