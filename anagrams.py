'''Write a function that will find all the anagrams of a word from a list. You will be 
given two inputs a word and an array with words. You should return an array of all the 
anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']'''

def anagrams(word, words):
    wlist = [w for w in words if sorted(w)==sorted(word)]
    return wlist

a = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) 
#Returns['aabb', 'bbaa']
print(a)
b = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) 
#Returns ['carer', 'racer']
print(b)
c = anagrams('laser', ['lazing', 'lazy',  'lacer']) 
#Returns []
print(c)