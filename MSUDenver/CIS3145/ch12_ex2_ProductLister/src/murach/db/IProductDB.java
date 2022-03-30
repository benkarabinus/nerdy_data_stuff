/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
*/

package murach.db;

import murach.business.Product;

//interface declaration  of IProductDB
public interface IProductDB {
    //get method of IProductDB interface
    public Product get(String productCode);
  
}
