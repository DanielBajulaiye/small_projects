# import math
# import random
# # tasks = []
# #
# # def show_menu():
# #     print("\n---To-DO List Menu ---")
# #     print("1. Add  Tasks")
# #     print("2. View Tasks")
# #     print("4. Remove Tasks")
# #     print("5. Exit")
# #
# # def add_task():
# #     task_name = input("Enter task name")
# #     tasks.append({"task": task_name, "completed": False})
# #     print(f'Task "{task_name}" added successfully!')
# #
# # def view_tasks():
# #     if not tasks:
# #         print("No tasks found!")
# #         return
# #     print("\nYour TO-DO List:")
# #     for i, task in enumerate(tasks,1):
# #         status = "done" if task ["completed"] else "x"
# #         print(f"{i}. [{status}] {task['task']}")
# #
# # def mark_completed():
# #     view_tasks()
# #     try:
# #         task_num = int(input("Enter task number to mark as completed ")) - 1
# #         if 0 <= task_num < len(tasks):
# #             removed_task = tasks.pop(task_num)
# #             print(f'Task "{removed_task["task"]}" removed!')
# #         else:
# #             print("Invalid task number.")
# #     except ValueError:
# #         print("Please enter a valid number.")
# #
# # while True:
# #     show_menu()
# #     choice = input("Choose an option (1-5):")
# #
# #     if choice == "1":
# #         add_task()
# #     elif choice == "2":
# #         view_tasks()
# #     elif choice == "3":
# #         mark_completed()
# #     elif choice == "4":
# #         remove_task()
# #     elif choice == "5":
# #         print("Goodbye!")
# #         break
# #     else:
# #         print("Invalid option. Please enter a number 1 and 5.")
#
# # random_numbers = random.randint(1, 100)
# # guess = int(input("Guess a number:"))
# # print(f"Your guess is {guess}")
# #
# # print(f"The computer's guess is {random_numbers}")
# #
# # if guess == random_numbers:
# #     print("Correct guess!")
# # elif guess < random_numbers:
# #     print("Too low!")
# # elif guess < random_numbers:
# #     print("Too high!")
# # else:
# #     print("Invalid Input")
#
# def add(x,y):
#     return x + y
#
# def subtract(x,y):
#     return x - y
#
# def divide(x,y):
#     if y == 0:
#         return "Undefined"
#     return x / y
#
# def multiply( x,y):
#     return x * y
#
# prompt = ("Welcome to the calculator")
#
# num1 = float(input("Enter first number"))
# num2 = float(input("Enter second number"))
#
# print("1. Add")
# print("2. Subtract")
# print("3. Multiple")
# print("4. Divide")
#
# choice = input("Enter a number : (1/2/3/4) ")
#
# if choice == "1":
#     print (num1, "+", num2 , "=",add(num1,num2))
#
# elif choice == "2":
#     print(num1, "-", num2, "=", subtract(num1, num2))
#
# elif choice == "3":
#     print(num1, "*", num2, "=", multiply(num1, num2))
#
# elif choice == "4":
#     print (num1, "/", num2 , "=",divide(num1,num2))
#
# else:
#     print("Invalid digit my boy!!")
#
#
import random

game_input = ["rock","paper", "scissors"]

users_choice = input("Pick one (Rock, Paper, Scissors):").lower().strip()

computer_choice = random.choice(game_input)

print(f"You picked:{users_choice}")

print(f"Computer picked:{computer_choice}")

if users_choice == "rock" and computer_choice == "paper":
    print("you lose!")
elif users_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif users_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif users_choice == "paper" and computer_choice == "scissors":
    print("You lose!")
elif users_choice == "scissors" and computer_choice == "rock":
    print("you lose")
elif users_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif users_choice == computer_choice:
    print("You draw")
else:
    print("Invalid")