/*
Name: Ben Karabinus
Project: Chapter 15 Exercise 3 Guessing Game
Date: 10/23/19
Description: This project shows basic understanding of creating and formatting 
date objects in Java 8
*/

package murach.games;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.util.Random;

public class NumberGame {
    private int upperLimit;
    private int number;
    private int guessCount;
    private LocalDateTime startTime;//This instance variable stores the time when the guessing game starts
    private LocalDateTime endTime;//This instance variable stores the time when the guessing game ends
    
    
    public NumberGame() {
        this(50);
    }
    
    public NumberGame(int upperLimit) {
        this.upperLimit = upperLimit;
        Random random = new Random();
        number = random.nextInt(upperLimit + 1) ;
        guessCount = 1;
    }

    public int getNumber() {
        return number;
    }

    public int getGuessCount() {
        return guessCount;
    }
    
    public int getUpperLimit() {
        return upperLimit;
    }
    
    public void incrementGuessCount() {
        guessCount = guessCount + 1;
    }
    
    /*The method below creates a LocalDateTime object and stores 
      it in the startTime variable*/
    public void setStartTime() {
       this.startTime = LocalDateTime.now();
    }
    
     /*The method below creates a LocalDateTime object and stores 
      it in the endTime variable*/
    public void setEndTime() {
        this.endTime = LocalDateTime.now();
    }
    
    //Get method for the startTime variable
    public LocalDateTime getStartTime(){
        return startTime;
    }
    //Get method for the endTime variable
    public LocalDateTime getEndTime(){
        return endTime;
    }
    
    //The method below returns the duration of the game measured in seconds
    public long getDuration(){
        //Create a reference point for start of the game
        long start = startTime.toInstant(ZoneOffset.UTC).getEpochSecond();
        //Create a reference point for end of the game
        long end = endTime.toInstant(ZoneOffset.UTC).getEpochSecond();
        //(end - start) == the duration of the game
        return (end - start);
    }
    
    //The method below creates, formats, and returns a LocalDate object
    public String getDateFormatted(){
        DateTimeFormatter dtf = DateTimeFormatter.ofLocalizedDate(FormatStyle.LONG);
        return dtf.format(LocalDate.now());
    }
    
   
}