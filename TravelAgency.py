"""2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

Clue: You could consider the user's budget"""

print("WELCOME TO THE TRAVEL AGENCY")
print("----------------------------------------")


def user_data():
    username = input("\nPlease enter your name: ")
    print(f'\nWelcome {username}, to improve your experience fillout the next data required')
    budget = input("Please enter your budget so we can offer the best choices for you: ")
    return int(budget)

def winter(user):
    print("\nIn winter we have two incredible choices for you")
    traveling_winter = 100
    activities = input("\nDo you want to go skiing or take a tour?: (skiing/tour)").lower()        
    if activities == "skiing":
        message = '\nGreat choice! Go Skiing in ANDORRA. This will cost you 100$'
    elif activities == "tour":
        message = "\nExcellent choice! Take a tour in SWITZERLAND. This will cost you 100$"
    else:
       message = "\nInvalid option. Please try again."

    saving = user - traveling_winter
    if saving > 0:
        money = f"\nYou are saving {saving} with this amazing trip. "
    else:
        money = "\nYou have the total money for this trip"
    return message + money

def summer(user):
    print("\nIn Summer we have two incredible choices for you")
    traveling_summer = 400
    activities =input("\nDo you want to do extreme sports or activities on the beaches?: (sports/beaches) ").lower()
    if activities == "sports":
        message = "\nWhat a wonderfull chice! We offer hiiking and extreme sports in SPAIN!!! "
    elif activities == "beaches":
        message = "\nBeach lovers unite! We offer all kind of activities on the beaches from PORTUGAL"
    else:
        message = "\nInvalid activity. Please type 'Sports' or 'Beaches'. Try Again."
    
    saving = user - traveling_summer
    if saving > 0:
        money = f"\nYou are saving {saving} with this amazing trip. "
    else:
        money = "\nYou have the total money for this trip"
    return message + money
    
def spring(user):
    print("\nSpring is here, but it's also hot. So let's make your vacations the best we can do ")
    traveling_spring = 300
    activities = input("\nThis season we have options to play sports or go on a tour, which one do you prefer?: (sports/tour) ").lower()
    if activities == "sports":
        message = "\nWhat a wonderfull chice! We offer hiiking and extreme sports in FRANCE!!! "
    elif activities == "tour":
        message = "\nCultural and historical tours in ITALY are very popular at this season. Have and excellent trip."
    else:
        message = "\nInvalid activity. Please type 'Sports' or 'Tour'. Try Again."
    saving = user - traveling_spring
    if saving > 0:
        money =f"\nYou are saving {saving} with this amazing trip. "
    else:
        money = "\nYou have the total money for this trip"
    return message + money

def autumn(user):
    print("\nAutumn is coming soon. Let's planifique an incredible trip to enjoy the maximun of this season.")
    traveling_autumn = 200
    activities = input("\nThis season we have options to play sports or do cultural activities, which one do you prefer?: (sports/activities) ").lower()
    if activities == "sports":
        message = "\nWhat a wonderfull chice! We offer hiiking and extreme sports in BELGIUM!!! "
    elif activities == "tour":
        message = "\nCultural and historical activities in AUSTRIA are very popular at this season. Have and excellent trip."
    else:
        message = "\nInvalid activity. Please type 'Sports' or 'Tour'. Try Again."

    saving = user - traveling_autumn
    if saving > 0:
        money = f"You are saving {saving} with this amazing trip. "
    else:
        money = "You have the total money for this trip"
    return message + money

user = user_data()
trip = False
while trip != True:
    season = input("\nDo you want any season in particular ? Answer (Y/n): ").upper()
    if season == "Y":
        season = input("\nEnter the season you prefer (winter-autumn-spring-summer): ").lower()
        if season == "winter":
            if user >= 100:
                print(winter(user))
                print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
                trip = True
            else:
                print("We don't have options that fit with your budget. Try with another season")
                trip = False
        elif season == "autumn":
            if user >= 200:
                print(autumn(user))
                print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
                trip = True
            else:
                print("We don't have options that fit with your budget. Try with another season: ")
                trip = False
        elif season == "spring":
            if user >= 300:
                print(spring(user))
                print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
                trip = True
            else:
                print("We don't have options that fit with your budget. Try with another season: ")
                trip = False
        elif season == "summer":
            if user > 400:
                print(summer(user))
                print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
                trip = True
            else:
                print("We don't have options that fit with your budget. Try with another season: ")
                trip = False
    elif season == "N":
        trip = True
        print("Nice! We are going to give you the best choice acording your budget. If you want to see other choices try changing the budget")
        if user >= 100 and user < 200:
            print(winter(user))
            print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
        elif user >= 200 and user < 300:
            print(autumn(user))
            print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
        elif user >= 300 and user < 400:
            print(spring(user))
            print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
        elif user >= 400:
            print(summer(user))
            print("Thank you for ussing our travel agency. We spect that you have an wonderfull trip.")
        else:
            print("We don't have options that fit with your budget. Try with another season: ")



