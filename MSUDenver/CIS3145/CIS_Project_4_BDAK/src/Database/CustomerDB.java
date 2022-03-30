/*
Name: Ben Karabinus
Project: CIS 3145 Project 4
Date: 11/23/19
Description: This project shows basic understanding of multi-tiered applications 
in Java 8
 */
package Database;

import Business_Logic.Customer;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

//begining class CustomerDB
public class CustomerDB {
    
    //return customer object from the result set pulled from underlying database
    private static Customer getCustomerFromRow(ResultSet rs) throws SQLException {
        
        
        int userID = rs.getInt(1);
        String firstName = rs.getString(2);
        String lastName = rs.getString(3);
        String email = rs.getString(4);
        
        //create new customer object
        Customer customer = new Customer(userID, firstName, lastName, email);
        
        return customer;
    }
    
    //create and store result set of all customers in database
    public static List<Customer> getAll() throws DatabaseException {
        
        //create prepared statement
        String sql = "SELECT * FROM Customer;";
        
        //create array list to store customer objects
        List<Customer> customers = new ArrayList<>();
        
        //establish database connection
        Connection connection = DatabaseUtility.getConnection();
        
        //try prepared statement
        try (PreparedStatement ps = connection.prepareStatement(sql);
                ResultSet rs = ps.executeQuery()) {
            
            //while result set is not null append customer objects to customers
            while (rs.next()) {
                Customer customer = getCustomerFromRow(rs);
                customers.add(customer);
            }
            rs.close();
            //return array list cistomers
            
            return customers;
            
            //handle database exception
        } catch (SQLException e) {
            throw new DatabaseException(e);
        }
    }
    
    //create result set returning customer based on CustomerID
    public static Customer get(int userID) throws DatabaseException {
        
        //create prepared statement
        String sql = "SELECT * FROM Customer WHERE CustomerID = ?";
        
        //establish connection
        Connection connection = DatabaseUtility.getConnection();
        
        //implement prepared statement
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setInt(1, userID);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                Customer customer = getCustomerFromRow(rs);
                rs.close();
                return customer;
            } else {
                rs.close();
                return null;
            }
            //handle database exception
        } catch (SQLException e) {
            throw new DatabaseException(e);
        }
    }
    
    //add new customer to the database
    public static void add(Customer customer) throws DatabaseException {
        
        //create prepared statement
        String sql
                = "INSERT INTO Customer (FirstName, LastName,"
                + " EmailAddress) "
                + "VALUES (?, ?, ?)";
        
        //establish connection
        Connection connection = DatabaseUtility.getConnection();
        
        //implement prepared statement
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
           
           //assign attributes to customer object
           // ps.setInt(1, customer.getUserID());
            ps.setString(1, customer.getFirstName());
            ps.setString(2, customer.getLastName());
            ps.setString(3, customer.getEmail());
            ps.executeUpdate();
            
            //catch database exception
        } catch (SQLException e) {
            throw new DatabaseException(e);
        }
    }
    
     //update customer information
     public static void update(Customer customer) throws DatabaseException {
        
        //create prepared statement
        String sql = "UPDATE Customer SET "
                + "CustomerID = ?, "
                + "FirstName = ?, "
                + "LastName = ?, "
                + "EmailAddress = ?"
                + "Where CustomerID = ?";
        
        //establish database connection
        Connection connection = DatabaseUtility.getConnection();
        //execute prepared statement
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setInt(1, customer.getUserID());
            ps.setString(2, customer.getFirstName());
            ps.setString(3, customer.getLastName());
            ps.setString(4, customer.getEmail());
            ps.setInt(5, customer.getUserID());
            ps.executeUpdate();
            
          //catch database exception
        } catch (SQLException e) {
            throw new DatabaseException(e);
        }
    }
     
     //delete customer from the database
     public static void delete(Customer customer)
            throws DatabaseException {
        
        //create prepared statement
        String sql = "DELETE FROM Customer "
                + "WHERE CustomerID = ?";
        
        //establish database connection
        Connection connection = DatabaseUtility.getConnection();
        
        //execute prepared statement
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setLong(1, customer.getUserID());
            ps.executeUpdate();
            
            //catch sql exception
        } catch (SQLException e) {
            throw new DatabaseException(e);
        }
    }
    
}
