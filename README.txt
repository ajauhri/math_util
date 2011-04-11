math_util 1.0
March 18, 2011

README
----------------------
A simple python package with the following functionalities:
  - Prime number generation <= `n`: Computes prime numbers using a sieve technique.

  Usage:
	>>> from prime_factors import PrimeNumbers
	>>> obj = PrimeNumbers(11)
	>>> print obj.rwh() #rwh(): Uses a sieve algorithm to compute (Reference: # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188)
	    

 
  - Prime factor generation <= `n`: Computes prime factors in ascending order for an intger `n`

   Usage:
	>>> from prime_factors import PrimeFactors
	>>> obj = PrimeFactors(11)
	>>> print obj.compute_prime_factors()
	[11]




