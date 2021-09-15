# Pre-script Things
import random
loop_continue = "true"

# functions


tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 0

# Yes/no
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


# Instructions
instructions = yes_no("Have you played before?")
print("You chose {}".format(instructions))
print()

# Add the instructions here when you have actually made the game you twat
if instructions == "no":
    print("*** How to play ***")
    print()
    print("Placeholder instructions")
    print()

# Num check
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


STARTING_BALANCE = num_check("How much do you want to play with?", 1, 10)

# Token Generator
loop_continue = "true"

while loop_continue == "true":
    def token_gen():
        for i in range(0, 500):
            chosen = random.randint(1, 100)

        if 1 <= chosen <= 5:
            chosen = "Unicorn"
            balance = 4
            return [balance, chosen]
        elif 6 <= chosen <= 36:
            chosen = "Donkey"
            balance = 1
            return [balance, chosen]
        elif chosen % 2 == 0:
            chosen = "Horse"
            balance = 0.5
            return [balance, chosen]
        else:
            chosen = "Zebra"
            balance = 0.5
            return [balance, chosen]

# Continues the loop (or doesn't)
if balance > 0:
    loop_continue = str(input("Would you like to play again?"))
    loop_continue.strip().lower()
    if loop_continue == "yes" or loop_continue == "y" and balance > 0:
        var = loop_continue == "true"
    elif loop_continue == "no" or loop_continue == "n" and balance > 0:
        balance -= tokens[0]
        var = loop_continue == "false"

    else:
        print("Please input yes or no")
else:
    print("*** Out of money! ***")
    print("*** You loose ***")

# The main function (runs the code)
while loop_continue == "true":
    tokens = token_gen()
    print()
    print("Token: {}".format(tokens[1]))
    print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
    print("Current Balance: ${:.2f}".format(balance))
