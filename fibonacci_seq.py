# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("Enter how many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("You enter positive number")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
else:
    print("Fibonacci sequence: ")
    while count < nterms:  # 0 < 5
        print(n1)          #0
        nth = n1 + n2       #1
        n1 = n2             #1
        n2 = nth            #1
        count +=1              #1


#0,1,1,2,3,5,8






