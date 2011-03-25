#!/usr/bin/env python

import unittest

from prime_factor import PrimeFactor, PrimeFactorError

class Test(unittest.TestCase):
        """Unit tests for googlemaps."""
        def test_input_as_one(self):
            pfactor = PrimeFactor(1)
            pfactor.compute_prime_factors()
            self.assertEqual(pfactor.get_prime_factors(), [])
            
        def test_input_as_zero(self):
            pfactor = PrimeFactor(0)
            self.assertRaises(PrimeFactorError,pfactor.compute_prime_factors)

        def test_input_as_square(self):
            pfactor = PrimeFactor(49)
            pfactor.compute_prime_factors()
            self.assertEqual(pfactor.get_prime_factors(), [7,7])

if __name__ == "__main__":
    unittest.main()
