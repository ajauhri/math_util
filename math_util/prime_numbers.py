#!/usr/bin/env python
# Copyright (C) 2011 Abhinav Jauhri
# This is free software, licensed under the Lesser Affero General
# Public License, available in the accompanying LICENSE.txt file. 

__all__ = ['PrimeNumbers']


class PrimeNumbers(object):
    """
    Python wrapper to print prime number <= lim
	
    An easy-to-use Python wrapper to print prime factors of an integer

    >>> from math_util import PrimeNumebers
    >>> prime_numbers = PrimeNumbers(11)
    >>> list = prime_numbers.rwh()
    >>> print list
    [2,3,5,7,11]

    """
    def __init__(self, lim):
        """
        Create a new :class:`PrimeNumbers` object using the given `lim`.

        :param lim: Integer for which prime factors have to be generated
        :type lim: int
        """
        self.lim = lim

    def rwh(self):
        """
        Prints prime numbers <= lim using sieve algorithm
        :return: List of prime numbers
        :rtype: list
        """
        if self.lim is 1:
            return []
        self.lim = self.lim+1
        sieve = [True] * (self.lim/2)
        for i in xrange(3, int(self.lim**0.5)+1, 2):
            if sieve[i/2]:
                sieve[i*i/2::i] = [False] * ((self.lim-i*i-1)/(2*i)+1)
        return [2] + [2*i+1 for i in xrange(1, self.lim/2) if sieve[i]]
