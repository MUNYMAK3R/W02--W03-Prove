# Function: Continue to prompt the user if they want to keep playing.
def continue_playing():
    option2 = input("Thanks for playing! Continue with another mad lib? ")
    while option2 !=  "Yes" and option2 != "yes" and option2 != "Y" and option2 != "y" and option2 != "No" and option2 != "no" and option2 != "N" and option2 != "n":
        option2 = input("Please enter a valid option: ")
    if option2 == "Yes" or option2 == "yes" or option2 == "Y" or option2 == "y":
        print("Please select which mad lib theme you would like to fill out:\n")
        option3 = input("The options are School, Work, or Home: ")
        if option3 == "School" or "school":
            school_mad_lib()
        elif option3 == "Work" or "work":
            work_mad_lib()
        elif option3 == "Home" or "home":
            home_mad_lib()
    else:
        print("Thank you for playing!")

# Function: The school mad lib option.
def school_mad_lib():
    print ("\n")
    print("Welcome to the School Mad Lib!\n")
    verb1 = input("Please enter a verb: ")
    verb2 = input("Please enter a second verb ending with 'ing': ")
    adj1 = input("Please enter a adjective: ")
    adj2 = input("Please enter a second adjective: ")
    print("\n")
    print("Oh no you are late for class! You qucikly " + verb1 + " your backpack and rush to class!\n")
    print("You are " + verb2 + " as you " + adj1 + " rush to class!\n")
    print("Your teacher notices that you have rushed in and sat down. She asks 'Why are you late?' You " + adj2 + " anwser 'I swear it will not happen again!'\n")
    continue_playing()

# Function: The work mad lib option.
def work_mad_lib():
    print ("\n")
    print("Welcome to the Work Mad Lib!\n")
    verb1 = input("Please enter a verb: ")
    verb2 = input("Please enter a second verb: ")
    adj1 = input("Please enter a adjective: ")
    adj2 = input("Please enter a second adjective: ")
    print("\n")
    print("You are in a boring meeting. Ted leans over to you and asks 'Hey do you wanna skip this meeting and " + verb1 + "?'")
    print("You answer 'Yes Please!' You and Ted leave the meeting and " + verb2 + " down the stairs.")
    print("Ted looks " + adj1 + " as both of you prepare to " + verb1)
    print("You both " + verb1 + adj2 + " and have a great time! As you are done, he exclaims 'This was the best idea we have had in a long time!'\n")
    continue_playing()

# Function: The home mad lib option.
def home_mad_lib():
    print ("\n")
    print("Welcome to the Home Mad Lib!\n")
    verb1 = input("Please enter a verb: ")
    verb2 = input("Please enter a second verb: ")
    adj1 = input("Please enter a adjective: ")
    adj2 = input("Please enter a second adjective: ")
    print("\n")
    print("You wake up to your best friend ringing the doorbell. You " + verb1 + " down the stairs and " + adj1 + " answer the door.")
    print("Your friend asks 'Hey would you like to " + verb2 + " today?'")
    print("You answer 'Yes please!' You both " + adj2 + " rush out the door and have a great time!\n")
    continue_playing()

# The introduction sentance to prompt the user for a specific mad lib theme to fill out. 
print ("Welcome to my first Python Project using Mad Lib!\n")
print ("Please select which mad lib theme you would like to fill out.")
option = input("The options are School, Home, or Work: ")

# Continue to ask user for input that is "School", "school", "Work", 'work", "Home", or "home" and then run the inputted mad lib.
while option !=  "School" and option != "Home" and option != "Work" and option != "school" and option != "home" and option != "work":
    option = input("Please enter a valid theme: ") 

if option == "School" or option =="school":
    school_mad_lib()
elif option == "Work" or option == "work":
    work_mad_lib()
elif option == "Home" or option == "home": 
    home_mad_lib()


