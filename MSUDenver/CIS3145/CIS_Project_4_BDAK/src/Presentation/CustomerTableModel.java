/*
Name: Ben Karabinus
Project: CIS 3145 Project 4
Date: 11/23/19
Description: This project shows basic understanding of multi-tiered applications 
in Java 8
 */
package Presentation;

import Business_Logic.Customer;
import Database.CustomerDB;
import Database.DatabaseException;
import java.util.List;
import javax.swing.table.AbstractTableModel;

//create CutomerTableModel from AbstractTableModel
public  class CustomerTableModel extends AbstractTableModel {
    
    //array list to store customer objects
    private List<Customer> customers;
    //list stores column names
    private final String[] COLUMN_NAMES = {"Email", "First Name", "Last Name"};
    
    //construct and populate table model
    public CustomerTableModel(){
        try{
            customers = CustomerDB.getAll();
         
        //catch database exception
        }catch(DatabaseException e){
            System.out.println(e);
        }
        
    }

    @Override //determine number of rows in the table
    public int getRowCount() {
        return customers.size();
    }

    @Override //determine number of columns in the table
    public int getColumnCount() {
        return COLUMN_NAMES.length;
    }
    
    @Override //determine column names
    public String getColumnName(int columnIndex){
        return COLUMN_NAMES[columnIndex];
    }

    @Override //return customer attributes based on table position
    public Object getValueAt(int rowIndex, int columnIndex) {
        switch(columnIndex){
            case 0:
                return customers.get(rowIndex).getEmail();
            case 1:
                return customers.get(rowIndex).getFirstName();
            case 2:
                return customers.get(rowIndex).getLastName();
            default:
                return null;
        }
        
    }
    
    //return customer object based on table position
    Customer getCustomer(int rowIndex){
        
        return customers.get(rowIndex);
    }
    
    //refresh table following database update
    void databaseUpdated(){
        try{
            customers = CustomerDB.getAll();
            fireTableDataChanged();
         
        //catch database exception
        }catch(DatabaseException e){
            System.out.println(e);
        }
    }
    
    
}
