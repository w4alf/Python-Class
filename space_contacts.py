#NOte: you must have requests installed to run this code. You can install it by running pip install requests in the terminal
#This code will print the names of the people currently in space

import requests
people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()
print(json)

print('the people currently in space are:')
for person in json['people']:
    print(person['name'])
    

