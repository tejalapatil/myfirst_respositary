from pickle import *

class student:
    def __init__(self):
        self.name = "rohit"
        self.age = 21
        self.rollno = 19

    def show_details(self):
        print("name:",self.name,"age:",self.age,"rollno:",self.rollno)


s1 = student()
"""f = open("pickle.txt","wb")
dump(s1,f)
f.close()"""


f= open("pickle.txt","rb")
s1 = load(f)
s1.show_details()

