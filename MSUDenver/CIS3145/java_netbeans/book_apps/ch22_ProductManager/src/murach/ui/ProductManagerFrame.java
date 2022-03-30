package murach.ui;

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

import murach.business.Product;
import murach.db.ProductDB;
import murach.db.DBException;

public class ProductManagerFrame extends JFrame {
    private JTable productTable;
    private AvailabilityTableModel productTableModel;
    
    public ProductManagerFrame() {
        try {
            UIManager.setLookAndFeel(
                    UIManager.getSystemLookAndFeelClassName());
        } catch (ClassNotFoundException | InstantiationException |
                 IllegalAccessException | UnsupportedLookAndFeelException e) {
            System.out.println(e);
        }
        setTitle("Product Manager");
        setSize(768, 384);
        setLocationByPlatform(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        add(buildButtonPanel(), BorderLayout.NORTH);
        productTable = buildProductTable();
        add(new JScrollPane(productTable), BorderLayout.CENTER);
        setVisible(true);        
    }
    
    private JPanel buildButtonPanel() {
        JPanel panel = new JPanel();
        
        JButton addButton = new JButton("Add");
        addButton.setToolTipText("Add product");
        addButton.addActionListener((ActionEvent) -> {
            doAddButton();
        });
        panel.add(addButton);
        
        JButton editButton = new JButton("Edit");
        editButton.setToolTipText("Edit selected product");
        editButton.addActionListener((ActionEvent) -> {
            doEditButton();
        });
        panel.add(editButton);
        
        JButton deleteButton = new JButton("Delete");
        deleteButton.setToolTipText("Delete selected product");
        deleteButton.addActionListener((ActionEvent) -> {
            doDeleteButton();
        });
        panel.add(deleteButton);
        
        return panel;
    }
    
    private void doAddButton() {
        ProductForm productForm = new ProductForm(this, "Add Product", true);
        productForm.setLocationRelativeTo(this);
        productForm.setVisible(true);
    }
    
    private void doEditButton() {
        int selectedRow = productTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this,
                    "No product is currently selected.", 
                    "No product selected", JOptionPane.ERROR_MESSAGE);
        } else {
            Product product = productTableModel.getProduct(selectedRow);
            ProductForm productForm = 
                    new ProductForm(this, "Edit Product", true, product);
            productForm.setLocationRelativeTo(this);
            productForm.setVisible(true);
        }
    }
    
    private void doDeleteButton() {
        int selectedRow = productTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this,
                    "No product is currently selected.", 
                    "No product selected", JOptionPane.ERROR_MESSAGE);
        } else {
            Product product = productTableModel.getProduct(selectedRow);
            int ask = JOptionPane.showConfirmDialog(this,
                    "Are you sure you want to delete " + 
                        product.getDescription() + " from the database?",
                    "Confirm delete", JOptionPane.YES_NO_OPTION);
            if (ask == JOptionPane.YES_OPTION) {
                try {                    
                    ProductDB.delete(product);
                    fireDatabaseUpdatedEvent();
                } catch (DBException e) {
                    System.out.println(e);
                }
            }
        }
    }
    
    void fireDatabaseUpdatedEvent() {
        productTableModel.databaseUpdated();
    }    
    
    private JTable buildProductTable() {
        productTableModel = new AvailabilityTableModel();
        JTable table = new JTable(productTableModel);
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        table.setBorder(null);
        return table;
    }    
}