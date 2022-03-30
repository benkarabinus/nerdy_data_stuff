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
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.WindowConstants;


public class CustomerForm extends JDialog {
    
    //create instance variables of the customer form
    private JTextField userIDField;
    private JTextField firstNameField;
    private JTextField lastNameField;
    private JTextField emailField;
    private JButton submitButton;
    private JButton cancelButton;
    private Customer customer = new Customer();
    
    //construct form to enter new customer into the database
    public CustomerForm(java.awt.Frame parent, String title, boolean modal) {
        super(parent, title, modal);
        initComponents();
        userIDField.setText("New Customer");
        userIDField.setEnabled(false);
    }
    
    //construct to update existing customer 
    public CustomerForm(java.awt.Frame parent, String title,
            //this constructor passes selected customer object
            boolean modal, Customer customer) {
        this(parent, title, modal);        
        this.customer = customer;
        
        //set button name to update
        submitButton.setText("Update");
        // populate fields with user attributes
        
        userIDField.setText(Integer.toString(customer.getUserID()));
        firstNameField.setText(customer.getFirstName());
        lastNameField.setText(customer.getLastName());
        emailField.setText(customer.getEmail());
        
        //enable userID field
        userIDField.setEnabled(false);
    }
    
    //initiate form components
    private void initComponents() {
        userIDField = new JTextField();
        firstNameField = new JTextField();
        lastNameField = new JTextField();
        emailField = new JTextField();
        submitButton = new JButton();
        cancelButton = new JButton();
        
        //dispose of dialogue box "customerForm" on close
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);        
        
        //create and set component dimensions
        Dimension shortField = new Dimension(120, 20);
        Dimension longField = new Dimension(300, 20);
        userIDField.setPreferredSize(shortField);
        userIDField.setMinimumSize(shortField);        
        firstNameField.setPreferredSize(longField);
        firstNameField.setMinimumSize(longField);        
        lastNameField.setPreferredSize(longField);
        lastNameField.setMinimumSize(longField);
        emailField.setPreferredSize(longField);
        emailField.setMinimumSize(longField);
        
        // set text for add button
        submitButton.setText("Add");
        
        //action listener for employs submitActionButtonPerformed()
        submitButton.addActionListener((ActionEvent e) -> {
            submitButtonActionPerformed();
        });
        
        //set text for cancel button
        cancelButton.setText("Cancel");
        
        //action  listener employees cancelButtonActionPerformed
        cancelButton.addActionListener((ActionEvent e) -> {
            cancelButtonActionPerformed();
        });

        //create JLabel and JTextField panel
        
        JPanel customerPanel = new JPanel();
        
        //set gridbag layout
        customerPanel.setLayout(new GridBagLayout());
        
        customerPanel.add(new JLabel("Customer ID:"),
                getConstraints(0, 0, GridBagConstraints.LINE_END));
        
        customerPanel.add(userIDField,
                getConstraints(1, 0, GridBagConstraints.LINE_START));
        
        customerPanel.add(new JLabel("First Name:"),
                getConstraints(0, 1, GridBagConstraints.LINE_END));
        customerPanel.add(firstNameField,
                getConstraints(1, 1, GridBagConstraints.LINE_START));
        
        customerPanel.add(new JLabel("Last Name:"),
                getConstraints(0, 2, GridBagConstraints.LINE_END));
        customerPanel.add(lastNameField,
                getConstraints(1, 2, GridBagConstraints.LINE_START));
        
        customerPanel.add(new JLabel("Email Address:"),
                getConstraints(0, 3, GridBagConstraints.LINE_END));
        
        customerPanel.add(emailField,
                getConstraints(1, 3, GridBagConstraints.LINE_START));

        // JButton panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout(FlowLayout.RIGHT));
        buttonPanel.add(submitButton);
        buttonPanel.add(cancelButton);

        // add panels to main panel
        setLayout(new BorderLayout());
        add(customerPanel, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);
        pack();        
    }
    
    //gridbag constraints static method allows user to pass x, y, and anchor value
    private GridBagConstraints getConstraints(int x, int y, int anchor) {
        GridBagConstraints c = new GridBagConstraints();
        c.insets = new Insets(5, 5, 0, 5);
        c.gridx = x;
        c.gridy = y;
        c.anchor = anchor;
        return c;
    }
    
    //cancel button dispose of window and contents
    private void cancelButtonActionPerformed() {        
        dispose();
    }
    
    //submit button (dual purpose)
    private void submitButtonActionPerformed() {
        //data first validated and set
        if (submitButton.getText().equalsIgnoreCase("add")){
            userIDField.setText("0");
        }
        if (validateData()) {
            setData();
            
            //conditional test edit or add
            if (submitButton.getText().equals("Add")) {
                doAdd();
            } else {
                doEdit();
            }
        }
    }
    
    //data validation
    private boolean validateData() {
        String stringUserID = userIDField.getText();
        String firstName = firstNameField.getText();
        String lastName = lastNameField.getText();
        String email = emailField.getText();
        int userID;
        
        if (stringUserID == null || firstName == null || lastName == null
                || email == null || stringUserID.isEmpty() || firstName.isEmpty()
                || lastName.isEmpty() || email.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please fill in all fields.",
                    "Missing Fields", JOptionPane.INFORMATION_MESSAGE);
            return false;
        } else {
            try {
                //additional functionality for later use
                //functionality validates id input if needed
                userID = Integer.parseInt(stringUserID);
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(this,
                        "The data entered in the User ID field is invalid",
                        "Please enter a valid User ID",
                        JOptionPane.INFORMATION_MESSAGE);
                userIDField.requestFocusInWindow();
                return false;
            }
        }
        return true;
    }
    
    //set customer attributes
    private void setData() {
        // userID does not need to be set for this implementation
        String userID = userIDField.getText(); 
        String firstName = firstNameField.getText();
        String lastName = lastNameField.getText();
        String email = emailField.getText();
        customer.setFirstName(firstName);
        customer.setLastName(lastName);
        customer.setEmail(email);
        
        
        
    }
    
    private void doEdit() {
        
        try {
            CustomerDB.update(customer);
            dispose();
            fireDatabaseUpdatedEvent();
        } catch (DatabaseException e) {
            System.out.println(e);
        }
    }
    
    private void doAdd() {
        try {
            CustomerDB.add(customer);
            dispose();
            fireDatabaseUpdatedEvent();
        } catch (DatabaseException e) {
            System.out.println(e);
        }
    }
    
    //update customerManangerFrame to reflect changes
    private void fireDatabaseUpdatedEvent() {
        CustomerManagerFrame customerManagerFrame = (CustomerManagerFrame) getOwner();
        customerManagerFrame.fireDatabaseUpdatedEvent();
    }
}
