import random
number= random.randint(1,20)
print("I am thinking of a number between 1 to 20")
global guess

for guess_taken in range(1,6):
    guess = int(input("Make a guess:- "))

    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")
    else:
        break
 
if guess == number:
    print(f"Good Job, you've guessed the correct number in just {guess_taken} guesses")
else:
    print(f"You failed,  The number I was thinking of was {number}")







