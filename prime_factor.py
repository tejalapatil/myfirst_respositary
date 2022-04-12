import string
import random
S = 10
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
print("The randomly generated string is : " + str(ran))


import sys
sys.exit(0)


n = int(input("Enter a number: "))
rev =0

while n > 0:
    dig = n%10

rev = rev*10+dig
n = n/10

print("the reverse number:", rev)

import sys
sys.exit(0)


import random
list =[2,3,4]
l1 = list * 2
print(l1)
print(sum(range(10,1000)))

import sys
sys.exit(0)


list1=['a', 'j', 'i', 'n', 'k', 'y', 'a']
b=random.randint(0,6)
print(list1[b])


import sys
sys.exit(0)

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   #print("{0} is Odd".format(num))
    print(num,"is Odd")


import sys
sys.exit(0)


# Program to check if a number is prime or not

num = int(input("Enter a num: "))

flag = False

if num > 1:
    for i in range (2,num):
        if (num %  i) == 0:
          flag = True
          break

if flag:
    print(num,"is not prime number")
else:
    print(num,"is prime number")

