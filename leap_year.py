n=int(input("Enter number:"))
temp=n
rev=0

while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

import sys
sys.exit(0)

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = input("Enter  a string: ")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")


import sys
sys.exit(0)

# Python program to check if year is a leap year or not

#year = 2000

year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))