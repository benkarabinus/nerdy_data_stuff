#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 9/26/2020
#Project: Week 3 Programming Assignment
#Purpose: show basic understanding of using python 3 for software testing


#import the necessary modules
import unittest, blackjack as b

#create class Compute_Stats2_Test
class Test_Blackjack_Test(unittest.TestCase):

    def test_score(self):

        ret = b.score([3, 12])
        self.assertEqual(ret, (13, 0))

        ret = b.score([5, 5,10])
        self.assertEqual(ret, (20, 0))

        ret = b.score([11, 10, 1])
        self.assertEqual(ret, (21,1))

        ret = b.score([1, 5])
        self.assertEqual(ret, (16, 1))

        ret = b.score([1, 1, 5])
        self.assertEqual(ret, (17,2))

        ret = b.score([1, 1, 1, 7])
        self.assertEqual(ret, (20,3))

        ret = b.score([7, 8, 10])
        self.assertEqual(ret, (25, 0))

        ret = b.score([10, 6, 1])
        self.assertEqual(ret,(17, 1))


    def test_stand(self):

        self.assertTrue(b.stand(17,"soft",[9,8]))
        self.assertTrue(b.stand(17, "hard",[9,8]))
        self.assertTrue(b.stand(17, "soft",[1,6]))
        self.assertFalse(b.stand(17,"hard",[1,6]))
        self.assertFalse(b.stand(18,"soft",[1,6]))
        self.assertFalse(b.stand(18,"hard",[1,6]))





    def test_input_arg_1(self):

        self.assertRaises(TypeError, b.validate_input("a",14,"c"))

    def test_input_arg_2(self):

        self.assertRaises(TypeError, b.validate_input(14,"b","c"))

    def test_input_arg_3(self):

        self.assertRaises(TypeError, b.validate_input("a","b",14))

    def test_value_arg2(self):

        self.assertRaises(ValueError, b.validate_input(100, 21, "c"))













if __name__ == "__main__":
    unittest.main()
