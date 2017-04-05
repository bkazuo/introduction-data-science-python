import csv

# %precision 2

with open('MOCK_DATA.csv') as csvfile:
    people = list(csv.DictReader(csvfile))
    
# The first three dictionaries in our list.
print(people[:3])
print("---------------")

# key gives us the column names of our csv
print(people[0].keys())
print("---------------")

# Find the average age
age_average = sum(int(person['age']) for person in people) / len(people)
print('Average age ' + str(age_average))
print("---------------")

# Get the unique values for the age of people
ages = set(person['age'] for person in people)
print(ages)
# print(type(ages))
print("---------------")

# Iterating all over the people and ages levels
ages_grouped = []
for age in ages:
	number_of_people = 0
	for person in people:
		if age == person['age']:
			number_of_people += 1
	ages_grouped.append((int(age), number_of_people))
print(sorted(ages_grouped))
print("---------------")

for age, total in sorted(ages_grouped):
	print('There are ' + str(total) + ' people with ' + str(age) + ' years.')
print("---------------")
