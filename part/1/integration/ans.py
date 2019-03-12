#!/usr/bin/env python

import sys

#
# Please try to add 1~3 line of code to finish the integration
# 
# def anonymous(x):
#     return x**2 + 1
# 
# def integrate(fun, start, end):
#     step = 0.1
#     intercept = start
#     area = 0
#     while intercept < end:
#    
# intercept += step
#         ''' your work here '''
#     return area
# 
# print(integrate(anonymous, 0, 10))
#


def anonymous(x):

 return x**2 + 1

def analytical_integral (fun,start,end): # ===

 # fun not used

 I = lambda x : ( x**3 / 3 + x )

 return I(end) - I(start)

#///
def approximate_integral(fun,start,end): # ===

 h = 0.0001
 x = start
 s = 0
 z = 0

 y = [ fun(x), None ]

 while x < end:

  x += h

  y[1] = fun(x)

  # rectangle + triangle at the top

  s += y[0] * h + ( y[1] - y[0] ) * h / 2
  z += y[0]

  y = y[::-1]

 # s ~ (z+(fun(end)-fun(start))/2)*h

 return s

#///

integrate = approximate_integral

#
# Analytical solution
#
# print(analytical_integral(anonymous,0,10))

print(integrate(anonymous, 0, 10))

