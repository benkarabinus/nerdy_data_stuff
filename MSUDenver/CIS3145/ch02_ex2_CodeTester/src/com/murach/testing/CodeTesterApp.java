/*
Author: Ben Karabinus
Project:ch02_ex2_CodeTester_BDAK
Date: 8/20/19
Description: This project was created to display understanding of basic java syntax
*/

package com.murach.testing;

import java.util.Random;

public class CodeTesterApp {
    public static void main(String args[]) {
        //initializ variables
        double x = 5;
        double y = 3;
        double width = 4.25;
        double length = 8.5;
        double perimeter = 0;
        // display a welcome message
        System.out.println("Welcome to the Code Tester\n");
        
        
        // enter test code here
        System.out.println("The value of x is: " + x +"\n");
        System.out.println("The value of y is: " + y + "\n");
        System.out.println(x+"/"+ y + " = " +(x/y) + "\n");
        System.out.println("Could not find folder named \"C:\\Program Files\\Test\" \n");
        width = 16.75; //width now = 16.75
        System.out.println("Width: " + width);
        System.out.println("Length: "+ length);
        perimeter = 2 * width +  2 * length;
        System.out.println("Perimeter: "+ perimeter+ "\n");
      
        
        System.out.println("Bye!");
    }
}
