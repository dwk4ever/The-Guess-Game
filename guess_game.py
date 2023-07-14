#Importing random module
import random
#correct guessed number

#Guess game level select instructions
user_level = int(input("***Choose difficulty level*** \n 1.Easy(1-10) \n 2.Medium(1-100) \n 3.Hard(1-1000)\n\n\n provide level:"))
level = 0
if user_level == 1:
    level = 20

elif user_level == 2:
    level = 100

elif user_level == 3:
    level = 1000
else:
    print("Invalid input")
    exit(1)

guess_number = random.randint(1, level)

#user chances to guess thhe correct number based on level selected
user_input = 0
chances = 0
max_chances = {1:5,2:10,3:100}
if user_level == 1:
    level = 20

elif user_level == 2:
    level = 100

elif user_level == 3:
    level = 1000
while chances < max_chances[user_level]:
    
 

#collecting user input
    user_input = int(input(f"Enter your guessed number(1-{level}): "))
    if user_input == guess_number:
        print(f"Congrats! You guessed the correct number and you used {chances} chances!")
        break
    elif user_input > level:
        print("You guessed out of range!")
    elif user_input < guess_number:
        print("Your guess is too low!")
    elif user_input > guess_number:
        print("Your guess is too high!")
     
    chances += 1
   
    if chances == max_chances[user_level]:
     print("Game Over!!!, you have run out of chances!")
    
print("Thanks for playing!")
