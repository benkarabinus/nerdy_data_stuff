#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 2/15/2020
#Project: Chapter 11 Exercise Birthday Calculator
#Purpose: show basic understanding of how to use Date objects 
#in Python 3

from datetime import date, datetime, timedelta

#function to display title
def display_title():
    print("Birthday Calculator")
    print()

#function to get birthdate and set correct year
def get_info():

     #try: accept user data
     while True:
        birthday_str = input("Enter birthday (MM/DD/YY): ")    
        try:
             birthdate = datetime.strptime(birthday_str, "%m/%d/%y")
        #catch value error exception, continue to begining of loop
        except ValueError:
            print("Invalid date format! Try again.")
            continue
        #else correct birthdate error and return birthdate

        if birthdate > datetime.now():
            adjusted_birth_year = birthdate.year - 100
            birthdate = datetime(adjusted_birth_year, birthday.month,
                                     birthday.day)
        return birthdate

#function to process user input
def process_info(birthdate):

    #set current day
    current_day = datetime.now()
    #set days in year
    days_in_year = 365.2425
    #set next birthday
    next_birthday = date(current_day.year, birthdate.month, birthdate.day)
    #calculate age
    if next_birthday == date.today():
        age = ((current_day - birthdate).days / days_in_year) +1
    else:
        age = ((current_day - birthdate).days / days_in_year)
    #adjust next birthday if needed
    if date.today() > next_birthday:
        next_birthday = date(current_day.year +1, birthdate.month,
                             birthdate.day)
    #calculate time to next birthday
    days = (next_birthday - date.today()).days
    #return processed user information
    return current_day, age, next_birthday,days

#function to print results to the console
def print_results(current_day, age, next_birthday, days, name, birthdate):

    #print user birthday with formatting
    print("Birthday: " +birthdate.strftime("%A, %B %d, %Y"))
    #print current date with formatting
    print("Today: ", datetime.now().strftime("%A, %B %d, %Y"))
    #if user > 2 years old
    if age > 2:
        print(name, "is ", int(age), "years old!")
    #else print age in days
    else:
        age = (datetime.now() - birthdate).days
        print(name, "is ", age, "days old!")
    #drop days through birthday message block
    if days == 0:
        print(name+"'s birthday is today!")
    elif days == 1:
        print(name+"'s birthday is tomorrow!")
    elif days == 365:
        print(name+"'s birthday was yesterday!")
    else:
        print(name+"'s birthday is in",days,
        "days!")
    print()
    
    
    
#main function
def main():

    #display title
    display_title()
    #loop control variable
    choice = "y"
    #main control loop
    while choice.lower() != "n":
        #accept user input
        name = input("Enter name: ")
        birthdate = get_info()
        #process input
        current_day, age, next_birthday, days = process_info(birthdate)
        #print results to console
        print_results(current_day, age, next_birthday,days,name,birthdate)
        #allow user to continue
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")
    
    
    

if __name__ == "__main__":
    main()
