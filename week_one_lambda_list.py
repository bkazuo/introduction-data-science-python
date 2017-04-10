# Example of lambda that takes three parameters and adds the first two
my_function = lambda a,b,c: a + b
print(my_function(1,2,3))
print("---------------")


# Iterating from 0 to 999 and return the even numbers
my_list = []
for number in range(0,1000):
	if number % 2 == 0:
		my_list.append(number)

print(my_list)
print("---------------")


# List comprehension
my_list_2 = [number for number in range(1,1000) if number % 2 == 0]
print(my_list_2)
print("---------------")

# Using lambda to split
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
print(list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))