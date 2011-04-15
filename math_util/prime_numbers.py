#!/usr/bin/env python
# Copyright (C) 2011 Abhinav Jauhri
# This is free software, licensed under the GNU LESSER GENERAL PUBLIC LICENSE
# Public License, available in the accompanying LICENSE.txt file

__all__ = ['PrimeNumbers']

class PrimeNumbers(object):
    """
    Python wrapper to print prime number <= lim
	
    An easy-to-use Python wrapper to print prime factors of an integer

    >>> from math_util import PrimeNumebers
    >>> prime_numbers = PrimeNumbers(11)
    >>> list = prime_numbers.sieve_of_atkin()
    >>> print list
    [2,3,5,7,11]

    """
    def __init__(self, limit):
        """
        Create a new :class:`PrimeNumbers` object using the given `lim`.

        :param lim: Integer for which prime factors have to be generated
        :type lim: int
        """
        self.limit = limit

    def sieve_of_atkin(self):
        """
        Prints prime numbers <= lim using sieve algorithm
        :return: List of prime numbers
        :rtype: list
        """
        # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        if self.limit is 1:
            return []
        self.limit = self.limit + 1
        sieve = [True] * (self.limit / 2)
        for i in xrange(3, int(self.limit ** 0.5) + 1, 2):
            if sieve[i/2]:
                sieve[i*i/2:i] = [False] * ((self.limit-i * i-1)/(2*i) + 1)
        return [2] + [2*i + 1 for i in xrange(1, self.limit / 2) if sieve[i]]
