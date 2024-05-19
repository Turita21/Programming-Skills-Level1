"""5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
It must have a login and validate the data; after the third failed attempt, it should be locked.
The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
The user must choose if they want to check an additional piece of luggage into the hold.
Hand luggage is free of charge.
The user must purchase both the outbound and return tickets.
The user can choose their preferred meal: Regular, Vegetarian, Kosher.
The program must collect the following data: Name, country of origin, passport, and destination country.
Upon completing the process, the system will display everything the user has previously chosen along with their information. 
The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.
"""
import random
import datetime
def create_user():
    print("\n\n\tYou are going to create a new user, please fill the next information\n")
    name = input("Name: ")
    lastname = input( "Lastname: ")
    mail = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    count = 0
    while password !=  confirm_password:
        print("The passwords don't match, please try again")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")
        count += 1 
        if count == 3:
            print("You have tried 3 times, the system is shutting down")  
            break
    listData = [name, lastname, mail, password]
    return listData

def login(listData):
    print("-------------------------------------------------------------------------")
    print("\t\nWelcome to Turkish Airlines, please login to proceed\n")
    mail = input("Email: ")
    password = input("Password: ")
    count = 0
    while mail != listData[2] or password != listData[3]:
        print("The email or password is incorrect, please try again")
        mail = input("Email: ")
        password  = input("Password: ")
        count += 1
        if count == 3:
            print("You have tried 3 times, the system is locked out.")  
            break
    message = "\nYou have succesfully login."
    return message

def origin_country():
    print("-------------------------------------------------------------------------")
    origin = input("\t\t\t\t\tPlease choose your origin country: ")
    return origin

def destination_country():
    print("-------------------------------------------------------------------------")
    destination = input("\t\t\t\t\tPlease choose your destination country: ")
    return destination

def dates():
    print( "-------------------------------------------------------------------------")
    print("\t\t\t\t\tPlease choose the dates for your trip: ")
    choice =  input("Do you want to choose the dates? (y/n): ").lower()
    if choice == "y":
        date1_str = input("\nDepart Date (mm/dd/yy): ")
        date2_str = input("\nReturn Date (mm/dd/yy): ")
        date1 = datetime.datetime.strptime(date1_str, "%m/%d/%y")
        date2 = datetime.datetime.strptime(date2_str, "%m/%dd/%y")
    elif choice == "n":
        today = datetime.datetime.now()
        year_later = today + datetime.timedelta(days=365)
        date1 = today + datetime.timedelta(seconds=random.randint(0, int((year_later - today).total_seconds())))
        date2 = date1 + datetime.timedelta(seconds=random.randint(0, int((year_later - date1).total_seconds())))
    else:
        return  "Invalid input"
    return date1, date2

def flight_class():
    print("-------------------------------------------------------------------------")
    print("\t\t\t\t\tPlease choose your flight class: ")
    print("\t\t\t\t\t1. Economy Class")
    print("\t\t\t\t\t2. First Class")
    choice =  int(input("Enter your choice: "))
    if choice == 1:
        return "Economy Class"
    elif choice == 2:
        return  "First Class"
    else:
        return "Invalid input"


def luggage():
    print("-------------------------------------------------------------------------")
    print("Please choose the number of luggage you want to bring. Remember that you ticket  ")
    print("only cover one luggage of 23 kg and a hand luggage. So you have to pay for the extra luggage.")
    extra = input("\t\t\t\t\tDo you want to bring extra luggage? (y/n): ").lower()
    if extra == "y":
        choice =  int(input("\t\t\t\t\tEnter 1 to bring one additional luggage and 2 to bring two additional luggage: "))
        if choice == 1:
            price = 100
        elif choice == 2:
            price = 200
        else:
            print("Invalid input")
    elif extra == "n":
        price = 0
    return price

def meal():
    print("-------------------------------------------------------------------------")
    print("Please choose the meal you want to have during your flight. ")
    print("Remember that your ticket includes one meal.")
    print("\t\t 1- Regular")
    print("\t\t 2- Vegetarian")
    print("\t\t 3- Kosher")
    option =  int(input("\t\t\t\t\tEnter your choice: "))
    if option == 1:
        meal = "Regular"
    elif option == 2:
        meal = "Vegetarian"
    elif option == 3:
        meal =  "Kosher"
    else:
        print("Invalid choice. Please Try again.")
    return meal

def personal_data():
    pass







depart_date, return_date = dates()
print(f"Depart Date (mm/dd/yy): {depart_date.strftime('%m/%d/%Y')}")
print(f"Return Date (mm/dd/yy): {return_date.strftime('%m/%d/%Y')}")











