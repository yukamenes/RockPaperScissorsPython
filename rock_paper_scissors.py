import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#FIRST OPTION
"""
yourChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and"
                   " 2 for Scissors:\n"))
possibleVariations = ["rock", "paper", "scissors"]
if yourChoice != 0 and yourChoice != 1 and yourChoice !=2:
    print("You print wrong number. Try again!")
else:
    if yourChoice == 0:
        print(rock)
    elif yourChoice == 1:
        print(paper)
    elif yourChoice == 2:
        print(scissors)

    print("Computer Choice:")
    computerChoice = choice(possibleVariations)
    if computerChoice == "rock":
        print(rock)
    elif computerChoice == "paper":
        print(paper)
    else:
        print(scissors)

    if (yourChoice == 0 and computerChoice == "rock") or (yourChoice == 1 and computerChoice == "paper")  or (yourChoice == 2 and computerChoice == "scissors"):
        print("It`s a draw")
    elif (yourChoice == 0 and computerChoice == "paper") or (yourChoice == 1 and computerChoice == "scissors") or (yourChoice == 2 and computerChoice == "rock"):
        print("You lose")
    else:
        print("You win")
"""

#SECOND OPTION
list = [rock,paper,scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and"
                       " 2 for Scissors:\n"))
computerChoice = random.randint(0,2)
if userChoice <0 or userChoice > 2:
    print("Tou print wrong number")
else:
    print(list[userChoice])
    print("Computer choice:")
    print(list[computerChoice])
    if  userChoice == computerChoice:
        print("It`s a draw")
    elif userChoice == 0 and computerChoice == 2:
        print("You win!")
    elif userChoice == 2 and computerChoice == 0:
        print("You lose!")
    elif userChoice > computerChoice:
        print("You win!")
    elif computerChoice > userChoice:
        print("You lose")





