def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

while True:
    want_instructions = yes_no("Do you want to read the intructions? ")
    print(f"you chose {want_instructions}\n")