def num_check(question,low,high):

    # Money input
    error = "Please input a number between {} and {}".format(low,high)

    valid = False
    while not valid:
        try:
            response = int(input("How much money would you like to input?"))
            if 0 < response <= 10:
                print("You are playing with ${}".format(response))
                valid = True
            else:
                print(error)

        except ValueError:
            print(error)

how_much = num_check("How much do you want to play with?", 1,10)
