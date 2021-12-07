#!/usr/bin/env python3
"""@author Ben Karabinus"""
import os
import csv
from collections import namedtuple
import logging
import requests
import ssl
import argparse






def main():
    """
    main method setup to allow use as a module and as a solo program
    """

    #create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

    # logging file handler
    fh = logging.FileHandler('autompg2.log', 'a')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # logging stream handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    #creater parser
    parser = argparse.ArgumentParser(description="This program allows the user to \
    sort AutoMPG objects by year, mpg, default.")
    parser.add_argument('command', metavar = '<command>',\
                        choices = ['print'],\
                        help = 'Please type print')
    parser.add_argument('-s', '--sort', dest='sort',\
                        action='store', metavar='<sort order>',\
                        choices=['year', 'mpg', 'default'],\
                        help='<sort order> = year || mpg || default')


    #employ paserer
    args = parser.parse_args()

    data = AutoMPGData()
    #if optional arg sort by option
    if args.sort == 'year':
        data.sort_by_year()
    if args.sort == 'mpg':
        data.sort_by_mpg()
    if args.sort == 'default':
        data.sort_by_default()
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

    def sort_by_default(self):
        self.data.sort()

    def sort_by_year(self):
       self.data.sort(key=lambda x: (x.year, x.make, x. model, x.mpg))


    def sort_by_mpg(self):
        self.data.sort(key=lambda x: (x.mpg, x.make, x.model, x.year))

    def _load_data(self):
        self.data = []
        if not os.path.exists("auto-mpg.clean.txt"):
            self.get_data()
            self._clean_data('auto-mpg.data.txt')
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

    def get_data(self):
        """Download data from the web"""
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
        timeout = 0.2
        try:
            r = requests.get(url, timeout = timeout)
            r.raise_for_status()
            with open('auto-mpg.data.txt', 'w')as file:
                file.write(r.text)
        except requests.exceptions.ConnectionError as error:
            print(str(error))
        except requests.exceptions.Timeout as error:
            print(str(error))

    def __iter__(self):
        return iter(self.data)


# execute main() function if called as a program
if __name__ == '__main__':
    main()
