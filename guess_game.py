#Importing random module
import random
#correct guessed number
guess_number = random.randint(1, 20)

#user has 5 chances to guess thhe correct number
user_input = 0
while user_input < 5:

    print("You have 5 chances to guess")

#collecting user input
    user_input = int(input("Enter your guessed number: "))
    if user_input == guess_number:
        print("Congrats! You guessed the correct number!")
    elif user_input < guess_number:
        print("Your guess is too low!")
    elif user_input > guess_number:
        print("Your guess is too high!")
    else:
        if user_input != guess_number:
            print("Wrong answer, better luck next time!")
user_input += 1