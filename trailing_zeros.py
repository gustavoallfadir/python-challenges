'''
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html 
'''

from math import factorial
def zeros(n):
    z = 0
    for x in str(factorial(n))[::-1]: 
        if x == '0': 
            z += 1
        else:
            break
    return z

print(zeros(0)) # return 0
print(zeros(6)) #return 1
print(zeros(30)) #return 7