'''Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only if the 
original word was capitalized (known as Upper Camel Case, also often referred to as 
Pascal case).'''

import re
def to_camel_case(text):
    return "".join(w if re.split('-|_',text).index(w) == 0 and w.islower()\
        else w.title() for w in re.split('-|_',text))


print(to_camel_case("the-stealth-warrior")) #theStealthWarrior
print(to_camel_case("The-Stealth-Warrior")) #TheStealthWarrior