""" Flow Control Statements """

# 1. if   --> checks a condition; runs its block if true. 
# 2. elif --> checks another condition if previous ones were false, also used for check for multiple conditions.
# 3. else --> runs its block if none of the above conditions were true.

# 1. if:-

name = "John Wick"
if name == "John Wick":
    print("Hi, BabaYaga")


# 2. else:- 

name = "John Wick"
if name == " Wick":
    print("Hi, BabaYaga")
else:
    print("Hello,Stranger")

# 3. elif:- 
name = "John Wick"
age = 60
if name == "John Wick":
    print("Hi, BabaYaga")
elif age < 18:
    print("You are not John, Kiddo")

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')


name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print("You are neither alice nor little ")
    