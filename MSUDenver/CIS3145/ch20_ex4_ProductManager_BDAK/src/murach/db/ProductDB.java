/*
Name: Ben Karabinus
Project: Chapter 20 exercise 4 Product Manager
Date: 11/7/19
Description: This project demonstrates the ability to connect to a MySQL database
using a Java 8 application.
*/

package murach.db;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import murach.business.Product;

public class ProductDB {
    
    
    /*
    the static method below uses the result set pulled from the MySQL product 
    database to create a local product object
    */
    private static Product getProductFromRow(ResultSet rs) throws SQLException {

        int productID = rs.getInt(1);
        String code = rs.getString(2);
        String description = rs.getString(3);
        double price = rs.getDouble(4);
        String note = rs.getString(5); // added getString method returns note

        Product p = new Product();
        p.setId(productID);
        p.setCode(code);
        p.setDescription(description);
        p.setPrice(price);
        p.setNote(note); // added setNote method sets note for product object
        
        return p;
    }
    /*
    the method below returns all products from the database by creating a
    connection and then using a prepared statement to query the database. The 
    result set is stored in the ArrayList products.The result set is then 
    printed to the console.
    */
    public static List<Product> getAll() throws DBException {
        String sql = "SELECT * FROM Product ORDER BY ProductID";
        List<Product> products = new ArrayList<>();
        Connection connection = DBUtil.getConnection();
        try (PreparedStatement ps = connection.prepareStatement(sql);
                ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Product p = getProductFromRow(rs);
                products.add(p);
            }
            rs.close();
            return products;
        } catch (SQLException e) {
            throw new DBException(e);
        }
    }
    
    /*
    the method below returns a single product from the MySQL products database
    by creating a connection then using a prepared statement to query the
    database then using the resulting data to create a product object.
    */
    public static Product get(String productCode) throws DBException {
        String sql = "SELECT * FROM Product WHERE Code = ?";
        Connection connection = DBUtil.getConnection();
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, productCode);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                Product p = getProductFromRow(rs);
                rs.close();
                return p;
            } else {
                rs.close();
                return null;
            }
        } catch (SQLException e) {
            throw new DBException(e);
        }
    }
    
    /*
    the method below allows the user to add products to the MySQL products 
    databse by creating a connection then using a prepared statement to update 
    the database using attributes from the product object created from user input
    */
    public static void add(Product product) throws DBException {
        String sql
                = "INSERT INTO Product (Code, Description, ListPrice, Note) "
                + "VALUES (?, ?, ?, ?)";
        Connection connection = DBUtil.getConnection();
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, product.getCode());
            ps.setString(2, product.getDescription());
            ps.setDouble(3, product.getPrice());
            ps.setString(4, product.getNote());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DBException(e);
        }
    }
    
    /*
    the method below uses similar procedures to the add method above to update 
    existing records in the MySQL products database
    */
    
    public static void update(Product product) throws DBException {
        String sql = "UPDATE Product SET "
                + "Code = ?, "
                + "Description = ?, "
                + "ListPrice = ?, "
                + "Note = ?"
                + "WHERE ProductID = ?";
        Connection connection = DBUtil.getConnection();
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, product.getCode());
            ps.setString(2, product.getDescription());
            ps.setDouble(3, product.getPrice());
            ps.setString(4, product.getNote());
            ps.setLong(5, product.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DBException(e);
        }
    }
    
    /*
    the method below allows the user to delete products from the MySQL products
    database by creating a connection and using a prepared statement to delete 
    records based upon the product code supplied by the user
    */
    public static void delete(Product product)
            throws DBException {
        String sql = "DELETE FROM Product "
                + "WHERE ProductID = ?";
        Connection connection = DBUtil.getConnection();
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setLong(1, product.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DBException(e);
        }
    }
}