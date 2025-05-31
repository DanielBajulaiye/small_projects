import random

choices = ["rock","paper","scissors"]
computer = random.choice(choices)

player = input("Let us play a game of rock, paper,scissors. Pick one:").lower().strip()

if player == computer:
    print("This is a tie!")
elif(player == "")