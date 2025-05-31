# odd or even number guesser

while True:
    print("\nWelcome to the odd or even number guesser\nInput your number and the computer guesses if it's odd or even")
    choice = input("Enter your number (Or type q to quit):")

    if choice.lower() == 'q':
       print("Thank you for playing")
       break

    number = int(choice)

    if number % 2  == 0:
        print("This is an even number")
    else:
        print("This is an odd number")


