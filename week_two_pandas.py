import pandas as pd
import numpy as np

animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))
print("---------------")

numbers = [1, 2, 3]
print(pd.Series(numbers))
print("---------------")

animals = ['Tiger', 'Bear', None]
print(pd.Series(animals))
print("---------------")

numbers = [1, 2, None]
print(pd.Series(numbers))
print("---------------")

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'
          }
s = pd.Series(sports)
print(s)
print(s.index)
print("---------------")


s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print(s)
print("---------------")

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print(s)
print("---------------")

# Querying a Series
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}

s = pd.Series(sports)
print(s)
print("---------------")
print(s.iloc[3])
print("---------------")
print(s.loc['Taekwondo'])
print("---------------")
print(s[3])
print("---------------")
print(s['Taekwondo'])
print("---------------")

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
print(s)
print("---------------")
print(s.iloc[0])
print("---------------")
print(s)
print("---------------")

s = pd.Series([100.00, 120.00, 101.00, 3.00])

total = 0
for item in s:
    total+=item
print(total)
print("---------------")


total = np.sum(s)
print(total)
print("---------------")

s = pd.Series(np.random.randint(0,1000,10000))
# print(s)
print(s.head()) # It gets the first 5 elements of the series
print("---------------")

print(len(s))
print("---------------")

summary = 0
for item in s:
    summary+=item

print(summary)
print("---------------")

summary2 = np.sum(s)
print(summary2)
print("---------------")

print(s.head())
s+=2
print(s.head()) # adds two to each item in s using broadcasting
s-=2
print("---------------")

# The same thing as the previous chunk of code
print(s.head())
for label, value in s.iteritems():
    s.set_value(label, value+2)
print(s.head()) # adds two to each item in s using broadcasting
print("---------------")

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
print(s)
print("---------------")

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])

all_countries = original_sports.append(cricket_loving_countries)
print(all_countries)
print("---------------")
print(all_countries.loc['Cricket'])
print("---------------")


# The DataFrame Data Structure
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print(df)
print("---------------")
print(df.loc['Store 2'])
print(type(df.loc['Store 2']))
print("---------------")
print(df.loc['Store 1'])
print("---------------")
print(df.loc['Store 1', 'Cost'])

print("---------------")

df.T
print(df.T.loc['Cost'])
print(df.loc['Store 1']['Cost'])
print("---------------")

print(df.loc[:,['Name', 'Cost']])
print("---------------")

print(df.drop('Store 1'))
print("---------------")

copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)
print("---------------")

copy_df = df.copy()
print(copy_df)
del copy_df['Name']
print(copy_df)
