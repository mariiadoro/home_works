result = ""
people = [
    {"name": "Lennon", "age": 40},
    {"name": "McCartney", "age": 81},
    {"name": "Harrison", "age": 58},
    {"name": "Starr", "age": 83},
]
the_youngest = [person["name"] for person in people if person["age"] == min(person["age"] for person in people)]
print(f"The youngest in the list: {the_youngest}")

the_longest_name = [person["name"] for person in people if len(person["name"]) == max(len(person["name"]) for person in people)]
print(f"The one with the longest name: {the_longest_name}")

sum_age = sum(person["age"] for person in people) / len(people)
print(f"The average age between people in the list: {sum_age}")
