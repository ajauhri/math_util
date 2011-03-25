#!/usr/bin/env python

import unittest

from prime_numbers import rwh

class Test(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(rwh(11),[2,3,5,7,11])

    def test_prime_numbers_for_one(self):
        self.assertEqual(rwh(1),[])

    def test_prime_numbers_for_two(self):
        self.assertEqual(rwh(2),[2])


if __name__ == "__main__":
    unittest.main()
