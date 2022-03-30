
package helloenumeration_bdak;

/**
 * Date: October 24, 2019
 * @author Ben Karabinus
 * Description: Creating a language Enumeration and process dates
 */
public enum LanguageType {
    ENGLISH,
    FRENCH,
    SPANISH;
    
  /**
    *
    *  @return The language enumeration as English, French, or Spanish
    */  
    @Override
    public String toString(){
        String temp = "";
        
        if(this.ordinal() == 0)
            temp = "English";
        else if (this.ordinal() == 1)
            temp = "French";
        else if (this.ordinal()== 2)
            temp = "Spanish";
        
        
        return temp;
    }
}
