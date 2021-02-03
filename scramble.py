'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered
'''

def scramble(s1, s2):
    for i in s2:
        try:
            s1.index(i)
            s1 = s1.replace(i,'',1)
        except:
            return False
    return  True


print(scramble('rkqodlw', 'world'),  True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
print(scramble('cxtlpxdahtvwtzikw','xatdpwtizvhkxtcwl'), True)