'''Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.'''

def move_zeros(array):
    L = [item for item in array if type(item) == bool or item != 0]
    for i in array:
        if type(i) != bool and i ==0:
            L.append(i)
    return L

print(move_zeros([False,1,0,1,2,0,1,3,"a"]))

print(move_zeros([9, 0.0, 9, 1, 2, 1, 1, 0.0, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0]))

print(move_zeros( ['z', -4, -1, -10, '0', -10, 0, 6, 1, -3, 'y', 0, 10, 10, 'c', 2, 'b', -1, 1, 0, 6, 0, 0]))