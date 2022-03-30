/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package FishyBusiness;

/**
 *
 * @author owner
 */
public class FishyActions {
    
   String type;
   String profile;
   Double price;
   
   public FishyActions(){
       
   }
   
   public FishyActions(String type, String profile,Double price){
       this.type = type;
       this.profile = profile;
       this.price = price;
       
   }
   
   public void setFishType(String type){
       this.type = type;
   }
   
   public void setFishProfile(String profile){
       this.profile = profile;
   }
   
   public void setFishPrice(Double price){
       this.price = price;
   }
   
   public String getFishType(){
       return this.type;
   }
   
   public String getFishProfile(){
       return this.profile;
   }
   
   public Double getFishPrice(){
       return this.price;
   }

    
   
   
    
 
}
