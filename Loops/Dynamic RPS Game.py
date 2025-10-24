import random

rock = "🪨"
paper = "📃"
scissors = "✂️"
print('''Rules of RPS:-  0 for Rock, 1 for Paper, 2 for Scissors
         Rock wins against scissors. (0 wins against 2)
         Scissors win against paper. (2 wins against 1)
         Paper wins against rock.    (1 wins against 0) \n''')

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))

if 0 <= user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Hurray , You Win . 🥳🥳🥳")
elif computer_choice == 0 and user_choice  == 2:
    print("You Lose. 👎👎👎")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice > computer_choice:
    print("Hurray , You Win . 🥳🥳🥳")
elif user_choice < computer_choice:
    print("You Lose. 👎👎👎")
