/*
Name: Ben Karabinus
Project: Chapter 12 exercise 2 ProductLister
Date: 10/15/19
Description: this project shows basic understanding of implementing and using
interfaces in java
Aside: no inline comments were added to this class as no code was edited
*/

package murach.ui;

public class StringUtil {

    public static String pad(String s, int length) {
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