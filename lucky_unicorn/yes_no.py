# Yes/no checker
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
