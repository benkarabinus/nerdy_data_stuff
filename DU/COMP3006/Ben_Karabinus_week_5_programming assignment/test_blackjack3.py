#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 8/15/2020
#Project: Week 5 Programming Assignment
#Purpose: show basic understanding of using python 3 for software testing


#import the necessary modules
import unittest, blackjack3 as b


class Test_Blackjack_Test(unittest.TestCase):


    def test_score(self):
        """
        Test that the score function computes the correct total and soft ace counts
        for each hand provided as input below
        """
        ret = (b.Hand(cards=[3, 12]).score())
        self.assertEqual(ret, (13, 0))

        ret = (b.Hand(cards=[5, 5, 10]).score())
        self.assertEqual(ret, (20, 0))

        ret = (b.Hand([11, 10, 1]).score())
        self.assertEqual(ret, (21,0))

        ret = (b.Hand([1, 5]).score())
        self.assertEqual(ret, (16, 1))

        ret = (b.Hand([1, 1, 5]).score())
        self.assertEqual(ret, (17, 1))

        ret = (b.Hand([1, 1, 1, 7]).score())
        self.assertEqual(ret, (20, 1))

        ret = (b.Hand([7, 8, 10]).score())
        self.assertEqual(ret, (25, 0))

        ret = (b.Hand([10, 6, 1]).score())
        self.assertEqual(ret, (17, 0))

        ret = (b.Hand([1, 6]).score())
        self.assertEqual(ret, (17, 1))

    def test_is_blackjack(self):
        self.assertTrue(b.Hand([11, 10, 1]).is_blackjack())

    def test_is_bust(self):
        self.assertTrue(b.Hand([10, 10, 2]).is_bust())

    def test_stand(self):
        """
         Test that the stand function returns the correct boolean value
         "True or False" for whether the player should hit or stand based on rules of
         the game.
        """
        hand = b.Hand(cards=[9, 8])
        strategy = b.Strategy(17, True).stand(hand)
        self.assertTrue(strategy)
        strategy2 = b.Strategy(17, False).stand(hand)
        self.assertTrue(strategy2)
        hand = b.Hand(cards=[1, 6])
        strategy3 = b.Strategy(17, True).stand(hand)
        self.assertTrue(strategy3)
        strategy4 = b.Strategy(17, False).stand(hand)
        self.assertFalse(strategy4)
        hand = b.Hand(cards=[1, 1, 5])
        strategy5 = b.Strategy(17, False).stand(hand)
        self.assertFalse(strategy5)
        hand = b.Hand(cards=[1, 1, 1, 7])
        strategy6 = b.Strategy(17, False).stand(hand)
        self.assertFalse(strategy6)

    #test input validation
    def test_str_arg_1(self):
        with self.assertRaises(TypeError):
            b.validate_input('a')

    def test_flt_arg_1(self):
        with self.assertRaises(TypeError):
            b.validate_input(100.1)


if __name__ == "__main__":
    unittest.main()
