# funtions go here

def yes_no(question):

    # Checks user response to a question is yes / no ***

    while True:

        response = input(question).lower()

        #check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "no":
           return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

Roll the dice and try and win!
    """)


def int_check():
    #checks users enter an interger more than / equal to 13

    error = "please enter an interger more than / equal to 13"

    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want instruction")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print ()
game_goal = int_check()
print(game_goal)
