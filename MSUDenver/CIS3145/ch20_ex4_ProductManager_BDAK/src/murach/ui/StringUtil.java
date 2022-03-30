/*
Name: Ben Karabinus
Project: Chapter 20 exercise 4 Product Manager
Date: 11/7/19
Description: This project demonstrates the ability to connect to a MySQL database
using a Java 8 application.
Aside: no inline comments were added to this class no code was edited
*/

package murach.ui;

public class StringUtil {

    public static String padWithSpaces(String s, int length) {
        if (s.length() < length) {
            StringBuilder sb = new StringBuilder(s);
            while (sb.length() < length) {
                sb.append(" ");
            }
            return sb.toString();
        } else {
            return s.substring(0, length);
        }
    }
}
