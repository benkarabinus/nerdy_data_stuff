#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/10/2020
#Project: Chapter 18 Exercise Preferences
#Purpose: show basic understanding of how to create GUI
#in Python 3

#import required modules
import tkinter as tk
from tkinter import ttk
from person import Person
import db

#class "PreferencesFrame" (GUI)
class PreferencesFrame(ttk.Frame):
    #initialize GUI
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        #read preferences from csv
        name, language, save_time = db.read_to_list()
        #assign preferences to person instance
        self.person = Person(name, language, save_time)

        #define string variables for text entry fields
        self.name = tk.StringVar()
        self.language = tk.StringVar()
        self.save = tk.StringVar()
        self.name.set(self.person.name)
        self.language.set(self.person.language)
        self.save.set(self.person.save_time)
        #init frame components
        self.initComponents()

    def initComponents(self):
        self.pack()
        #display labels and text entry fields
        ttk.Label(self, text="Name").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.name).grid(
            column=1, row=0)
        ttk.Label(self, text="Language").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.language).grid(
            column=1, row=1)
        ttk.Label(self, text="Auto Save Every X Minutes").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.save).grid(
            column=1, row=2)
        #init buttons
        self.makeButtons()
        #set padding for all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)



    def makeButtons(self):
        #create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)
        #add button frame to grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)
        #add two buttons to the button frame
        ttk.Button(buttonFrame, text="Save",command=self.click_save_button) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Cancel", command=self.parent.destroy) \
            .grid(column=1, row=0)

    #save button action listener
    def click_save_button(self):
        #assign contents of text fields to variables
        name = self.name.get()
        language = self.language.get()
        #catch value error and display error message
        try:
            save = int(self.save.get())
        except ValueError:
            ttk.Label(self, text="Must be a valid integer.").grid(
                column=3, row=2, sticky=tk.W)
        #if required fields are null display error message
        if name == "":
            ttk.Label(self, text="Required.").grid(
                column=3, row=0, sticky=tk.W)
        elif language == "":
            ttk.Label(self, text="Required.").grid(
                column=3, row=1, sticky=tk.W)
        #else write preferences to csv file and close window
        else:
            self.person.create_preferences_list(name, language, save)
            self.parent.destroy()

#if main run main()
if __name__ == "__main__":
    #init root window
    root = tk.Tk()
    #set title
    root.title("Preferences")
    #init preferences frame on root
    PreferencesFrame(root)
    #run GUI
    root.mainloop()











