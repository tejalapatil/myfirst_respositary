import json

person = {
    'first_name': "John",
    "isAlive": True,
    "age": 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    },
    "hasMortgage": None
}


"""with open('person.json', 'w') as f:
        json.dump(person,f)"""


open('person.json', 'r').read()
