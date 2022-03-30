/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package FishData;

import FishyBusiness.FishyActions;

/**
 *
 * @author owner
 */
public class FishyData {
    
    public static FishyActions getFish(String name){
        
        FishyActions fish = new FishyActions();
        
        if (name.equalsIgnoreCase("tuna")){
            fish.setFishType("Maguro");
            fish.setFishProfile("high mineralty");
            fish.setFishPrice(8.00);
        }
        
        else if (name.equalsIgnoreCase("salmon")){
            fish.setFishType("Shake");
            fish.setFishProfile("Oil Rich");
            fish.setFishPrice(8.00);
        }
        else if (name.equalsIgnoreCase("White fish")){
            fish.setFishType("Shiro");
            fish.setFishProfile("Light");
            fish.setFishPrice(7.00);
        }
        
        else {
            fish.setFishType("unknown");
            fish.setFishProfile("unkniwn");
            fish.setFishPrice(0.00);
        }
        
        return fish;
        
    
    }
}
