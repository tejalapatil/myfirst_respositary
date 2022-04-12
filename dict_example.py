
email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain}")

import sys
sys.exit(0)

list1 = ["A","B","C","A","B"]
list2 = ["V1","V2","V3","v1","V1"]


def create_dec(list1,list2):
    dictionary ='{'
    for i,k in enumerate(list1):
        dictionary = dictionary+'\''+list1[i]+'\':\''+list2[i]+'\','
    dictionary = dictionary[:-1]+'}'
    return dictionary


mydictionary = create_dec(list1,list2)
print("type of dict:" ,type(mydictionary))
print(mydictionary)

import sys
sys.exit(0)

from collections import defaultdict

test_list1 = ["A","B","C","A","B"]
test_list2 = ["V1","V2","V3","v1"]
new_dict = defaultdict(set)
for m,n in zip (test_list1, test_list2):
    new_dict[m].add(n)

print(new_dict)