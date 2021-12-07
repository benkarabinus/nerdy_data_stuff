#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/10/2020
#Project: Chapter 18 Exercise Preferences
#Purpose: show basic understanding of how to create GUI
#in Python 3

#import database tier
import db

#class persom
class Person:
    def __init__(self, name, language, save_time):
        self.__name = name
        self.__language = language
        self.__save_time = save_time

    #getter and setter methods for class Person
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self,language):
        self.__language = language
    @property
    def save_time(self):
        return self.__save_time
    @save_time.setter
    def save_time(self,save_time):
        self.__save_time = save_time

    #convert user preferences for storage in csv format
    def create_preferences_list(self, name, language, save):
        preferences = []
        preference = []
        preference.append(name)
        preference.append(language)
        preference.append(save)
        preferences.append(preference)
        db.preference_writer(preferences)

