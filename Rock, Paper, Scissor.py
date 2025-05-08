import random

# Declaring Variables
# elements = ["rock", "paper", "scissors"]
# userInput = input("Choose one between rock, paper and scissors: ")
# machineChoice = random.choice(elements)
# cont = input("wanna continue?(y/n) ")

# print("You chose {}" .format(userInput))
# print("I chose {}" .format(machineChoice))

while True:
    
    #Declaring variables inside the loop
    elements = ["rock", "paper", "scissors"]
    userInput = input("Choose one between rock, paper and scissors: ")

    if userInput not in elements:
        print("I didn't understand, make sure you chose a valid")
        continue

    machineChoice = random.choice(elements)

    print("You chose {}" .format(userInput))
    print("I chose {}" .format(machineChoice))

    if userInput == "rock" and machineChoice == "rock":
        print("Looks like we have a tie!")
    if userInput == "rock" and machineChoice == "paper":
        print("I won!")
    if userInput == "rock" and machineChoice == "scissors":
        print("You won!")
    if userInput == "paper" and machineChoice == "rock":
        print("You won!")
    if userInput == "paper" and machineChoice == "paper":
        print("Looks like we have a tie!")
    if userInput == "paper" and machineChoice == "scissors":
        print("I won!")
    if userInput == "scissors" and machineChoice == "paper":
        print("You won!")
    if userInput == "scissors" and machineChoice == "scissors":
        print("Looks like we have a tie")
    if userInput == "scissors" and machineChoice == "rock":
        print("I won!")
    cont = input("wanna continue?(y/n) ")
    if cont != "y":
        break