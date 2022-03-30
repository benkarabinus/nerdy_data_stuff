/*
Name: Ben Karabinus
Project: Chapter 17 exercise 3
Date: 10/31/19
Description: This project shows basic understanding of writing to and printing
from a text file
*/

package murach.rectangle;
import java.io.*;


public class RectangleIO {
    
    //create static variable to represent the file "rectangle.txt"
    static String file = "rectangle.txt";
    
    public static void save(Rectangle r){
        
        //try block is used to handle IO exception
        try {
            //method chaining is used to create the input stream
            PrintWriter rectangleWriter = new PrintWriter(
                    new BufferedWriter(
                            new FileWriter(file,true)));
            //the length, width, area, and perimeter of each rectangle is written
            rectangleWriter.println(r.getLength()+"|"+r.getWidth()+"|"
                    +r.getAreaNumberFormat()+"|"+
                    r.getPerimeterNumberFormat());
            rectangleWriter.close();//Close and flush the file
            
        } catch (IOException ex) {
            System.out.println("IO exception occured. Oops!");
        }
    }
   
    
    public static void printFile(){
        
        System.out.println("RECTANGLES (length|width|area|perimeter)");
        //try block is used to handle IO and file not found exception
        try {
            
            //method chaining is used to create the output stream
            BufferedReader rectangleIn = new BufferedReader(
                    new FileReader(file));
            
            //declaration of temporary storage variable "line"
            String line;
            
            //while loop is used to read txt file contents 1 line at a time
            while((line = rectangleIn.readLine()) != null){
                
                //print each line to the console
                System.out.println(line);
            }
            rectangleIn.close();//close and flush the file
            
            /*
            The warning messages at lines 21 and 40 are attempting to add a try
            with resources statement. This statement essentially flushes and 
            closes the file. Instead I used the .close() method since its what
            we went over in class.
            */
            
        } catch (FileNotFoundException ex) {
            System.out.println("Oops the file you're attempting to read was not"
                    + "found");
        } catch (IOException ex) {
            System.out.println("An IO exception. Oh No!");
        }
        
    }
}

