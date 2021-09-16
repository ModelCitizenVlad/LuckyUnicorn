# Pre-script Things
import random
loop_continue = "true"

# functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "y" or response == "yes":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please input yes or no")

def num_check(question, low, high):
    error = "Please input a number between {} and {}".format(low, high)
    question = "How much money would you like to input?"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low < response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

balance = 0
# Instructions
instructions = yes_no("Have you played before?")
# Add the instructions here when you have actually made the game you twat
if instructions == "no":
    print("*** How to play ***")
    print()
    print("Start by inputting a number as your balance. Then you will be randomly generated a token.")
    print("If the token is a Unicorn, you will gain $4")
    print("If the token is a Horse or a Zebra, you will loose $0.5")
    print("If the token is a Donkey, you will loose $1")
    print("You cannot play with less than $1")
    print()
    print("***             ***")

balance = num_check("How much do you want to play with?", 1, 10)
print("Starting Balance: ${:.2f}".format(balance))

# Token Generator
while loop_continue == "true" and balance >= 1:
    chosen = random.randint(1, 100)
    if 1 <= chosen <= 5:
        token = "Unicorn"
        balance += 4
    elif 6 <= chosen <= 36:
        token = "Donkey"
        balance -= 1
    else:
        if chosen % 2 == 0:
            token = "Horse"
            balance -= 0.5
        else:
            token = "Zebra"
            balance -= 0.5
    print("You got a {}. Your balance is {:.2f}".format(token,balance))
# Continues the loop (or doesn't)
    if balance >= 1:
        replay = input("Would you like to play again?").strip().lower()
        if replay == "yes" or replay == "y":
            loop_continue = "true"
        elif replay == "no" or replay == "n":
            loop_continue = "false"
            print("Game over!")
            print("Exiting game with ${}".format(balance))
        else:
            print("Please input yes or no")
    else:
        loop_continue = "false"
        print("*** Out of money! ***")
        print("  *** You loose ***")
