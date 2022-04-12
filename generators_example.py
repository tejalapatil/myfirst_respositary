# Python3 code to demonstrate yield keyword

# Checking number of occurrence of
# geeks in string

# generator to print even numbers


def print_even(test_string):
	for i in test_string:
		if i == "are":
			yield i


# initializing string
test_string = " The are many geeks around you, geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0
print ("The number of geeks in string is : ", end = "" )
test_string = test_string.split()

for j in print_even(test_string):
	count = count + 1

print (count)

import sys
sys.exit(0)


# yield keyword

# generator to print even numbers
def print_even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i


# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
    print(j, end=" ")



import sys
sys.exit(0)



import math

def factorial():
    num = int(input("Enter Number: "))

    num1 = math.factorial(num)
    print(num1)

factorial()
import sys
sys.exit(0)


# we can use yield keyword in fun it becomes generator fun...
def mygen():
    n = 1
    yield n
    n += 2
    yield n
    n += 3
    yield n


for n in mygen():
    print(n)



import sys
sys.exit(0)


def mygen():
    yield 10
    yield 20
    yield 30
    yield 40


gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))





