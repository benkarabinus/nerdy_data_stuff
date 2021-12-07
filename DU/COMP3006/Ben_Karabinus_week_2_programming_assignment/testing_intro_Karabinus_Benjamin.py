#!/usr/bin/env python3
#Ben Karabinus
#Comp 3006
#This program was created to practice using Python 3 for basic software testing
#9/9/2020

import unittest

class TestMax(unittest.TestCase):


    def testRetValues(self):
        #test return values of the max() in mehtod body as needed

        #a sequence of integers
        ret = max([1,2,3])
        self.assertEqual(ret, 3)

        #a sequence of floats
        ret = max([1.0, 2.0,3.0])
        self.assertEqual(ret, 3.0)

        #sequence of mixed type float/int OK
        ret = max([1,2,2.75])
        self.assertEqual(ret, 2.75)

        #a sequence of characters
        ret = max(['a','A'])
        self.assertEqual(ret, 'a')

        #a string
        ret = max("Hello")
        self.assertEqual(ret, 'o')

        #a sequence of iterables
        it_1 = [1,2,3]
        it_2 = [4,5,6]
        ret = max(it_1, it_2)
        self.assertEqual(ret, it_2)


    def test_TypeError_from_non_iter(self):

        #place Not iterable types in method body as needed

        with self.assertRaises(TypeError):
            ret = max(None)
            
        with self.assertRaises(TypeError):
            ret = max(1)



    def test_TypeError_from_mixed_types(self):

        #place iterables with mixed types in method body as needed

        with self.assertRaises(TypeError):
            ret = max([1,2,'a'])


    def test_ValueError_from_empty(self):

        #place empty sequence in method body as needed

        with self.assertRaises(ValueError):
            ret = max(list())













if __name__ == "__main__":
    unittest.main()
