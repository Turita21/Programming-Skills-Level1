"""4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

Login; it should be locked after the third failed attempt.
The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu."""
import datetime

def user_singup():
    user_name = input("Enter your name: ")
    mail = input("Enter your email: ")
    password = input("Create a password: ")
    confirmation = input("Confirm your password: ")
    while password != confirmation:
        print("Sorry the passwords doesnt match. Try again")
        password = input("Create a password: ")
        confirmation = input("Confirm your password: ")
    dictionary = {"Name":user_name, "Mail address" : mail, "Password":password}
    return dictionary

def login(dictionary):
    login_attemps = 0
    while login_attemps < 3:
        mail_address = input("Enter your mail: ")
        password = input("Enter your password: ")
        if (mail_address == dictionary["Mail address"] and password == dictionary["Password"]):
            message = "\n\tYou have succesfully logged in."
            break
        else:
            login_attemps +=1
            left = 3 - login_attemps
            if login_attemps < 3:
                print(f"\n\tThe information is not correct. Please try again. You have {left} attemps. Try again")
            else:
                message = "\n\tYour account has been blocked due to too many incorrect attempts.\n\tPlease contact our customer service department."
    return message

def menu():
    print("\nWe are delighted to have our hotels all over the world.")
    print("\nPlease choose an option from below to continue: ")
    print("1 -Search by destination.\n")
    print("2 -Search by date.\n")
    print("3 -Make a reservation.\n")
    print("4 -View my reserved rooms.\n")
    print("5 -Log out.\n")
    choice=input("Number of your choice :")
    return int(choice)

def destination():
    print("We count with hotels in these destinations:\n")
    print("\t 1- Spain \n")
    print("\t 2- France \n")
    print("\t 3- Portugal \n")
    print("\t 4- Italy \n")
    print("\t 5- Germany \n")
    num_country = int(input("Choose the number of the desired country: "))
    if num_country == 1: 
        country = "Spain"
    elif num_country == 2:
        country = "France"
    elif num_country == 3:
        country = "Portugal"
    elif num_country == 4:
        country = "Italy"
    elif num_country == 5:
        country = "Germany"
    else:
        print("That number is not asssigned to any country. Please try again")
    print(f"\nYou choose {country}\n")
    if country == "Spain":
        print("\nIn this destination we have hotels in: ")
        print("\t 1- Madrid\n")
        print("\t 2- Barcelona\n")
        print("\t 3- Valencia\n")
        num_city = int(input("\nPlease enter the number of your city of you preference: "))
        if num_city == 1:
            city = "Madrid"
            return "\nYour destination is " + city + " " + country
        elif num_city == 2:
            city = "Barcelona"
            return "\nYour destination is " + city + " " + country 
        elif num_city == 3:
            city = "Valencia"
            return "\nYour destination is " + city + " " + country 

def hotels():
    print("\nSelect the kind of room of your preference: \n")
    print("\t 1- Single Room\n")
    print("\t 2- Double Room\n")
    print("\t 3- Group Room\n")
    print("\t 4- VIP Suite\n")
    print("\t 5- Luxury Suite\n")
    number_of_rooms = int(input("How many rooms do you  want? "))
    
    n = 0
    list_room = []
    while n < number_of_rooms: 
        room_type = int(input("\nEnter the number of the room from the list above: "))
        n += 1
        if room_type == 1:
            room = "Single room"
            print(f"\nThe room {n} is a single room.")
        elif room_type == 2:
            room = "Double room"
            print(f"\nThe room {n} is a double room.")
        elif room_type == 3:
            room = "Group room"
            print(f"\nThe room {n} is a Group room.")
        elif room_type == 4:
            room = "VIP Suite"
            print(f"\nThe room {n} is a VIP suite.")
        elif room_type == 5:
            room = "Luxury Suite"
            print(f"\nThe room {n} is a Luxury suite.")
        else:
            print("This option is incorrect, please try again.")
        list_room.append(room)
    return list_room

def reservations():
    date = datetime.datetime.now()
    print("\nPlease enter the day, the month, the year and the hour to make the reservation: \n")
    day =  int(input("\tDay (dd): "))
    month = int(input("\tMonth (mm): "))
    year = int(input("\tYear (yyyy): "))
    hour = input("\tHour [hh]: ")
    if hour > 24:
        print("You have enter an invalid hour. Please try again.\n")
        hour = input("\tHour [hh]: ")
    nights =  int(input("\tNumber of nights: "))

    if day  < date.day or month < date.month or year < date.year:
        date_reservation =  "\nThe date you entered is invalid.Please, enter a valid date."      
    else:
        date_CheckIn_reservation = {"Day": day,
                            "Month": month,
                            "Year": year,
                            "Hour": hour}
        date_CheckOut_reservation ={ "Day": day+nights,
                            "Month": month,
                            "Year": year,
                            "Hour": hour}
        
    return "Your reservation is set to the following datetime " +  str(date_CheckIn_reservation) + " until " + str(date_CheckOut_reservation)
        
def prices(list_room):
    total = 0
    for i in list_room:
        if i == "Single room":
            price_room =  100
        elif i == "Double room":
            price_room = 200
        elif i == "Group room":
            price_room = 350
        elif i == "VIP suite":
            price_room = 450
        elif i == "Luxury suite":
            price_room = 550
        total += price_room
    return total
    
    

print("------------------------------------------------------------------")
print("------------------------ WELCOME TO RH HOTELS---------------------")

print(prices(["VIP suite"]))
# account = input("Do you already have an account ? Y/N: ").lower()
# if account == 'y':
#     d1 = {"Name":"Coral","Mail address":"cori119","Password":"hagro"}
#     user = login(d1)
#     print(user)
# else:
#     print("\t-------------Please sign up.------------")
#     user = user_singup()
#     print("\t--------Account created. Enter your data to login.-------")
#     print(login(user))
