package murach.ui;

import java.util.List;
import javax.swing.table.AbstractTableModel;
import murach.business.Product;
import murach.db.ProductDB;
import murach.db.DBException;

public class AvailabilityTableModel extends AbstractTableModel {
    
    String stuff [] = {"a","b","c","d"};
    private static final String[] COLUMN_NAMES = {
        "", "M", "T", "W", "T","F","Sa","Su"
    };

    
    public AvailabilityTableModel() {
        
    }
    
    
    
    

    @Override
    public int getRowCount() {
       return 5;
    }

    @Override
    public int getColumnCount() {
        return COLUMN_NAMES.length;
    }
    
    @Override
    public String getColumnName(int columnIndex) {
        return COLUMN_NAMES[columnIndex];
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        switch (columnIndex) {
            case 0:
                return "hello";
            case 1:
                return "hello";
            case 2:
                return "hello";
            default:
                return null;
        }
    }   
}