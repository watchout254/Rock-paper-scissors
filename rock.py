import random
import sys

print("\tWelcome to Rock,paper and scissors game")
print("Rock = 0\n"
      "Paper = 1\n"
      "Scissors = 2")
print("0. Rock\n"
      "1. Paper\n"
      "2. Scissors")
selection = int(input("Enter your choice: "))
if selection >= 3 or selection < 0:
    print("Shutting program down, enter numbers 0-2 next time")
    sys.exit()
else:
    if selection == 0:
        print("you've chosen rock")
    elif selection == 1:
        print("you've chosen paper")
    else:
        print("You've chosen scissors")

    compChoice = random.randint(0,2)
    print(f"Computer chose: {compChoice}")

    if compChoice == selection:
        print("It's a draw")
    elif compChoice == 0 and selection == 2:
        print("You lose bana")
    elif selection == 0 and compChoice == 2:
        print("You've won!!!")
    elif compChoice > selection:
        print("You lose mahn")
    elif selection > compChoice:
        print("You win")



