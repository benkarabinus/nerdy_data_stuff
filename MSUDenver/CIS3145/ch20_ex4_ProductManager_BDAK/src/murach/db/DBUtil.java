/*
Name: Ben Karabinus
Project: Chapter 20 exercise 4 Product Manager
Date: 11/7/19
Description: This project demonstrates the ability to connect to a MySQL database
using a Java 8 application.
Aside: no inline comments were added to this class no code was edited
*/
package murach.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBUtil {
    
    private static Connection connection;
    
    private DBUtil() {}

    public static synchronized Connection getConnection() throws DBException {
        if (connection != null) {
            return connection;
        }
        else {
            try {
                // set the db url, username, and password
                String url = "jdbc:mysql://localhost:3306/mma";
                String username = "mma_user";
                String password = "sesame";

                // get and return connection
                connection = DriverManager.getConnection(
                        url, username, password);
                return connection;
            } catch (SQLException e) {
                throw new DBException(e);
            }            
        }
    }
    
    public static synchronized void closeConnection() throws DBException {
        if (connection != null) {
            try {
                connection.close();
            } catch (SQLException e) {
                throw new DBException(e);
            } finally {
                connection = null;                
            }
        }
    }
}