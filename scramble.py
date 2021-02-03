'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered
'''

#Using loop, slower
#def scramble(s1, s2):
#    for i in s2:
#        if i in s1:
#            s1 = s1.replace(i,'',1)
#        else:
#            return False
#    return  True


#faster 
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0


print(scramble('rkqodlw', 'world'),  True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
print(scramble('cxtlpxdahtvwtzikw','xatdpwtizvhkxtcwl'), True)