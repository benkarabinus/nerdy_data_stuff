#!/usr/bin/env python3
"""@author Ben Karabinus"""
import csv
import unittest
from collections import namedtuple
from autompg import AutoMPG


class TestAutoMpg(unittest.TestCase):
    """Test methods of class AutoMPG"""
    def AutoMPG(self):
        r1 = AutoMPG("Toyota", "Tacoma", 2004, 17.5)
        r2 = AutoMPG("Nissan", "Frontier", 2004, 18.0)
        r3 = r1
        #test constructor
        self.assertEqual((r1.make, r1.model, r1.year, r1.mpg),\
                         ("Toyota", "Tacoma", 2004, 17.5))
        #test eq method
        self.assertTrue(r1 == r1)
        self.assertFalse(r1 == r2)
        #test hash
        self.assertNotEqual(r1.__hash__(), r2.__hash__())
        self.assertEqual(r1.__hash__(), r3.__hash__())
        #test lt method
        self.assertTrue(r2 < r1)

class TestAutoMPGData(unittest.TestCase):
    """Test methods of class AutoMPGData using pieces of relevant methods"""

    def test_clean_data(self):
        dirty_file = "This\tline\thas\ttabs"
        clean_file = "This line has tabs"
        def _clean_data(dirty_file):
            new_clean_file = dirty_file.expandtabs(1)
            return new_clean_file
        ret = _clean_data(dirty_file)
        self.assertEqual(ret, clean_file)

    def test_parse_data(self):
        #manually create AutoMPG object
        b = AutoMPG('chevrolet', 'chevelle malibu', '70', '18.0')
        #parse file to create AutoMPG object
        csvfile = ['18.0   8   307.0      130.0      3504.      12.0   70  1        "chevrolet chevelle malibu"']
        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower', \
                                       'weight', 'acceleration', 'model_year', \
                                       'origin', 'car_name'])
        reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)
        for row in reader:
            record = Record._make(row)
            make_model = record.car_name.split(" ")
            model = " ".join(make_model[1:])
            a = AutoMPG(make_model[0], model, record.model_year, record.mpg)

        #test equality of manually created object and parsed object
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
