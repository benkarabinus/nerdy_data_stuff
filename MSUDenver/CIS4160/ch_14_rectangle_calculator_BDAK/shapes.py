#!/usr/bin/env python3
# Name: Ben Karabinus
# Date: 2/18/2020
# Project: Chapter 15 Rectangle Square Calculator
# Purpose: show basic understanding of object oriented design and
# inheritance in Python 3

# create the class Rectangle
class Rectangle:
    # Rectangle constructor
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    # create properties for "get" and "set" methods
    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, height):
        self.__height = height

    @width.setter
    def width(self, width):
        self.__width = width

    # method to return area
    def get_area(self):
        return self.__width * self.__height

    # method to return perimeter
    def get_perimeter(self):
        return (2 * self.__width) + (2 * self.__height)

    # override the string method of the object class
    def __str__(self):
        shape = ""
        for i in range(self.__height):
            for j in range(self.__width):
                if i == 0 or i == self.__height - 1:
                    shape += '* '
                elif j == 0 or j == self.__width - 1:
                    shape += '* '
                else:
                    shape += '  '
            shape += "\n"
        return shape
