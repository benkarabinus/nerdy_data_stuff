/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fishapp;

import FishData.FishyData;
import FishyBusiness.FishLine;
import FishyBusiness.FishyActions;
import java.util.Scanner;

/**
 *
 * @author owner
 */
public class FishApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        
        System.out.println("welcome to the fish app");
        System.out.println("Enter Fish:");
        String name = sc.nextLine();
        FishyActions fish = FishyData.getFish(name);
        System.out.println("Enter number  of orders: ");
        int qnty = Integer.parseInt(sc.nextLine());
        FishLine order = new FishLine(fish, qnty);
        
        System.out.println("Type: "+ fish.getFishType());
        System.out.println("FLavor Profile: "+fish.getFishProfile());
        System.out.println("Price: "+ fish.getFishPrice());
        System.out.println("Quantity: " +order.getQnty());
        System.out.println("Total: "+ order.getTotalFormatted());
        System.out.println("Bye");
        
    }
    
}
