#!/usr/bin/env python3
"""@author Ben Karabinus"""
import os
import csv
from collections import namedtuple


def main():
    """
    main method setup to allow use as a module and as a solo program
    """
    data = AutoMPGData()
    for a in data:
        print(a)


class AutoMPG:
    """"Class AutoMPG created to store print and test records of each auto"""
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
    def __repr__(self):
        return f'AutoMPG ({self.make}, {self.model}, {str(19)+self.year}, {self.mpg})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if type(self) == type(other):
            return (self.make, self.model, self.year, self.mpg) == \
            (other.make, other.model, other.year, other.mpg)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.make, self.model, self.year, self.mpg))

    def __lt__(self, other):
        if type(self) == type(other):
            return (self.make, self.model, self.year, self.mpg) \
            < (other.make, other.model, other.year, other.mpg)
        else:
            return NotImplemented

class AutoMPGData:
    """Class AutoMPGData created to clean manipulate and store data source"""
    def __init__(self):
        self._load_data()

    def _load_data(self):
        self.data = []
        if not os.path.exists("auto-mpg.clean.txt"):
            file = "auto-mpg.data.txt"
            self._clean_data(file)
            clean_file = "auto-mpg.clean.txt"
            if os.path.exists(clean_file):
                self.parse_data(clean_file)
        else:
            file = "auto-mpg.clean.txt"
            self.parse_data(file)

    def _clean_data(self, dirty_file):
        clean_file = "auto-mpg.clean.txt"
        with open(dirty_file, 'r')as dirty_file, open(clean_file, 'w')as clean_file:
            reader = dirty_file.readlines()
            for line in reader:
                clean_file.write(line.expandtabs())
        return clean_file

    def parse_data(self, file):
        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower',\
                                       'weight', 'acceleration', 'model_year',\
                                       'origin', 'car_name'])
        with open(file, 'r')as csvfile:
            reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)
            for row in reader:
                record = Record._make(row)
                make_model = record.car_name.split(" ")
                model = " ".join(make_model[1:])
                a = AutoMPG(make_model[0], model, record.model_year, record.mpg)
                self.data.append(a)

    def __iter__(self):
        return iter(self.data)


## execute main() function if called as a program
if __name__ == '__main__':
    main()
