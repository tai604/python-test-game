###### IMPORTING RANDOM AND TIME & DEFINING VARIABLES ######

import random
import time


############# BASIC VARIABLES 
i = 0
Player1Points = 0
Player2Points = 0
Player1Tiebreaker = 0
Player2Tiebreaker = 0
Winner_Points = 0

### This Sets logged in to false, and then makes sure the username and password is correct before allowing them to continue ###
## 

logged_in1 = False
logged_in2 = False
while logged_in1 == False:
    username = input('What is your username? ')
    password = input('What is your password? ')
    if username == 'User1' or username == 'User2' or username == 'User3' or username == 'User4' or username == 'User5':
        if password == 'password':
            print('Welcome, ',username,' you have been successfully logged in.')
            logged_in1 = True
            user1 = username
        else:
            print('Incorrect password, try again')  
    else:
        print('Incorrect username, try again')

while logged_in2 == False:
    username = input('What is your username? ')
    password = input('What is your password? ')
    if username == 'User1' or username == 'User2' or username == 'User3' or username == 'User4' or username == 'User5':
        if password == 'password':
            print('Welcome, ',username,' you have been successfully logged in.')
            logged_in2 = True
            user2 = username
        else:
            print('Incorrect password, try again')  
    else:
        print('Incorrect username, try again')


###### DEFINING ROLL ######

### Makes the dice roll for the player and works out the total for that roll ###

def roll():

    points = 0

    Point1 = random.randint(1,6)  # Selects A random Number Using the import random module

    Point2 = random.randint(1,6)  # Selects A random Number Using the import random module

    Pointtotal = Point1 + Point2  # Adds The Point1 and Point2 Score Togther and makes a total

    points = points + Pointtotal

    if Pointtotal % 2 == 0:
        points = points + 10

    else:
        points = points - 5

    if Point1 == Point2:
        Point3 = random.randint(1,6)
        points = points +Point3

    return(points)

###### DICE ROLL ######

### This rolls the dice 5 times for the players, and then adds up the total. If the scores are equal, it starts a tie breaker and determines the winner off that ###


print("             _______      ")
print("           /\       \     ")
print("          /()\   ()  \    ")
print("         /    \_______\   ")
print("         \    /()     /   ")
print("          \()/   ()  /    ")
print("           \/_____()/     ")
print("     ")
print("    Type Role To Get Started  ")
print(" The Game Will Role For Both User's  ")
print("") 


play = input('User@Dice ')
print("")
for i in range(1,5):
    Player1Points += roll()
    print('',user1, 'You Have Rolled A',Player1Points,'')
    time.sleep(1)
    Player2Points += roll()
    print('',user2, 'You Have Rolled A',Player2Points,'')
    time.sleep(1)

    if Player1Points == Player2Points:
    while Player1Tiebreaker == Player2Tiebreaker:


        Player1Tiebreaker = random.randint(1,6)
        Player2Tiebreaker = random.randint(1,6)

    if Player1Tiebreaker > Player2Tiebreaker:
        Player2Points = 0
    elif Player2Tiebreaker > Player1Tiebreaker:
        Player1Points = 0

###### WORKING OUT THE WINNER ######

### This checks which score is bigger, then creates a tuple for my leaderboard code###

if Player1Points>Player2Points:
    Winner_Points = Player1Points
    winner_User = user1
    winner = (Winner_Points, user1)
elif Player2Points>Player1Points:
    Winner_Points = Player2Points
    winner = (Winner_Points, user2)
    winner_User = user2

print('Well done, ', winner_User,' you won with ',Winner_Points,' Points')

###### CODE TO UPLOAD ALL SCORES TO A FILE ######

## IN Progress




