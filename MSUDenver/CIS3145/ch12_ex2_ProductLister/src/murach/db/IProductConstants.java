/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
*/

package murach.db;

//declaration of IProductConstants interface 
public interface IProductConstants {
    
    //constants are available within all classes implementing the interface
    //constants declared by inherited intefaces will also be available
    final int CODE_WIDTH = 10; //constant declaration
    final int DESC_WIDTH = 34; //constant declaration
    final int PRICE_WIDTH = 10; //constant declaration
}
