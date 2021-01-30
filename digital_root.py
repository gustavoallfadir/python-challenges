'''Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced. The input
will be a non-negative integer.'''

def digital_root(n):
    while len(str(n)) > 1:
        n = sum(int(i) for i in str(n))
    return n

a = digital_root(16) #returns 7
print(a)
b = digital_root(15) #returns 6
print(b)
c = digital_root(24) #returns 6
print(c)
d = digital_root(29) #returns 2
print(d)