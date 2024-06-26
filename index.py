0 points: Student meets none of or only a few of the requirements, does not seem to understand what is being asked of them.

1 point: Student meets a majority of the requirements and has a solid understanding of the task, however shows some gaps.

2 points: Student meets all of the requirements and has a good understanding of the task.

Understanding of Course Work (2 points):

Used the skills learned from class.

When run, the code works correctly as intended.

Code is well written and efficient.

0 points: Student's code has multiple bugs, does not show an understanding of how to complete the assignment.

1 point: Student's code has 3 or less bugs, seems to have an understanding of the assignment, but may need some more guidance.

2 points: Student's code works as intended, has 1 or less bug and shows a complete understanding of the assignment.

Extra Point for Extra Work (1 point):

Edge cases are considered and errors are caught.

Does more than just minimum requirements.

0 points: Student did only minimum amount required.

1 point: Student went above and beyond in assignment, challenged self, etc.
Lists
Declaring Lists
list_1 = []

names = ['Max','Cindy', 'Kathy', "bob", 'Nate']
print(names)
['Max', 'Cindy', 'Kathy', 'bob', 'Nate']
Indexing a List
#  list_name[start: stop: step]

# Single Index
print(names[0])

# Print starting at index 1 going to the end
print(names[1:])

# Print starting at the beginning of a list up until a number
print(names[:2])

# Print starting at index 1 and going up BY 2 in each iteration
print(names[1::2])

# Print starting at the back and display in reverse order
print(names[::-1])
Max
['Cindy', 'Kathy', 'bob', 'Nate']
['Max', 'Cindy']
['Cindy', 'bob']
['Nate', 'bob', 'Kathy', 'Cindy', 'Max']
.append()
names.append('Brandon')
print(names)
['Max', 'Cindy', 'bob', 'Nate', 'Brandon', 'Brandon', 'Brandon']
.insert()
names.insert(3, 'Devon')
print(names)
['Max', 'Cindy', 'bob', 'Devon', 'Nate', 'Brandon', 'Brandon', 'Brandon']
.pop()
# Defaults to the last value if no parameter is given
# Pop returns the element that was removed in case you want to assign it to a varable

my_name = names.pop(2)
print(my_name)
print(names)
Kathy
['Max', 'Cindy', 'bob', 'Nate']
.remove()
# Value to be removed rather than index
# names.remove('bob')
# print(names)

# remove multiple brandons from list
while 'Brandon' in names:
    names.remove('Brandon')
print(names)
['Max', 'Cindy', 'Devon', 'Nate']
del()
Concatenating Two Lists
# Will append two lists together, will NOT add the values!!

list_2 = [0, 1, 2]
list_3 = [3, 4, 5]

large_list = list_2 + list_3
print(large_list)
[0, 1, 2, 3, 4, 5]
Lists Within Lists

# Lists can hold ANY type of other element! Including other lists!
# They can go as deep as you want; this is called nested lists

names = ["Max", "sam", "Josh", ["Sally", ["Sue", "Jim"],"Tameka"]]
print(names)
print(names[3][1][1])
['Max', 'sam', 'Josh', ['Sally', ['Sue', 'Jim'], 'Tameka']]
Jim
Looping Through Lists
# Two ways to loop through a list! One is by index; the other is by using the 'in' keyword

# By index
for i in range(len(names)):
    print(names[i])

# Loop with 'in'
for name in names:
    print(name)
Max
sam
Josh
['Sally', ['Sue', 'Jim'], 'Tameka']
Max
sam
Josh
['Sally', ['Sue', 'Jim'], 'Tameka']