# Python program to check if the number is an Armstrong number or not

#num = 1634
num = int(input("Enter a number: "))

# Changed num variable to string,
# and calculated the length (number of digits)

order = len(str(num))
#print(order)
# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


import sys
sys.exit(0)

num = int(input("Enter a number: "))

#inistiliaze sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num==sum:
  print(num," is a amstrong number")
else:
    print(num," is not amstrong number")

import sys
sys.exit(0)

# Multiplication table (from 1 to 10) in Python

# num = 12

    # To take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

