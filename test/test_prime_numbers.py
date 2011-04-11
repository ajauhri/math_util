#!/usr/bin/env python

import unittest

from prime_numbers import PrimeNumbers

class Test(unittest.TestCase):

    def test_prime_numbers(self):
        prime = PrimeNumbers(11)
        self.assertEqual(prime.rwh(),[2,3,5,7,11])

    def test_prime_numbers_for_one(self):
        prime = PrimeNumbers(1)
        self.assertEqual(prime.rwh(),[])

    def test_prime_numbers_for_two(self):
        prime = PrimeNumbers(2)
        self.assertEqual(prime.rwh(),[2])


if __name__ == "__main__":
    unittest.main()
