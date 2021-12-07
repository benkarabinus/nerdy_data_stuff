#!/usr/bin/env python3
"""@author Ben Karabinus"""
import argparse
import csv
import logging
import os
from collections import namedtuple, defaultdict
import numpy as np
import requests
import matplotlib.pyplot as plt



def main():


    """
    main method setup to allow use as a module and as a solo program
    """
    #create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    # logging file handler
    fh = logging.FileHandler('autompg3.log', 'a')
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
    parser.add_argument('-o', '--ofile', dest= 'output', default=None,\
                        action='store', metavar='<outfie>',\
                        help='please specify a filename. If None sys.stdout')
    parser.add_argument('-p', '--plot', dest='plot',\
                        action='store_true', default='False',
                        help='create a simple plot of average mpg by year or by make')
    parser.add_argument('-a', '--average', dest='mean',\
                        choices=['mpg_by_year', 'mpg_by_make'],\
                        action='store', metavar='<avg_mpg> mpg_by_year || mpg_by_make',\
                        help='print and plot (optional -p) average mpg by year or make')

    #employ paserer
    args = parser.parse_args()
    data = AutoMPGData()
    
    #if optional arg sort by option or store by option
    if args.sort == 'year':
        data.sort_by_year()
    if args.sort == 'mpg':
        data.sort_by_mpg()
    if args.sort == 'default':
        data.sort_by_default()
    if args.mean == 'mpg_by_make':
        data = data.mpg_by_make()
    if args.mean == 'mpg_by_year':
        data = data.mpg_by_year()
    if args.plot and args.mean == 'mpg_by_make':
        plt = plot_data(data, 'make')
        if args.output == None:
            plt.show()
        else:
            plt.savefig(args.output + '.png')
            
    if args.plot and args.mean == 'mpg_by_year':
        plt = plot_data(data, 'year')
        if args.output == None:
            plt.show()
        else:
            plt.savefig(args.output + '.png')
    if args.output == None:
        import sys
        output_direct(sys.stdout, data)
    else:
        with open(args.output +'.csv', 'w') as args.output:
            output_direct(args.output, data)



def output_direct(output, data):

    if isinstance(data, dict):
        for k, v in data.items():
            writer = csv.writer(output)
            writer.writerow([k, v])
    else:
        for a in data:
            writer = csv.writer(output)
            writer.writerow([a.make, a.model, a.year, a.mpg])


#create and return scatter plot
def plot_data(data, choice):

    if choice == 'year':
        x = np.array([k for k,v in data.items()])
        y = np.array([v for k, v in data.items()])
        plt.scatter(x, y)
        plt.xlabel('Year')
        plt.ylabel('Avg_MPG')

    if choice == 'make':
        x = np.array([k for k, v in data.items()])
        y = np.array([v for k, v in data.items()])
        plt.scatter(x,y)
        plt.xlabel('Make')
        plt.ylabel('Avg_MPG')

    return plt





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
        clean_dict = {"chevroelt":"chevrolet",
                      "chevy": "chevrolet",
                     "maxda": "mazda",
                      "mercedes-benz": "mercedes",
                      "toyouta": "toyota",
                      "vokswagen": "volkswagen",
                      "vw": "volkswagen"}

        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower',\
                                       'weight', 'acceleration', 'model_year',\
                                       'origin', 'car_name'])
        with open(file, 'r')as csvfile:
            reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)
            for row in reader:
                record = Record._make(row)
                make_model = record.car_name.split(" ")
                model = " ".join(make_model[1:])
                for k, v in clean_dict.items():
                    if make_model[0] == k:
                        make_model[0] = v
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

    def get_mean(self, attribute):

        l = []
        for record in self.data:
            if record.year == attribute or record.make == attribute:
                l.append(float(record.mpg))
        l = np.array(l)
        return round(l.mean(), 4)

    #return dictionary of average mpg by year (sorted)
    def mpg_by_year(self):
        years =[]
        for record in self.data:
            year = record.year
            years.append(year)
        years = set(years)
        avg_mpg_year = defaultdict(lambda: "Not a valid year")
        for year in years:
            avg_mpg_year[year] = self.get_mean(year)
        sorted_avg = {key: val for key, val in sorted(avg_mpg_year.items(), key = lambda e: e[0])}
        return sorted_avg

    #return dictionary of avg mpg by make (sorted)
    def mpg_by_make(self):
        makes = []
        for record in self.data:
            make = record.make
            makes.append(make)
        makes = set(makes)
        avg_mpg_make = defaultdict(lambda: "Not a valid make")
        for make in makes:
            avg_mpg_make[make] = self.get_mean(make)
        sorted_avg = {key: val for key, val in sorted(avg_mpg_make.items(), key = lambda e: e[0])}
        return sorted_avg

    def __iter__(self):
        return iter(self.data)


# execute main() function if called as a program
if __name__ == '__main__':
    main()
