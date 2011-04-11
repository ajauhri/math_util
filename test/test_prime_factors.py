#!/usr/bin/env python

import unittest

from prime_factors import PrimeFactors, PrimeFactorsError


class Test(unittest.TestCase):

        def test_input_as_one(self):
            pfactor = PrimeFactors(1)
            self.assertEqual(pfactor.compute_prime_factors(), [])
            
        def test_input_as_zero(self):
            pfactor = PrimeFactors(0)
            self.assertRaises(PrimeFactorsError,pfactor.compute_prime_factors)

        def test_input_as_square(self):
            pfactor = PrimeFactors(49)
            self.assertEqual(pfactor.compute_prime_factors(), [7,7])

if __name__ == "__main__":
    unittest.main()
