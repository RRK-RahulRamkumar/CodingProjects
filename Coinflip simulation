# Functions used to print

def coin_head():
    print("""
    1       1
    1       1
    111111111
    1       1
    1       1
""")


def coin_tail():
    print("""
    1111111
       1   
       1   
       1   
       1   
       1   
""")


def display_output():
    print(f"""
Number of outcomes: {number_of_outcomes}
Number of heads: {number_of_heads}
Number of tails: {number_of_tails}
""")

# Variables

import random

number_of_outcomes = 0
number_of_heads = 0
number_of_tails = 0
continue_flip = True

# Main Program

while continue_flip:
    random_number = random.randrange(1, 3)
    user_input = input("Flip the coin? Yes(Y) No(N): ").upper()

    if user_input == "Y":
        print(random_number)
        if random_number == 1:
            number_of_heads = number_of_heads + 1
            coin_head()
        else:
            number_of_tails = number_of_tails + 1
            coin_tail()
        number_of_outcomes = number_of_outcomes + 1

    elif user_input == "N":
        continue_flip = False
        display_output()
    else:
        print("Program error.")
