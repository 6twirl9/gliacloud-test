#!/usr/bin/env python

import sys

#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#
# The sum of these multiples is 23.
#
# • Find the sum of all the multiples of 3 or 5 below 1000.
#


top = 10 if len(sys.argv) != 2 else int(sys.argv[1])

def foobar(top,reduce,*cut):

 return sum(( _ for _ in range(top) if reduce([ ( _ % c ) == 0 for c in cut])))

print(f'Sum of multiples of 3 or 5 for natural numbers below {top}')
print('Ans: {}'.format(foobar(top,any,3,5)))

