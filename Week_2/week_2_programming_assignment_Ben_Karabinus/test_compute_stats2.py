#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 9/9/2020
#Project: Week 2 Programming Assignment
#Purpose: show basic understanding of using python 3 for software testing

#import the necessary modules
import unittest, compute_stats2 as c

#create class Compute_Stats2_Test
class Compute_Stats2_Test(unittest.TestCase):




    #test a sequence containing an even number of elements
    def test_even_elements(self):

        ret = c.compute_stats([i for i in range(1,11)])
        self.assertEqual(ret, (1, 10, 5.5,5.5))

    #test a sequence containing an odd number of elements
    def test_odd_elements(self):

        ret = c.compute_stats([i for i in range(1,10)])
        self.assertEqual(ret, (1,9,5,5))

    #test an empty sequence
    def test_empty_sequence(self):

        ret = c.compute_stats([])
        self.assertEqual(ret, (None, None, None, None))

    #test a sequence with a single element
    def test_single_element_sequence(self):

        ret = c.compute_stats([1])
        self.assertEqual(ret, (1, 1, 1, 1))

    #test a sequence with mixed data types
    def test_sequence_mixed_data_types(self):

        with self.assertRaises(TypeError):
            ret = c.compute_stats([1,2,'data',4])






if __name__ == "__main__":
    unittest.main()
