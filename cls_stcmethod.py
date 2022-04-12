def modifier(baz):
    baz = 42
    print (baz)


bam = 21
print (bam)
modifier(bam)
print (bam)

import sys
sys.exit(0)

def modifier(value):
    value["foo"] = 25
    print(value)


bar = {}
print(bar)
modifier(bar)
print(bar)

import sys
sys.exit(0)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfun(self):
        print("hello my name is" +self.name)


p1 = Person("john",36)
p1.myfun()

import sys
sys.exit(0)

# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1995)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
