'''Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks 
whether the two arrays have the "same" elements, with the same multiplicities. "Same" 
means, here, that the elements in b are the elements in a squared, regardless of the order.'''

def comp(array1, array2):
    t = True
    for y in array2:
        if t == False:
            break
        for x in array1:
            if y == x*x:
                t = True
                break
            else:
                t = False
    return t          


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) #true

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) #false

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) #false