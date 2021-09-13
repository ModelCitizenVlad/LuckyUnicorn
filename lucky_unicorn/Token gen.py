import random

def token_gen(question):
    STARTING_BALANCE = question

    for i in range(0, 500):
        chosen = random.randint(1, 100)

    if 1 <= chosen <= 5:
        chosen = "Unicorn"
        balance += 4
    elif 6 <= chosen <= 36:
        chosen = "Donkey"
        balance -= 1
    else:
        if chosen % 2 == 0:
            chosen = "Horse"
        else:
            chosen = "Zebra"
        balance -= 0.5

# Output
print()
print("Token: {}".format(chosen))
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))

STARTING_BALANCE = int(input("Gimme money"))
token_gen(STARTING_BALANCE)
