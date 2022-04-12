
def function(a):
    return a*a
x = map(function, (1,2,3,4))  #x is the map object
print(x)
print(set(x))


import datetime

dateandtime= datetime.datetime.now()
print(repr(dateandtime))


for index, value in enumerate(["milk","water","drink","gfgj"]):
    print(index,value)


import sys
sys.exit(0)


# itertors are defined by using iter() and and access the elements using function next()

for character in "Tejal":
    print(character)

import sys
sys.exit(0)

nums = [1,2,3,4,5,6]
nums_iter = iter(nums)
print(nums_iter)

# to print next function to the elements
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))

