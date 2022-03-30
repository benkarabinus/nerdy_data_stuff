/*
Name: Ben Karabinus
Project: Chapter 20 exercise 4 Product Manager
Date: 11/7/19
Description: This project demonstrates the ability to connect to a MySQL database
using a Java 8 application.
Aside: no inline comments were added to this class noo code was edited
*/
package murach.db;

/* 
 * This is just a wrapper class so we can throw a common exception for
 * the UI to catch without tightly coupling the UI to the database layer.
 */
public class DBException extends Exception {
    DBException() {}
    
    DBException(Exception e) {
        super(e);
    }
}