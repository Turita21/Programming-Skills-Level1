"""
1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
The system should also allow comparison between two players. Use the following player profiles:

Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
The program functions as follows: The coach accesses the system and encounters a menu with the following options:

Player Review: By entering the player's jersey number, they can access the player's characteristics.
Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
Identify the fastest player: Displays the player with the most points in speed.
Identify the top goal scorer: Displays the player with the most points in goals.
Identify the player with the most assists: Displays the player with the most points in assists.
Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
The system should also allow returning to the main menu."""



def menu():
    print("\nMANCHESTER UNITED SYSTEM")
    print("------------------------------------------------------")
    print("[1] Player Review")
    print("[2] Compare two Players")
    print("[3] Identify the Fastest Player")
    print("[4] Identify the top Goal Scorer")
    print("[5] Identify the Player with the most Assists")
    print("[6] Identify the player with the highest Passing Accuracy")
    print("[7] Identify the player with the most defensive involvements")
    print("[8] Quit")
    option = input("Enter a number from above to proceed: ")
    if  int(option) <1 and int(option) >8:
        print("Please enter a valid option ")
        option = input("Enter a number from above to proceed: ")
    return  int(option)

def menu_players():
    print("\nPlayers Availables with their jersey number: ")
    print("Bruno Fernandes Jersey [8]")
    print("Rasmus Hojlund Jersey [11]")
    print("Harry Maguire Jersey [5]")
    print("Alejandro Garnacho Jersey [17]")
    print("Mason Mount Jersey [7]")
    return "\n"


def player_review():
    print(menu_players())
    jersey_number = int(input("Enter the jersey number of the player that you want  to review: "))
    for key, values in players.items():
        if values["Jersey Number"] == jersey_number:
            print("Player Name: " + values["Name"])
            print("Goals: " + str(values["Goals"]))
            print("Points in Speed: " + str(values["Points in speed"]))
            print("Points in Assists: " + str(values["Points in assists"]))
            print("Passing Accuracy: " + str(values["Passing accuracy"]))
            print("Defensive Involvements: " + str(values["Defensive involvements"]))
            return  "\n\n"
        else:
            print("Invalid Jersey Number! Please try again.")
    return True

def compare_two_players():
    print(menu_players())
    player1_jersey = int(input("Enter the number jersey of the first player: "))
    player2_jersey = int(input("Enter the number jersey of the second player: "))
    for  key, value in players.items():
        if value["Jersey Number"] == player1_jersey: 
            print("\nPlayer Name: " + value["Name"])
            print("Goals: " + str(value["Goals"]))
            print("Points in Speed: " + str(value["Points in speed"]))
            print("Points in Assists: " + str(value["Points in assists"]))
            print("Passing Accuracy: " + str(value["Passing accuracy"]))
            print("Defensive Involvements: " + str(value["Defensive involvements"]))
            continue
        if  value["Jersey Number"] == player2_jersey:
            print("\nPlayer Name: " + value["Name"])
            print("Goals: " + str(value["Goals"]))
            print("Points in Speed: " + str(value["Points in speed"]))
            print("Points in Assists: " + str(value["Points in assists"]))
            print("Passing Accuracy: " + str(value["Passing accuracy"]))
            print("Defensive Involvements: " + str(value["Defensive involvements"]))
    return "\n"

def fastest_player():
    maximun = 0
    for key, value in players.items():
        if int(value['Points in speed']) > maximun:
            maximun = int(value['Points in speed'])
    for  key, value in players.items():
        if int(value["Points in speed"]) == maximun:
            print("\nThe Fastest Player is: " + value["Name"])
    return "With a points of " + str(maximun) + "\n"

def goal_scorer():
    maximun = 0
    for key, value in players.items():
        if int(value['Goals']) > maximun:
            maximun = int(value['Goals'])
    for  key, value in players.items():
        if int(value["Goals"]) == maximun:
            print("\nThe Top Scorer Player is: " + value["Name"])
    return "With " + str(maximun) + " goals"

def most_Assists():
    maximun = 0
    for key, value in players.items():
        if int(value['Points in assists']) > maximun:
            maximun = int(value['Points in assists'])
    for  key, value in players.items():
        if int(value["Points in assists"]) == maximun:
            print("\nThe Player with the most assists is: " + value["Name"])
    return  "Who has " + str(maximun) + " assits."

def passing_accuracy():
    maximun = 0
    for key, value in players.items():
        if int(value['Passing accuracy']) > maximun:
            maximun = int(value['Passing accuracy'])
    for  key, value in players.items():
        if int(value["Passing accuracy"]) == maximun:
            print("\nThe Player with the best passing accuracy is: " + value["Name"])
    return "Whose passing accuracy is: " + str(maximun)

def defensive_involvements():
    maximun = 0
    for key, value in players.items():
        if int(value['Defensive involvements']) > maximun:
            maximun = int(value['Defensive involvements'])
    for  key, value in players.items():
        if int(value["Defensive involvements"]) == maximun:
            print("\nThe Player with the best defensive involvements is: " + value["Name"])
    return "Whose Defensive Involvement is: " + str(maximun)

player1 = {"Name" : 'Bruno Fernandes', 
           "Goals" : 5, 
           "Points in speed" : 6, 
           "Points in assists" : 9, 
           "Passing accuracy" : 10, 
           "Defensive involvements" : 3,
            "Jersey Number": 8}
player2 = {"Name" : 'Rasmus Hojlund', 
           "Goals" : 12, 
           "Points in speed" : 8, 
           "Points in assists" : 2, 
           "Passing accuracy" : 6, 
           "Defensive involvements" : 2, 
           "Jersey Number": 11}
player3 = {"Name" : 'Harry Maguire', 
           "Goals" : 1, 
           "Points in speed" : 5, 
           "Points in assists" : 1, 
           "Passing accuracy" : 7, 
           "Defensive involvements" : 9, 
           "Jersey Number": 5}
player4 = {"Name" : 'Alejandro Garnacho', 
           "Goals" : 8, 
           "Points in speed" : 7, 
           "Points in assists" : 8, 
           "Passing accuracy" : 6, 
           "Defensive involvements" : 0, 
           "Jersey Number": 17}
player5 = {"Name" : 'Mason Mount', 
           "Goals" : 2, 
           "Points in speed" : 6, 
           "Points in assists" : 4, 
           "Passing accuracy" : 8, 
           "Defensive involvements" : 1, 
           "Jersey Number": 7}

players = {
    "Player 1" : player1,
    "Player 2" : player2,
    "Player 3" : player3,
    "Player 4" : player4,
    "Player 5" : player5
}

def return_menu():
    ctnue = True
    while ctnue == True:
        option = input("\nDo you want to go to the main menu? Please enter any letter to continue or 'q' to quit: ")
        if option.lower() != "q":
            ctnue = True
            main(menu())
        else:
            ctnue = False
            print("\n\nGoodbye!. Thanks for using the Manchester United System. Please come again.\n\n")
            

def main(choice):
    if choice == 1:
        print(player_review())
        return_menu()
    elif choice == 2:
        print(compare_two_players())
        return_menu()
    elif choice == 3:
        print(fastest_player())
        return_menu()
    elif choice == 4:
        print(goal_scorer())
        return_menu()
    elif choice == 5:
        print(most_Assists())
        return_menu()
    elif choice == 6:
        print(passing_accuracy())
        return_menu()
    elif choice == 7:
        print(defensive_involvements())
        return_menu()
    elif choice == 8:
        print("\n\nGoodbye!. Thanks for using the Manchester United System. Please come again.\n\n")
    else:
        print("The number that you enter is not valid. Please try again.")
    
choice = menu()
if choice == 1:
    print(player_review())
    return_menu()
elif choice == 2:
    print(compare_two_players())
    return_menu()
elif choice == 3:
    print(fastest_player())
    return_menu()
elif choice == 4:
    print(goal_scorer())
    return_menu()
elif choice == 5:
    print(most_Assists())
    return_menu()
elif choice == 6:
    print(passing_accuracy())
    return_menu()
elif choice == 7:
    print(defensive_involvements())
    return_menu()
elif choice == 8:
    print("\n\nGoodbye!. Thanks for using the Manchester United System. Please come again.\n\n")