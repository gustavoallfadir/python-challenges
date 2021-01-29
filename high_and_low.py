""" In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number. """

def high_and_low(numbers): 
    ints = [int(n) for n in numbers.split(' ')]
    return " ".join((str(max(ints)),str(min(ints))))


a = high_and_low("1 2 3 4 5")  # return "5 1"
print(a)
b = high_and_low("1 2 -3 4 5") # return "5 -3"
print(b)
c = high_and_low("1 9 3 4 -5") # return "9 -5"
print(c)
d = high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") # return "542 -214"
print(d)