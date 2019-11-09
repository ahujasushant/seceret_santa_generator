from random import *
people = []
while True:
    person = input("Enter a person participating.(end to exit):\n")
    if person == "end":
        break
    people.append(person)


shuffle(people)
offset = [people[-1]] + people[:-1]
for santa, receiver in zip(people, offset):
    print(santa, "buys for", receiver)