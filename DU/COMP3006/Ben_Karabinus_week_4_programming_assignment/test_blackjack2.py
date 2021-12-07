#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 8/10/2020
#Project: Week 4 Programming Assignment
#Purpose: show basic understanding of using python 3 for software testing


#import the necessary modules
import unittest, blackjack2 as b


class Test_Blackjack_Test(unittest.TestCase):

    """
    Test that the score function computes the correct total and soft ace counts
    for each hand provided as input below

    """
    def test_score(self):
        ret = (b.score([3, 12]))
        self.assertEqual(ret, (13, 0))

        ret = b.score([5, 5,10])
        self.assertEqual(ret, (20, 0))

        ret = b.score([11, 10, 1])
        self.assertEqual(ret, (21,0))

        ret = b.score([1, 5])
        self.assertEqual(ret, (16, 1))

        ret = b.score([1, 1, 5])
        self.assertEqual(ret, (17,1))

        ret = b.score([1, 1, 1, 7])
        self.assertEqual(ret, (20,1))

        ret = b.score([7, 8, 10])
        self.assertEqual(ret, (25, 0))

        ret = b.score([10, 6, 1])
        self.assertEqual(ret,(17, 0))

        ret = b.score([1,6])
        self.assertEqual(ret,(17,1))

    """
     Test that the stand function returns the correct boolean value
     "True or False" for whether the player should hit stand based on rules of
     the game.

    """

    def test_stand(self):
        self.assertTrue(b.stand(17, True, [9, 8]).stand)
        self.assertTrue(b.stand(17, False, [9, 8]).stand)
        self.assertTrue(b.stand(17, True, [1, 6]).stand)
        self.assertFalse(b.stand(17, False, [1, 6]).stand)
        self.assertFalse(b.stand(18, True, [1, 6]).stand)
        self.assertFalse(b.stand(18, False, [1, 6]).stand)
        self.assertFalse(b.stand(17, False, [1, 1, 5]).stand)
        self.assertFalse(b.stand(17, False,[1, 1, 1, 7]).stand)







    #test input validation
    def test_str_arg_1(self):

        with self.assertRaises(TypeError):
            b.validate_input('a')


    def test_flt_arg_1(self):

        with self.assertRaises(TypeError):
            b.validate_input(100.1)

















if __name__ == "__main__":
    unittest.main()
