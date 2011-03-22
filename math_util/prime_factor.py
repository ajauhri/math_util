#!/usr/bin/env python

from prime_numbers import rwh

__all__ = ['PrimeFactor', 'PrimeFactorError']


class PrimeFactorError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return repr("Exception: "+self.error)


class PrimeFactor(object):

    def __init__(self, num=0, prime_factors=[]):
        self.num = num
        self.prime_factors = prime_factors

    def compute_prime_factors(self):
        if self.num < 1:
            raise PrimeFactorError('Value less than one is not accepted')
        else:
            prime_numbers = rwh(self.num+1)
            num = self.num
            count = 0
            while num is not 1:
                while num%prime_numbers[count] is 0:
                    num /= prime_numbers[count]
                    self.prime_factors.append(prime_numbers[count])
                count = count + 1

                
    def get_prime_factors(self):
        return self.prime_factors

    
if __name__ == "__main__":
    import sys

    def main(argv):
        if len(argv) is not 2:
            # print main.__doc__
            sys.exit(1)
        try:
            obj = PrimeFactor(int(argv[1]))
            obj.compute_prime_factors()
            print obj.get_prime_factors()
        except PrimeFactorError, err:
            sys.stderr.write('%s\n' % err) 
            sys.exit(1) 

    main(sys.argv)
    
    
