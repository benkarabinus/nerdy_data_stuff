/*
Name: Ben Karabinus
Project: CIS 3145 Project 4
Date: 11/23/19
Description: This project shows basic understanding of multi-tiered applications 
in Java 8
 */
package Database;


public class DatabaseException extends Exception {
    DatabaseException() {}
    
    DatabaseException(Exception e) {
        super(e);
    }
}