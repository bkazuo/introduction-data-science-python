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
