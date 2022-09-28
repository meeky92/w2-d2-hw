# Create a list of numbers that are less than ten using l_1 and list comprehension
# Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]

#fxn will accept nums
#data type is list
#take list and return a new list with numbers less than 10

# for i in l_1:
#     if i in range(1,11):
#         print(i)

l_1 = [1,11,14,5,8,9]

l_1 = [i for i in l_1 if i in range(1,11)]
print(l_1)


#Using list comprehension, create a list of names of 4 letters or more and capitalize each name
# Output: ['Connor', 'Connor', 'Connor', 'Evan', 'Evan', 'Kevin']

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
names2 = [i.title() for i in names1 if len(i) > 3]
print(names2)

# for i in names1:
#     if len(i) > 3:
#         print (i.title())

