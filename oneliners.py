'''Introduce a list of number pairs and return the sum of the numbers;
return "zero" if the value is == 0. Use one line and an anonymous function
to complete the challenge.'''

tuples = [(0,0),(20,1),(1,4),(6,9),(8,10),(30,3),(0,0),(1,0),(10,20)]

s = list(map(lambda n: sum(n) if sum(n) > 0 else 'Zero', tuples))

print(s)

instruction = '''Write a function that searches for a word inside a string and
returns a text slice with a range of +15 and -15 characters from
the point of the searched word'''

find = lambda s, q: '...' + s[s.find(q)-15:s.find(q)+15] + '...' if q in s else None

print(find(instruction, 'searches'))
print(find(instruction,'range'))