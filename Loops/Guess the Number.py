import random

secrete_num = random.randint(1,20)
print("Welcome to the Number Guessing.")

user_choice = 0
for guesses_taken in range(1,7):
    print("Take a guess")
    user_choice = int(input("> "))
    if user_choice < secrete_num:
        print("Your guess is too low.")
    elif user_choice > secrete_num:
        print("Your guess is too high.")
    else:
        break

if user_choice == secrete_num:
    print("Correct guess")
else:
    print("Nope the num is", secrete_num)
