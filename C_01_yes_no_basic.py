want_instructions =input("do you want instruction").lower()

# check the user says yes / no
if want_instructions == "yes" or want_instructions == "y":
    print("you said yes")
elif want_instructions == "no" or want_instructions == "no":
    print("you said no")
else:
    print("please enter yes / no")

