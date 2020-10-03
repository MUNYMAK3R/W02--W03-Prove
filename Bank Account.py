# Class: The class for the bank account.
class bank_account:
    # Set the user balance to 0.
    def __init__ (user):
        user.balance = 0
   
    # Deposit amount the user inputs.
    def deposit(user):
        print("\n")
        amount = float(input("Enter an amount to be deposited: "))
        user.balance += amount
        print("You deposited: $" , round(amount, 2) , ".\n")
        main_menu()

    # Withdraw the amount the user inputs.
    def withdrawl(user):
        amount = float(input("Enter an amount to withdraw: "))
        print("\n")
        if user.balance > 0 and user.balance - amount > 0:
            user.balance -= amount
            print("You withdrew: $", round(amount, 2) , ".")
        else:
            print("Unable to withdraw. The balance would be below 0. Please add funds before withdrawing.\n")
            main_menu()
        main_menu()
    
    # Display the user's current bank account.
    def display_balance(user):
        print ("\n")
        print("Your available balance is $" , round(user.balance, 2) , ".\n" )
        main_menu()    

# Function: The main menu to navigate what the user wants to do with their account. 
def main_menu():
    print("Please choose what you would like to do with your account.")
    print("[1]- Deposit")
    print("[2]- Withdrawl")
    print("[3]- Display balance")
    print("[4]- Exit")
    option = input("Enter number: ")
    while option != "1" and option != "2" and option != "3" and option != "4":
        option = input("Please enter a valid option: ")
    if option == "1":
        user1.deposit()
    elif option == "2":
        user1.withdrawl()
    elif option == "3":
        user1.display_balance()
    elif option == "4":
        exit

# Initialize the current user's bank account class.
user1 = bank_account()

# The main driver for the program.
print("Welcome to your own personal bank!")
main_menu()