from random import *
people = []
while True:
    person = input("Enter a person participating.(end to exit):\n")
    if person == "end":
        break
    people.append(person)


shuffle(people)
people_list = [people[-1]] + people[:-1]
for santa, receiver in zip(people, people_list):
    print(santa, "buys for", receiver)