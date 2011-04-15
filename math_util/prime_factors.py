#!/usr/bin/env python
# Copyright 2011 Abhinav Jauhri
#
# This is free software, licensed under the GNU LESSER GENERAL PUBLIC LICENSE
# Public License, available in the accompanying LICENSE.txt file

from prime_numbers import PrimeNumbers

__all__ = ['PrimeFactors', 'PrimeFactorsError']

class PrimeFactorsError(Exception):
    """Base class for errors in the :mod:`compute_prime_factors` module.

    Mehtods of the :class:`PrimeFactor` raise this when unexpected behaviour occurs.
    """
    
    def __init__(self, error):
        """Create an exception with an error message.

        :param error: The actual error message
        :type error: string
        """
        self.error = error

    def __str__(self):
        """Return a string representaion of the :exc:`PrimeFactorError`."""
        return repr("Exception: "+self.error)


class PrimeFactors(object):
    """
    An easy-to-use Python wrapper to print prime factors of an integer

    >>> from math_util import PrimeFactors
    >>> prime_factors = PrimeFactors(15)
    >>> list = prime_factors.compute_prime_factors()
    >>> print list
    [3,5]
    """
    def __init__(self, integer=0):
        """
        Create a new :class:`PrimeFactors` object using the given `num`.

        :param num: Integer for which prime factors have to be generated
        :type num: int
        """
        self.integer = integer
        self.prime_factors = list()

    def compute_prime_factors(self):
        """
        Computes the prime fators for a given integer.
        :return: List of prime factors
        :rtype: list
        :raises PrimeFactor Error: if something unexpected happens
        """
        if self.integer < 1:
            raise PrimeFactorsError('Value less than one is not accepted')
        else:
            prime_number_generator = PrimeNumbers(self.integer)
            prime_numbers = prime_number_generator.sieve_of_atkin()
            count = 0
            while self.integer is not 1:
                while self.integer  % prime_numbers[count] is 0:
                    self.integer /= prime_numbers[count]
                    self.prime_factors.append(prime_numbers[count])
                count = count + 1
        return self.prime_factors
    
    
if __name__ == "__main__":
    import sys
    def main(argv):
        if len(argv) is not 2:
            print PrimeFactors.__doc__
            sys.exit(1)
        try:
            obj = PrimeFactors(int(argv[1]))
            print obj.compute_prime_factors()
        except PrimeFactorsError, err:
            sys.stderr.write('%s\n' % err) 
            sys.exit(1) 

    main(sys.argv)
     
