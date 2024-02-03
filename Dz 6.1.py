people = [
    {"name": "John", "age": 26},
    {"name": "Al", "age": 12},
    {"name": "Bob", "age": 15},
    {"name": "Jack", "age": 45}
]

#  Знайти наймолодших
min_age = min(person["age"] for person in people)
youngest_names = [person["name"] for person in people if person["age"] == min_age]

#  Знайти найдовші імена
max_length = max(len(person["name"]) for person in people)
longest_names = [person["name"] for person in people if len(person["name"]) == max_length]

#  Знайти середній вік
average_age = sum(person["age"] for person in people) / len(people)

print("Наймолодші:", youngest_names)
print("Найдовші імена:", longest_names)
print("Середній вік:", average_age)