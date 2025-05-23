import os
import sys
import time
import random

selectionPlayers = ['Virat Kohli','Kusal Mendis','Steve Smith','Jason Holder','Shikhar Dhavan','Dinesh Chandimal','Mohammad Amir','AB de Villiers','Imran Tahir','Thisara Perera','Jos Buttler','Asad Shafiq','Nowan Pradeep','Mitchell Starc','Ish Sodhi']

selectionPlayersSpeed = [128,145,101,99,78,65,95,156,133,107,170,129,106,144,60]

locations = ['Dhaka', 'Karachi', 'Kolkata', 'Chennai', 'New Delhi', 'Mumbai', 'Istanbul', 'Mexico', 'Las Vegas', 'Sydney', 'Moscow', 'Tokyo', 'London', 'Shanghai', 'Beijing', 'Paris', 'Dubai', 'Johannesburg', 'England', 'New York', 'Australia']

entry_fees = [100,200,250,500,1000,2500,5000,10000,25000,50000,75000,100000,200000,250000,500000,1000000,1500000,2000000,2500000,4500000,5000000]

prizes = [200,400,500,1000,2000,5000,10000,20000,50000,100000,150000,200000,400000,500000,1000000,2000000,3000000,4000000,5000000,9000000,10000000]

opponent_cricketers = ['Rohit Sharma', 'MS Dhoni', 'Hardik Pandya', 'Ravindra Jadeja', 'Bhuvneshwar Kumar', 'Jasprit Bumrah', 'Rishabh Pant', 'Suresh Raina', 'David Warner', 'Pat Cummins', 'Glenn Maxwell', 'Aaron Finch', 'Usman Khawaja', 'Nathan Lyon', 'Shaun Marsh', 'Peter Handscomb', 'Babar Azam', 'Fakhar Zaman', 'Sarfaraz Ahmed', 'Shadab Khan', 'Hasan Ali', 'Shaheen Afridi', 'Azhar Ali', 'Haris Sohail', 'Faf du Plessis', 'Quinton de Kock', 'Kagiso Rabada', 'Dale Steyn', 'Lungi Ngidi', 'Andile Phehlukwayo', 'Rassie van der Dussen', 'David Miller', 'Joe Root', 'Eoin Morgan', 'Jonny Bairstow', 'Ben Stokes', 'Jofra Archer', 'Chris Woakes', 'Adil Rashid', 'Moeen Ali', 'Jason Roy', 'Chris Gayle', 'Kieron Pollard', 'Andre Russell', 'Sunil Narine', 'Shai Hope', 'Shimron Hetmyer', 'Nicholas Pooran', 'Oshane Thomas', 'Sheldon Cottrell', 'Kane Williamson', 'Martin Guptill', 'Ross Taylor', 'Tom Latham', 'Colin de Grandhomme', 'Lockie Ferguson', 'Trent Boult', 'Mitchell Santner', 'Tim Southee', 'Angelo Mathews', 'Niroshan Dickwella', 'Lasith Malinga', 'Suranga Lakmal', 'Akila Dananjaya', 'Wanindu Hasaranga', 'Sachin Tendulkar']

cricketer_team_names = ['Thunderbolts', 'Storm Chasers', 'Blazing Stars', 'Cricket Kings', 'PitchMasters', 'Willow Warriors', 'Spin Doctors', 'Fast Lane', 'Boundary Breakers', 'Sixers Squad', 'Fierce Falcons', 'Mighty Mavericks', 'Speed Demons', 'Power Play', 'The Invincibles', 'Cricket Crusaders', 'Batting Brigade', 'Bowling Bandits', 'Fielding Force', 'The Champions', 'Rising Stars','Cricket Renegades', 'The Pioneers', 'Victory Vikings', 'Thunderbirds', 'Whirlwind Warriors', 'Spin Wizards', 'Pace Setters', 'The Gladiators', 'Master Blasters', 'The Mavericks', 'Blazing Bats', 'The Conquerors', 'Cricket Commandos', 'The Thunderers', 'Fierce Fighters', 'Speedsters', 'The Strikers', 'Powerhouse', 'The Blasters', 'Cricket Dynamos', 'The Flame', 'The Blazing Bats', 'The Thunderclap', 'The Whirlwind', 'The Stormers', 'The Lightning Bolts', 'The Hurricane', 'The Tornado', 'The Cyclone', 'The Blaze', 'The Inferno', 'The Fireballs', 'The Scorchers', 'The Heat', 'The Flame Throwers', 'The Spark', 'The Ember', 'The Ignite', 'The Fusion', 'The Pulse', 'The Surge', 'The Wave', 'The Tide', 'The Ripple', 'The Splash', 'The Dasher', 'The Bolt', 'The Flash', 'The Zoom', 'The Zing', 'The Ping', 'The Pong', 'The Bang', 'The Boom', 'The Crash', 'The Smash', 'The Bash', 'The Thrash', 'The Clash', 'The Sting', 'The Sling', 'The Fling', 'The Swing', 'The Sway', 'The Twirl', 'The Spin', 'The Curve', 'The Hook', 'The Slice', 'The Chip', 'The Dip', 'The Dive', 'The Plunge','The Soar', 'The Glide', 'The Slide', 'The Slip', 'The Trip', 'The Leap']

directions = ['North','West','East','South','North East','North West','South East','South West']

userSelectedMembers = []
toss = ['Head','Tail']

if not os.path.exists('User Info.txt') :

    name = input('Enter your name : ')
    Id = input('Set your Id : ')
    password = input('Enter your password : ')

    with open('User Info.txt','w') as ui :
        ui.write(name + '\n' + Id + '\n' + password)

ui = open('User Info.txt','r')
info = ui.read().splitlines()
name = info[0]
Id = info[1]
password = info[2]

iteration = 1

if not os.path.exists('User Team.txt') :
    print(f'\nSo {name}, You are the captain now.\nChoose your team.\n')

    for i in range(10) :

        for selectionplayer in selectionPlayers :
            print(f'{iteration}. {selectionplayer}')
            iteration += 1

        try :

            user_team = int(input('\nEnter the serial number of the name : '))
            selected_player = selectionPlayers[user_team - 1]
            print(f'{selected_player} is selected.')
            selectionPlayers.remove(selected_player)
            iteration = 1
            userSelectedMembers.append(selected_player)

        except Exception as e :
            print(f'Sorry!! Some error occured.\nError : {e}')

    teamName = input('\nYour team is almost ready!\nChoose a name for your team : ')

    with open('User Team.txt','a') as ut :
        ut.write(teamName + '\n' + name + '\n')

        for selectedMember in userSelectedMembers :
            ut.write(selectedMember + '\n')

    rules = '''Here are the rules :-
1. You have to enter a number between 1 to 6.
2. How fast you enter the ball would define the speed of the ball.
3. If the speed of the ball is zero that means that you have tried to hit the ball before it reaches\
you and the ball touches the Wicket and you are out. 
4. If the speed of the ball is greater than 80 that means the ball has already passed and you are out. 
5. If you enter 6, then the feilding player would try to Defence the score.
6. If the speed of the fielding player and the speed of the ball is equal that means the fielding player is able to catch the ball and you are out.
7. If the speed of fielding player is greater than speed of ball then it means that player is able to stop the ball and no runs are scored. 
8. If you enter 4 then the fielding player will again try to Defence the score.
9. If the speed of the fielding player is greater than or equals to the speed of the ball then it mea\
ns that the player is able to stop the ball and no runs are scored.
10. If the entered Run is equal to the entered ball then you are out.
11. During bowling you just have to remember that you have to enter the same Run your opponent is entering so that he is out.
12. You can play your game in some locations. The main aim of this game is TO MAKE MONEY.'''

    print(rules)

if not os.path.exists('User Money.txt') :

    with open('User Money.txt','w') as um :
        um.write('600')

f = open('User Team.txt','r')
info = f.read().splitlines()
userTeamName = info[0]
userTeamPlayers = info[1:]
f.close()

with open('User Money.txt','r') as um :
    money = int(um.read())


def UserInfo() :

    '''Function to display user information, their team details, and categorize them based on their money balance.
    
    The function prints:
    - User's name and ID
    - Team name and team players
    - Money balance
    - Level based on the amount of money
    
    Levels:
    - 'Beginner'    : $0 - $9,999
    - 'Intermediate': $10,001 - $74,999
    - 'Advanced'    : $75,001 - $99,999
    - 'Expert'      : $100,001 - $999,999
    - 'Champion'    : $1,000,000 and above'''
    
    print('\n------------------------------------------')
    print(f'Name : {name}')
    print(f'Id : {Id}')
    print(f'Team Name : {userTeamName}')
    print('Team Players :-\n')

    for player in userTeamPlayers :
        print(player)
        
    with open('User Money.txt','r') as um :
        money = int(um.read())

    print(f'\nMoney : ${money:,}')

    if money >= 0 and money < 10000 :
        level = 'Begginer'

    elif money >= 10001 and money < 75000 :
        level = 'Intermediate'

    elif money >= 75001 and money < 1000000 :
        level = 'Andvanced'

    elif money >= 1000001 and money < 10000000 :
        level = 'Expert'

    else :
        level = 'Champion'

    print(f'Level : {level}')
    print('------------------------------------------')

def StartingMatch(oppTeamName,oppTeam) :

    """Simulates the start of a cricket match by allowing the user to:
    - Select the number of overs for the match.
    - Choose a match location from a list, considering entry fees and prizes.
    - Deduct entry fees from the user's money and update the balance.
    - Display the opponent team and their player attributes.
    - Perform a coin toss to determine which team bats or bowls first.
    
    Parameters:
    oppTeamName (str): Name of the opponent team.
    oppTeam (list): List of players in the opponent team.
    
    Returns:
    str: 'Batting' if the user wins the toss and chooses to bat, 
         'Bowling' if the user wins the toss and chooses to bowl, 
         or 'Bowling' if the opponent wins the toss and chooses to bat.
    
    Notes:
    - The function reads and updates the user's money from a file named 'User Money.txt'.
    - It introduces delays using time.sleep() for a more interactive experience.
    - Uses random selection for the toss and opponent player attributes.
    
    Raises:
    - Exception: If any unexpected error occurs during execution"""
    
    global overs
    global money
    global entryFees

    try :
        desired_over = int(input('How many overs do you want to play?\nEnter here : '))
        overs = desired_over + overs
        print('Where do you want to play your match?')
        print('\n{:<5} {:<12} {:<13} {:<13}\n'.format("S.No","Location","Entry Fees","Prize"))

        for index,location in enumerate(locations) :
            print(f'{index + 1:<5} {location:<12} {entry_fees[index]:<13,} {prizes[index]:<13,}')

        while True :
            desired_location = int(input('\nEnter the serial number of the location where you want to play : '))

            if entry_fees[desired_location - 1] > money :

                print('You do not have enough money to enter and play at this location.Please choose a different location to play.')
                continue

            else :
                entryFees += entry_fees[desired_location - 1]
                money = money - entry_fees[desired_location - 1]

                with open('User Money.txt','w') as um :
                    um.write(str(money))

                break

        print('\nSelecting Opponent...')
        time.sleep(3)
        print(userTeamName,end='\t')
        print('vs\t',end='')
        sys.stdout.flush()
        print(oppTeamName)
        print(f'\nTeam members of {oppTeamName} are as follows :-\n')

        for players in oppTeam :

            oppPlayerSpeed = random.randint(20,180)
            oppPlayerSpeeds.append(oppPlayerSpeed)
            print(f'{players}\t{oppPlayerSpeed}')

        print('\nToss Time :- You want to choose HEAD or TAIL ?\n\nPress 1 for Head\nPress 2 for Tail')
        user_toss = int(input('>>> '))
        print(f'\nYour Choice : {toss[user_toss - 1]}')

        if toss[user_toss - 1] == 'Head' :
            print(f'{oppTeamName}\'s Choice : Tail')

        else :
            print(f'{oppTeamName}\'s Choice : Head')

        print('\nFlipping Coin...')
        time.sleep(2)
        tossOutcome = random.choice(toss)
        print(f'Outcome : {tossOutcome}')

        if tossOutcome == toss[user_toss - 1] :
            print('\nYou win!!You want to choose Batting or Bowling ?\n\nEnter 1 for Batting\nEnter 2 for Bowling')

            while True :
                userChoice = int(input('>>> '))

                if userChoice == 1 :

                    print('Ok, You will be batting first.')
                    return 'Batting'

                elif userChoice == 2 :

                    print('Ok, You will be bowling first.')
                    return 'Bowling'

                else :

                    print('Kindly enter a valid number.')
                    continue

        else :
            print(f'You lose!! {oppTeamName} choose batting.So you will be Bowling first.')
            return 'Bowling'
        
    except Exception as e :
        print(f'Sorry!! Some error occured.\nError : {e}')

def UserBatNum() :

    '''User Batting Order Generator
Yields player indices (0 to 10) sequentially for the batting lineup.
Usage: Determines the next batter until all 11 have batted.'''

    for i in range(11) :
        yield i

def UserBowlerNum() :

    '''User Bowling Order Generator

Cycles through 11 bowlers, resetting after the 11th.  
Yields the current bowler's index (0 to 10).

Usage: Determines the next bowler in rotation.'''

    iteration = 0
    while True :

        yield iteration
        iteration = (iteration + 1) % 11

def OppBatNum() :

    '''Opponent Batting Order Generator
Yields player indices (0 to 10) sequentially for the opponent's batting lineup.
Usage: Determines the next opponent batter until all 11 have batted.'''

    for i in range(11) :
        yield i

def OppBowlerNum() :

    '''Opponent Bowling Order Generator

Cycles through 11 opponent bowlers, resetting after the 11th.  
Yields the current bowler's index (0 to 10).

Usage: Determines the next opponent bowler in rotation.'''

    iteration = 0
    while True :

        yield iteration
        iteration = (iteration + 1) % 11

userScore = 0
oppScore = 0

def batting(oppTeamName,oppTeam) :

    """
User Batting Simulation

This function simulates the user's batting phase in cricket game. 
The user selects runs to attempt, while the opponent team's fielding and bowling mechanics determine 
whether the user scores runs or gets out.

Functions:
-----------
1. batting(userTeamName, userTeam):
   - Simulates the batting process for the user.
   - Takes the user's team name and lineup as input.
   - Asks the user to choose the number of runs to attempt on each ball.
   - Determines the outcome based on a random bowling value.
   - Handles different dismissal scenarios (bowled, caught, run-out).
   - Updates the score, wickets, and strike rotation accordingly.

2. Opponent Bowling and Fielding Mechanics:
   - The opponent team delivers a random ball value.
   - If the user’s selected run matches the ball value, they are out.
   - Fielders randomly attempt to stop the ball, affecting runs scored.
   - If the ball is stopped, runs are prevented.

3. Game Flow:
   - Runs for a fixed number of overs.
   - Ends when all batters are out or overs are completed.
   - Displays match progress, including runs, balls, and wickets.
   - Includes strike rotation for realistic gameplay.

4. Error Handling:
   - Ensures valid user inputs for run selection.
   - Catches unexpected errors and prevents crashes.

Returns:
--------
- The total score of the user's team after the batting innings.

Usage:
---------------
Run the function, input runs when prompted, and follow the game simulation output."""

    global overs
    global userScore

    over = 0
    ball = 1
    outs = 0
    opp_bowler_num = OppBowlerNum()
    user_bat_num = UserBatNum()
    batting_player = userTeamPlayers[next(user_bat_num)]
    running_partner = userTeamPlayers[next(user_bat_num)]
    bowling_player = oppTeam[next(opp_bowler_num)]

    print('\n----------Starting your Batting----------')
    
    for i in range(overs * 6) :
        try :
            print(f'\nBall : {over}.{ball}\nScore : {userScore}/{outs}')
            print(f'\nBatting : {batting_player}\nRunning Partner : {running_partner}\nBowling : {bowling_player}') 

            beforeBowl = time.time()
            userBattingRun = int(input('\nEnter your batting runs : '))
            afterBowl = time.time() - beforeBowl
            timeTaken = (afterBowl // 1) * 20
            oppBowlingPoints = random.randint(1,6)

            print(f'Your Choice : {userBattingRun}\n{oppTeamName}\'s Choice : {oppBowlingPoints}')

            if userBattingRun < 7 :

                if userBattingRun == oppBowlingPoints :

                    print('You are OUT!!')
                    batting_player = userTeamPlayers[next(user_bat_num)]
                    print(f'Batting will now be done by {batting_player}')
                    outs = outs + 1

                elif timeTaken < 20 :

                    print('You moved your bat early and the ball touched the wicket.\nYou are OUT!!!')
                    batting_player = userTeamPlayers[next(user_bat_num)]
                    print(f'Batting will now be done by {batting_player}')
                    outs = outs + 1

                elif timeTaken > 200 :

                    print('You moved your bat too late that the ball had already passed and touched the wicket.\nYou are OUT!!!')
                    batting_player = userTeamPlayers[next(user_bat_num)]
                    print(f'Batting will now be done by {batting_player}')
                    outs = outs + 1

                elif userBattingRun == 6 :

                    directionNum = random.randint(0,7)
                    print(f'The ball went to {directions[directionNum]}.\n{oppTeam[directionNum]} will try to catch the ball.')
                    print(f'\nSpeed of ball : {timeTaken}\nSpeed of {oppTeam[directionNum]} : {oppPlayerSpeeds[directionNum]}')

                    if timeTaken == oppPlayerSpeeds[directionNum] :

                        print(f'{oppTeam[directionNum]} is able to catch the ball.\nYou are OUT!!!')
                        batting_player = userTeamPlayers[next(user_bat_num)]
                        print(f'Batting will now be done by {batting_player}')
                        outs = outs + 1

                    elif oppPlayerSpeeds[directionNum] > timeTaken :
                        print(f'{oppTeam[directionNum]} is able to stop the ball.\nSo,No runs are scored')

                    else :
                        userScore += 6

                elif userBattingRun == 4 :

                    directionNum = random.randint(0,7)
                    print(f'The ball went to {directions[directionNum]}.\n{oppTeam[directionNum]} will try to stop the ball.')
                    print(f'\nSpeed of ball : {timeTaken}\nSpeed of {oppTeam[directionNum]} : {oppPlayerSpeeds[directionNum]}')

                    if timeTaken <= oppPlayerSpeeds[directionNum] :
                        print(f'{oppTeam[directionNum]} is able to stop the ball.')
                        print('So,No runs are scored')

                    else :
                        userScore += 4
                    
                else :

                    if userBattingRun % 2 == 0 :
                        userScore = userScore + userBattingRun

                    else :
                        batting_player, running_partner = running_partner, batting_player
                        userScore = userScore + userBattingRun

                time.sleep(5)

            else :
                print('The number you have entered is greater than 6.Kindly enter a valid number.')

            if ball == 6 and overs - 1 != over :

                print('\n----------Over Completed----------\nTake a rest')
                time.sleep(3)
                ball = 1
                over = over + 1
                bowling_player = oppTeam[next(opp_bowler_num)]

            else :

                if overs - 1 == over and ball == 6 :

                    print('Your batting ends now.')
                    print(f'You scored {userScore} runs. ')
                    return userScore

                else :
                    ball = ball + 1

        except StopIteration :
            print(f'\nEveryone is out from your team.You scored {userScore} runs.')
            return userScore     

        except Exception as e :
            print(f'\nSorry!!! Some error occured.\nError : {e}')
        
def bowling(oppTeamName,oppTeam) :

    """Cricket Game Simulation (Bowling)

This Python script simulates a cricket match's bowling phase, where the user controls the bowler, and 
the opponent team bats. The game logic includes tracking overs, balls, scores, wickets, and fielding 
mechanics.

Functions:
-----------
1. bowling(oppTeamName, oppTeam):
   - Simulates the bowling process.
   - Takes the opposing team's name and lineup as input.
   - Asks the user to enter the number of runs to bowl.
   - Determines the batting outcome based on random values.
   - Handles different dismissal scenarios (catch, bowled, run-out).
   - Updates the number of outs and scores accordingly.

2. Fielding and Speed Mechanics:
   - The ball is directed randomly to different fielders.
   - The fielder's speed determines whether they stop the ball or drop a catch.
   - If a fielder stops the ball, runs are prevented.

3. Game Flow:
   - The script runs for a fixed number of overs.
   - Stops when all batters are out or overs are completed.
   - Displays match progress, including runs scored and wickets lost.
   - Implements error handling for invalid inputs.

4. Error Handling:
   - Handles invalid user inputs for runs to bowl.
   - Catches unexpected exceptions and prevents crashes.

Returns:
--------
- The total score of the opponent team after the bowling innings.

Usage:
-------
Run the script, enter the required inputs when prompted, and follow the game simulation output.""" 

    global overs
    global oppScore
    
    over = 0
    ball = 1
    outs = 0
    opp_bat_num = OppBatNum()
    user_bowler_num = UserBowlerNum() 
    batting_player = oppTeam[next(opp_bat_num)]
    running_partner = oppTeam[next(opp_bat_num)]
    bowling_player = userTeamPlayers[next(user_bowler_num)]
 
    print('\n----------Starting your Bowling----------')

    for i in range(overs * 6) :
        try :
            print(f'\nBall : {over}.{ball}\nScore : {oppScore}/{outs}')
            print(f'\nBatting : {batting_player}\nRunning Partner : {running_partner}\nBowling : {bowling_player}')
            
            userBowlingPoints = int(input('Enter runs to bowl : '))
            oppBattingRun = random.randint(1,6)
            timeTaken = random.randint(0,6) * 20

            print(f'Your Choice : {userBowlingPoints}\n{oppTeamName}\'s Choice : {oppBattingRun}')
            
            if userBowlingPoints < 7 :

                if userBowlingPoints == oppBattingRun :

                    print(f'{batting_player} is OUT!!')
                    batting_player = oppTeam[next(opp_bat_num)]
                    print(f'Batting will now be done by {batting_player}')
                    outs = outs + 1

                elif timeTaken < 20 :

                    print(f'{batting_player} moved his bat early and the ball touched the wicket.\n{batting_player} is OUT!!!')
                    batting_player = oppTeam[next(opp_bat_num)]
                    print(f'Batting will now be done by {batting_player}')
                    outs = outs + 1

                elif timeTaken > 200 :

                    print(f'{batting_player} moved his bat too late that the ball had already passed and touched the wicket.\n{batting_player} is OUT!!!')
                    batting_player = oppTeam[next(opp_bat_num)]
                    print(f'Batting will now be done by {batting_player}')
                    outs = outs + 1

                elif oppBattingRun == 6 :

                    directionNum = random.randint(0,7)
                    print(f'The ball went to {directions[directionNum]}.')
                    print(f'{userTeamPlayers[directionNum]} will try to catch the ball.')
                    print(f'\nSpeed of ball : {timeTaken}\nSpeed of {userTeamPlayers[directionNum]} : {selectionPlayersSpeed[directionNum]}')

                    if timeTaken == selectionPlayersSpeed[directionNum] :

                        print(f'{userTeamPlayers[directionNum]} catch the ball.')
                        print(f'{batting_player} is OUT!!!')
                        batting_player = oppTeam[next(opp_bat_num)]
                        print(f'Batting will now be done by {batting_player}')
                        outs = outs + 1

                    elif selectionPlayersSpeed[directionNum] > timeTaken :

                        print(f'{userTeamPlayers[directionNum]} is able to stop the ball.')
                        print('So, no runs are scored')

                    else :
                        oppScore += 6

                elif oppBattingRun == 4 :

                    directionNum = random.randint(0,7)
                    print(f'The ball went to {directions[directionNum]}.')
                    print(f'{userTeamPlayers[directionNum]} will try to stop the ball.')
                    print(f'\nSpeed of ball : {timeTaken}\nSpeed of {userTeamPlayers[directionNum]} : {selectionPlayersSpeed[directionNum]}')

                    if timeTaken <= selectionPlayersSpeed[directionNum] :

                        print(f'{userTeamPlayers[directionNum]} is able to stop the ball.')
                        print('So, no runs are scored')

                    else :
                        oppScore = oppScore + 4
                
                else :

                    if oppBattingRun % 2 == 0 :
                        oppScore = oppScore + oppBattingRun

                    else :
                        batting_player, running_partner = running_partner, batting_player
                        oppScore = oppScore + oppBattingRun

                time.sleep(5)

            else :
                print('The number you have entered is greater than 6.Kindly enter a valid number.')

            if ball == 6 and overs - 1 != over :

                print('\n----------Over Completed----------\nTake a rest')
                time.sleep(3)
                ball = 1
                over = over + 1
                bowling_player = userTeamPlayers [next(user_bowler_num)]

            else :

                if overs - 1 == over and ball == 6 :

                    print('Your bowling ends now.')
                    print(f'They scored {oppScore} runs')
                    return oppScore

                else :
                    ball = ball + 1

        except StopIteration :
            print(f'\nEveryone is out from {oppTeamName} team.They scored {oppScore} runs.')
            return oppScore     

        except Exception as e :
            print(f'\nSorry!!! Some error occured.\nError : {e}')
            
overs = 0
entryFees = 0
userScore = 0
oppScore = 0
oppPlayerSpeeds = []

def main() :

    '''Main function for the Hand Cricket game.

    This function initializes the game, prompts the user for a password, and allows them to play a match.
    The user can choose to start a match, view their details, or exit the game.
    
    Functionality:
    - Prompts the user for a password to access the game.
    - Randomly selects an opponent team name and players.
    - Starts a match where the user and the opponent take turns batting and bowling.
    - Determines the winner based on scores and updates the user's prize money.
    - Provides options to view user details or exit the game.

    The game follows standard hand cricket rules where the user and opponent take turns in batting and bowling.

    Exceptions:
    - Handles incorrect user input and general exceptions to avoid crashes.

    Returns:
    - None''' 
    
    global userScore
    global oppScore
    global entryFees
    global overs
    global money
    global oppPlayerSpeeds
    
    print('\t  𝗛𝗔𝗡𝗗 𝗖𝗥𝗜𝗖𝗞𝗘𝗧 𝗦𝗛𝗢𝗢𝗧')
    entered_password = input('\nEnter your password : ')
    if entered_password == password :

        while True :
            try :

                oppTeamName = random.choice(cricketer_team_names)
                oppTeam = []
                userScore = 0
                oppScore = 0 
                
                print('\nYou want to Start Next Match, See Your Details Or Exit?\n\nPress 1 to Star\
t Next Match.\nPress 2 to See Your Details.\nPress 0 to Exit The Game. ')
                userChoice = int(input('\n>>> '))
                
                if userChoice == 1 :

                    for i in range(11) :
                        oppTeamMembers = random.choice(opponent_cricketers)
                        oppTeam.append(oppTeamMembers)
                        opponent_cricketers.remove(oppTeamMembers)

                    print()
                    tossResult = StartingMatch(oppTeamName,oppTeam)
                    
                    if tossResult == 'Batting' :

                        user_score = batting(oppTeamName,oppTeam)
                        opp_score = bowling(oppTeamName,oppTeam)

                        if user_score > opp_score :
                            print('\nCongratulations!! You have won the match!')
                            prize = entryFees * 2
                            print(f'You got ${prize:,}')
                            money = money + prize

                            with open('User Money.txt','w') as um :
                                um.write(str(money))

                        elif user_score == opp_score :
                            print(f'It\'s a Tie!!\nYou got ${entryFees:,}')
                            money = money + entryFees
                            with open('User Money.txt','w') as um :
                                um.write(str(money))
                        else :
                            print('Sorry!! You lose the match. Better luck next time!')

                    else :
                        
                        opp_score = bowling(oppTeamName,oppTeam)
                        user_score = batting(oppTeamName,oppTeam)

                        if user_score > opp_score :
                            print('\nCongratulations!! You have won the match!')
                            prize = entryFees * 2
                            print(f'You got ${prize:,}')
                            money = money + prize

                            with open('User Money.txt','w') as um :
                                um.write(str(money))

                        elif user_score == opp_score :
                            print(f'It\'s a Tie!!\nYou got ${entryFees:,}')
                            money = money + entryFees
                            with open('User Money.txt','w') as um :
                                um.write(str(money))

                        else :
                            print('Sorry!! You lose the match. Better luck next time!')
                          
                    overs = 0
                    oppScore = 0
                    userScore = 0
                    entryFees = 0
                    oppPlayerSpeeds.clear()                 
                
                elif userChoice == 2 :
                    UserInfo() 
                    
                elif userChoice == 0 :
                    break
                    
                else :
                    print('Please enter a valid number')
                
            except Exception as e :
                print(f'Sorry!! Some error occurred!\nError : {e}')

    else :
        print('Wrong Password')

if __name__ == '__main__' :
    main()