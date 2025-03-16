import random


guess_number = random.randint(1,50)
user_guess = int(input("Guess a number between 1 to 50:"))

attempt = 0
max_attempt = 5

while attempt < max_attempt:
    user_guess = int(input("Guess a number beteem 1 to 50:"))
    attempt += 1

    if user_guess == guess_number:
        print("You are right")
    elif user_guess < guess_number:
        print("This is too low, think higher")
    elif user_guess > guess_number:
        print("This is too high, think lower")

if attempt == max_attempt:
    print(f"You are out of guesses,the secret number is: {guess_number}")