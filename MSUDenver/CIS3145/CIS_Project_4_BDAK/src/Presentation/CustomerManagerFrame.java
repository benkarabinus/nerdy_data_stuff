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
import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;


public class CustomerManagerFrame extends JFrame {
    
    private JTable customerTable; //create customer table variable
    private CustomerTableModel customerTableModel; // extend AbstractTable Model
    
    //constructor CustomerManagerFrame
    public CustomerManagerFrame() {
        
        //attempt to attain system look and feel
        try {
            UIManager.setLookAndFeel(
                    UIManager.getSystemLookAndFeelClassName());
        } catch (ClassNotFoundException | InstantiationException |
                 IllegalAccessException | UnsupportedLookAndFeelException e) {
            System.out.println(e);
        } 
        //set frame title, size, location, default close operation
        setTitle("Customer Manager");
        setSize(800, 600);
        setLocationByPlatform(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        //add the button panel to CustomerManagerFrame
        add(buildButtonPanel(), BorderLayout.SOUTH);
        
        //create customerTable and employ scrollbar when needed
        customerTable = buildCustomerTable();
        add(new JScrollPane(customerTable),BorderLayout.CENTER);
        // make table visible
        setVisible(true);
    }
    
    
      //method to build customer table  
      private JTable buildCustomerTable() {
        
        //create customerTableModel
        customerTableModel = new CustomerTableModel();
        
        //instantiate customerTableModel
        JTable table = new JTable(customerTableModel);
        
        //set selection mode, select one list index object at a time
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        table.setBorder(null);
        //return customer table
        return table;
    }
      
      //method to build button panel
      private JPanel buildButtonPanel() {
        
        //create new JPanel object
        JPanel panel = new JPanel();
        
        //the "add" button
        JButton addButton = new JButton("Add");
        addButton.setToolTipText("Add customer");
        
        //action listener for add button employs doAddButton method
        addButton.addActionListener((ActionEvent) -> {
            doAddButton();
        });
        
        //add the "add" button
        panel.add(addButton);
        
        //the "edit" button
        JButton editButton = new JButton("Edit");
        editButton.setToolTipText("Edit selected customer");
        
        //action listener for editButton employs doEditButton method
        editButton.addActionListener((ActionEvent) -> {
            doEditButton();
        });
        
        //add the "edit" button
        panel.add(editButton);
        
        //the delete button
        JButton deleteButton = new JButton("Delete");
        deleteButton.setToolTipText("Delete selected customer");
        
        //action listener deploys the doDeleteButton method
        deleteButton.addActionListener((ActionEvent) -> {
            doDeleteButton();
        });
        
        //add the "delete" button
        panel.add(deleteButton);
        
        //return the button panel
        return panel;
    }
      
      //add customer to the database
       private void doAddButton() {
        //create new customer form   
        CustomerForm customerForm = new CustomerForm(this, "Add Customer", true);
        customerForm.setLocationRelativeTo(this);
        customerForm.setVisible(true);
    }
       //edit existing customer
        private void doEditButton() {
        
        //test for row selection
        int selectedRow = customerTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this,
                    "No customer is currently selected.", 
                    "No customer selected", JOptionPane.ERROR_MESSAGE);
        } else {
            Customer customer = customerTableModel.getCustomer(selectedRow);
            
            //create form to edit customer
            CustomerForm customerForm = 
                    new CustomerForm(this, "Edit Customer", true, customer);
            customerForm.setLocationRelativeTo(this);
            customerForm.setVisible(true);
        }
    }
        
        //delete customer from the database
        private void doDeleteButton() {
        
        //test for row selection
        int selectedRow = customerTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this,
                    "No customer is currently selected.", 
                    "No customer selected", JOptionPane.ERROR_MESSAGE);
        } else {
            //select customer from the table
            Customer customer = customerTableModel.getCustomer(selectedRow);
            
            //user confirmation to delete customer
            int ask = JOptionPane.showConfirmDialog(this,
                    "Are you sure you want to delete " +customer.getFirstName()+" "+customer.getLastName()+" from the database?",
                    "Confirm delete", JOptionPane.YES_NO_OPTION);
            if (ask == JOptionPane.YES_OPTION) {
                try {
                    //delete customer 
                    CustomerDB.delete(customer);
                    
                    //update table
                    fireDatabaseUpdatedEvent();
                    
                    //catch database exception
                } catch (DatabaseException e) {
                    System.out.println(e);
                }
            }
        }
    
    }
        //mehtod to update table data
        void fireDatabaseUpdatedEvent() {
        customerTableModel.databaseUpdated();
    }    
}
