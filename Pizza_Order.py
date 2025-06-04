# print("Welcome to Python Pizza deliveries")
# size = input("What size of pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
# extra_cheese = input("Do you want cheese? Y or N:")

while True:

    bill = 0

    print("Welcome to the pizza palaceé!")

    size = input("What size of pizza do you want? S, M or L:").lower()
    print(f"You have chosen a {size.upper()} pizza ")

    if size == "s":
        bill = 15
    elif size == "m":
        bill = 20
    elif size == "l":
        bill = 25
    else:
        print("Please choose a size")
    pepperoni = input("Do you want pepperoni in your pizza? Y or N").lower()
    if pepperoni == "y":
        bill += 2
    extra_cheese = input("Do you want cheese? Y or N:").lower().strip()
    if extra_cheese == "y":
            bill += 1

    print(f"Your final bill is ${bill}")

    ask_again = input("\nWould you like to order another pizza? Y or N:").lower()
    if ask_again != "y":
        print("Thank you for visiting")
        break
