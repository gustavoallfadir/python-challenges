def isAlmostPalindrome(word):
    "Returns true if a word is a palindrome"
    word = word
    word_backwards = word[::-1]
    
    count = 0
    for i in range(int(len(word)/2)):
        for x in word[i]:
            print(i)
            print(x)
            print(word_backwards[i])
            if x != word_backwards[i]:
                count = count+1

    print(count)
    if count <= 1:
        return True
    else:
        return False


from math import sqrt


def avg_distance(x1,y1,x2,y2,x3,y3):
    "returns the average distance beetween 3 fiven coodinates"
    d1 = sqrt(pow((x2-x1),2) + pow((y2-y1),2))
    d2 = sqrt(pow((x3-x1),2) + pow((y3-y1),2))
    d3 = sqrt(pow((x2-x3),2) + pow((y2-y3),2))
    avg_distance = (d1+d2+d3)/3
    return avg_distance


def most_frequent(List): 
    "Returns the most frequent element in a list"
    max_frequency = 0
    most_frequent = List[0] 
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> max_frequency): 
            max_frequency = curr_frequency 
            most_frequent = i 
    print('max frequency is:', max_frequency)
    return most_frequent 
  
List = [2,1,5,7,8,1,2,8,9,1,2,2,1,3,3,3,3,3]
print('most frequeny number is:', most_frequent(List)) 

#I've lost the instruction given for the next 2 excercises, sorry.
def get_numbers_in_number(num_searched,num_given):
    count = 0
    for i in range(0,num_given):
        for x in str(i):
            if x == str(num_searched):
                count = count+1
    return count

print(get_numbers_in_number(6,1535))


dias = ['lun','mar','mier','jue','vier','sab','dom']
dia = []
count = 0

for i in range(1,180):
    for j in dias:
        if j[i] == 'lun':
            count = count+1

print(count)