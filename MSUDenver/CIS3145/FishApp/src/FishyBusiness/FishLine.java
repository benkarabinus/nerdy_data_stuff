/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package FishyBusiness;

import FishData.FishyData;
import java.text.NumberFormat;

/**
 *
 * @author owner
 */
public class FishLine {
    private FishyActions fish;
    private int qnty;
    
   public FishLine(FishyActions fish, int qnty){
       this.fish = fish;
       this.qnty= qnty;
   }
   
   public void setFish(FishyActions fish){
       
       this.fish = fish;
   }
   
   public void setQnty(int qnty){
       this.qnty = qnty;
   }
   
   public int getQnty(){
       return this.qnty;
   }
   
   public Double getTotal(){
      
       Double total = qnty * fish.getFishPrice();
       return total;
   }
   
   public String getTotalFormatted() {
        double total = this.getTotal();
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String totalFormatted = currency.format(total);        
        return totalFormatted;
    }
}
