'''Introduce a list of number pairs and return the sum of the numbers;
return "zero" if the value is == 0. Use one line and an anonymous function
to complete the challenge.'''

tuples = [(0,0),(20,1),(1,4),(6,9),(8,10),(30,3),(0,0),(1,0),(10,20)]

s = list(map(lambda n: sum(n) if sum(n) > 0 else 'Zero', tuples))

print(s)

inst = '''Write a function that searchs for a word inside a string and
returns a text slice with a range of +20 and -20 characters from
the point of the searched word'''

find = lambda s, q: s[s.find(q)-20:s.find(q)+20 if q in s else None]

print(find(inst, 'slice'))