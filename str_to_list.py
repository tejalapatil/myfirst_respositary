
def str_to_list(string):
    # Insert your code here
    str1 = string.replace(' ', '')
    list1 = []
    list1[:0] = str1
    return list1


string = "5 abcd"
print(str_to_list(string))


import sys
sys.exit(0)


def Convert(string):
    li = list(string.split(" "))
    return li


# Driver code
str1 = "Geeks for Geeks"
print(Convert(str1))

import sys
sys.exit(0)

def convert(s):
    new = ""

    for x in s:
        new += x
    return new

s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))


