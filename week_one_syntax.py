## add_numbers is a function that takes two numbers and adds them together.
def add_numbers(x, y):
	return x + y

print("First example result:" + str(add_numbers(1, 2)))
print("---------------")

## add_numbers updated to take an optional 3rd parameter. Using print allows printing of multiple expressions within a single cell.
def add_numbers_2(x, y, z=None):
	if (z == None):
		return x + y
	else:
		return x + y + z

print("Second example result:" + str(add_numbers_2(1, 2, 3)))
print("---------------")

# The flag parameter does not have to be the third in the call function list
def add_numbers_3(x, y, z=None, flag=False):
	if (flag):
		print('Flag is true!')

	if (z == None):
		return x + y
	else:
		return x + y + z

print("Third example result:" + str(add_numbers_3(1, 2, flag=True)))
print("---------------")

## Assign function add_numbers to variable a.
a = add_numbers
print("Forth example result:" + str(a(1,2)))
print("---------------")


# Types and Sequences
b = type('This is a string')
print(b)
print("---------------")

c = type(None)
print(c)
print("---------------")

d = type(1)
print(d)
print("---------------")

e = type(1.0)
print(e)
print("---------------")

f = type(add_numbers)
print(f)
print("---------------")

x = type((1, 'a', 2, 'b'))
print(x)
print("---------------")

y = type([1, 'a', 2, 'b'])
print(y)
print("---------------")

y = [1, 'a', 2, 'b']
y.append(3)
print(y)
print("---------------")

# For in python
for item in y:
	print(item)
print("---------------")

# While
i = 0
while(i != len(y)):
	print(y[i])
	i = i + 1
print("---------------")

# Concatenating lists
g = [1,2] + [3,4]
print(g)
print("---------------")

h = [1] * 3
print(h)
print("---------------")

# Check if operator is inside a list
print(1 in [1,2,3,4])
print("---------------")

i = 'This is a string'
print(i[0])
print(i[0:1])
print(i[0:2])
print(i[-1])
print(i[-4:-2])
print(i[:3])
print("---------------")

firstname = 'Christopher'
lastname = 'Brooks'
print(firstname + ' ' + lastname)
print(firstname * 3)
print('Chris' in firstname)
print("---------------")

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0]
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]
print(firstname + ' ' + lastname)
print("---------------")

# Make sure you convert objects to strings before concatenating
print('Chris' + str(2))
print("---------------")

# Dictionary
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
print(x['Christopher Brooks'])
print("---------------")

x['Kevyn Collins-Thompson'] = None
print(x['Kevyn Collins-Thompson'])
print("---------------")

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
for email in x.values():
	print(email)
print("---------------")

for name, email in x.items():
	print(name)
	print(email)
print("---------------")

x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname)
print(lname)
print(email)
print("---------------")

sales_record = {
	'price': 3.24,
	'num_items': 4,
	'person': 'Chris'
}
sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'
print(sales_statement.format(	sales_record['person'],
								sales_record['num_items'],
								sales_record['price'],
								sales_record['price'] * sales_record['num_items']))

