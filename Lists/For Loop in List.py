supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
print()

# Using the enumerate() Function with Lists
for index, item in enumerate(supplies):
    print('Index ' + str(index) + 'in supplies is: ' + item)
print()

# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'he-yes']
print("The index of 'hi' is", spam.index('hi'))
