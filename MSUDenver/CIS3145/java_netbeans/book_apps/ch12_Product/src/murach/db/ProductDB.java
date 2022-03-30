package murach.db;

import murach.business.Product;

public class ProductDB implements ProductReader {

    @Override
    public Product getProduct(String productCode) {
        // In a more realistic application, this code would
        // get the data for the product from a database
        // For now, this code just uses if/else statements
        // to return the correct product data

        // create the Product object
        Product product = new Product();

        // fill the Product object with data
        product.setCode(productCode);
        if (productCode.equalsIgnoreCase("java")) {
            product.setDescription("Murach's Java Programming");
            product.setPrice(57.50);
        } else if (productCode.equalsIgnoreCase("jsp")) {
            product.setDescription("Murach's Java Servlets and JSP");
            product.setPrice(57.50);
        } else if (productCode.equalsIgnoreCase("mysql")) {
            product.setDescription("Murach's MySQL");
            product.setPrice(54.50);
        } else {
            product.setDescription("Unknown");
        }
        return product;
    }

    @Override
    public String getProducts() {
        throw new UnsupportedOperationException(
                "This method hasn't been implemented yet.");
    }
}