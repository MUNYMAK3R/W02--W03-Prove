#DISCLAMER: all of the information provided is current as of October 3, 2020. Rates are subject to change. 

#Function: This is the main menu of the program to select a currency to be converted.
def main_menu():
    print("The currencies available to be converted are:")
    print("[1] - USD")
    print("[2] - Euro")
    print("[3] - Japanese Yen")
    currency = input("Please select a starting currency that you would like to convert: ")
    while currency !=  "1" and currency != "2" and currency != "3":
        currency = input("Please enter a valid option: ")
    if currency == "1":
        usd_conv()
    elif currency == "2":
        euro_conv()
    elif currency == "3":
        yen_conv()

#Function: This will prompt the user to rerun the currency program. 
def rerun():
    print("\n")
    option = input("Would you like to convert another currency? Y/N: ")
    while option != "Y" and option != "N" and option != "y" and option != "n":
        option = input("Please enter a vaild option: ")
    if option == "Y" or option == "y":
        main_menu()
    elif option == "N" or option == "N": 
        exit
        
#Function: This will convert the USD into the Euro, Japanese Yen, British Pound, and Australian Dollar.
def usd_conv():
    amount = float(input("Enter the amount of USD that you would like to be converted: "))
    print("\n")
    #Euro conversion
    amount *= .853554
    print("Euro: " , round(amount, 2))
    amount /= .853554
    #Yen conversion
    amount *= 105.319
    print("Japanese Yen: " , round(amount, 2))
    amount /= 105.319
    #British Pound conversion
    amount *= .773096
    print("British Pound: " , round(amount, 2))
    amount /= .773096
    #Australian Dollar
    amount *= 1.39643
    print("Australian Dollar: " , round(amount, 2))
    amount /= 1.39643
    rerun()

def euro_conv():
    amount = float(input("Enter the amount of Euro that you would like to be converted: "))
    print("\n")
    #USD conversion
    amount *= 1.17155
    print("USD: " , round(amount, 2))
    amount /= 1.17155
    #Yen conversion
    amount *= 123.394
    print("Japanese Yen: " , round(amount, 2))
    amount /= 123.394
    #British Pound conversion
    amount *= .905763
    print("British Pound: " , round(amount, 2))
    amount /= .905763
    #Australian Dollar
    amount *= 1.63610
    print("Australian Dollar: " , round(amount, 2))
    amount /= 1.63610
    rerun()

def yen_conv():
    amount = float(input("Enter the amount of Yen that you would like to be converted: "))
    print("\n")
    #Euro conversion
    amount *=  0.00810415
    print("Euro: " , round(amount, 2))
    amount /=  0.00810415
    #USD conversion
    amount *= .00949446
    print("USD: " , round(amount, 2))
    amount /= .00949446
    #British Pound conversion
    amount *= .00734044
    print("British Pound: " , round(amount, 2))
    amount /= .00734044
    #Australian Dollar
    amount *= .0132592
    print("Australian Dollar: " , round(amount, 2))
    amount /= .0132592
    rerun()

#The main driver for the program.
print("Hi! Welcome the Currency Converter!")
main_menu()
