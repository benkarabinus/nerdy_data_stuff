/*
Name: Ben Karabinus
Project: Chapter 22 Exercise 3 "TextEditor"
Date: 11/21/19
Description: THis project shows basic understaning og GUI concepts in Java 8
*/
package murach.texteditor;

import java.awt.BorderLayout;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.ScrollPaneConstants;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

public class MainWindow extends JFrame {
    
    //instance variables of the MainWindow class
    private File file;
    private String fileContents = "";
    private JTextArea textArea;
    private JScrollPane scrollBar;
    
        
    public MainWindow() {
        try {
            UIManager.setLookAndFeel(
                    UIManager.getSystemLookAndFeelClassName());
        } catch (ClassNotFoundException | InstantiationException |
                 IllegalAccessException | UnsupportedLookAndFeelException e) {
            System.out.println(e);
        }        
        setTitle("Text Editor");
        setSize(800, 600);
        setLocationByPlatform(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        //add scrollBar and textArea to MainWindow
        add(scrollBar = new JScrollPane(add(textArea = new JTextArea()))
                ,BorderLayout.CENTER);
        
         //wrap text to next line
         textArea.setLineWrap(true);
         
         //wrap by "whole" words
         textArea.setWrapStyleWord(true);
        
        
        //for aesthetic reasons set Horizontal scroll policy to never
        scrollBar.setHorizontalScrollBarPolicy
                (ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        
        
        //add button panel to the north area of the border layout 
        add(buildButtonPanel(), BorderLayout.NORTH);
       
        
        setVisible(true);
    }
    
    private JPanel buildButtonPanel() {
        JPanel panel = new JPanel();
        
        
        
        //the open button allows user to open a .txt file
        JButton openButton = new JButton("Open");
        
        //action listener for the open button
        openButton.addActionListener((ActionEvent ) -> {
            doOpenButton();
        });
        
        //tool tip for the open button
        openButton.setToolTipText("Click to open a text file ");
        
        //add button the open button to the panel
        panel.add(openButton);
        
        //save button allows the user to save changes to the file
        JButton saveButton = new JButton("Save");
        
        //action listener for the save button
        saveButton.addActionListener((ActionEvent) -> {
            doSaveButton();
        });
        
        //tool tip for the save button
        saveButton.setToolTipText("Click to save this file");
        panel.add(saveButton);
        
        
        return panel;
    }
    
    private void doOpenButton() {
        JFileChooser openDialog = new JFileChooser();
        int choice = openDialog.showOpenDialog(this);
        
        if (choice == JFileChooser.APPROVE_OPTION) {
            file = openDialog.getSelectedFile();
            fileContents = "";
            try {
                fileContents = new String(
                    Files.readAllBytes(Paths.get(file.toURI())));
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this,
                        "The file could not be read.", "File read error",
                        JOptionPane.ERROR_MESSAGE);
            }            
            
            //print file contents to JTextArea
            textArea.setText(fileContents);
        }
    }
    
    private void doSaveButton() {
        if (file != null) {
            
            //take file contens from JTextArea
            fileContents = textArea.getText();
            try {
                Files.write(Paths.get(file.toURI()), fileContents.getBytes());
                //print file contents to the text area and confirm file was saved
                textArea.setText(fileContents + "\n"+"The file was saved!");
                
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this,
                        "The file could not be written.", "File write error",
                        JOptionPane.ERROR_MESSAGE);
            }
            // TODO: display file contents in JTextArea control instead of on console
            //see begining of the method for print to text area
            //System.out.println(fileContents);
            
        }
    }
}