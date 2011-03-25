#!/usr/bin/env python
__all__ = ['rwh']

def rwh(n):
	if n is 1:
		return []
	n = n+1
	sieve = [True] * (n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

