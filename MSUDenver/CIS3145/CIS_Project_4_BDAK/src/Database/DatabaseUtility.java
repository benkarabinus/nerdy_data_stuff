/*
Name: Ben Karabinus
Project: CIS Project 4
Date: 11/23/19
Description: This project shows basic understanding of multi-tiered applications 
in Java 8
 */

package Database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

//create DatabaseUtility class
public class DatabaseUtility {
    
    private static Connection connection; //instance variable type "connection"
    
    
    private DatabaseUtility() {}
    
    //attempt to establish connection
    public static synchronized Connection getConnection() throws DatabaseException {
        if (connection != null) {
            return connection;
        }
        else {
            try {
                // set the db url, username, and password"
                String url = "jdbc:mysql://localhost:3306/mma";
                String username = "mma_user";
                String password = "sesame";

                // get and return connection
                connection = DriverManager.getConnection(
                        url, username, password);
                return connection;
                
                //handle database exception
            } catch (SQLException e) {
                throw new DatabaseException(e);
            }            
        }
    }
    
    //close database connection
    public static synchronized void closeConnection() throws DatabaseException {
        if (connection != null) {
            try {
                connection.close();
                
                //handle database exception
            } catch (SQLException e) {
                throw new DatabaseException(e);
            } finally {
                connection = null;                
            }
        }
    }
}