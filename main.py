import random
def findhighest (playerscores,players):
  winnerscore = playerscores[0]
  for i in range(len(playerscores)):
    if winnerscore < playerscores[i]:
      winnerscore = playerscores[i]
  highestplayers = []
  for i in range(len(playerscores)):
    if winnerscore == playerscores[i]:
      highestplayers.append(players[i])
  return highestplayers
  
def didPlayerWin (userchoice,compchoice):
  print ("I choice " + compchoice + "!")
  if userchoice == compchoice:
    return "tie"
  elif (userchoice == "rock" and compchoice == "paper") or (userchoice == "paper" and compchoice == "scissors") or (userchoice == "scissors" and compchoice == "rock"):
    return "win"
  else:
    return "lose"

def play(numofrounds, players, playerpoints):
  #is used for playing and outputting final winners
  for round in range(int(numofrounds)):
    for i in range (len(players)):
      userchoice = input(players[i] +"  type rock, paper, or scissors: ")
      compchoice = random.choice(["rock", "paper", "scissors"])
      status = didPlayerWin(userchoice, compchoice)
      if(status == "tie"):
        print("we tied, you get 1 point added")
        playerpoints[i] = playerpoints[i] + 1
      elif(status == "win"):
        print("you won, you get 2 points added")
        playerpoints[i] = playerpoints[i] + 2
      else:
        print("There were no points added this round for " + players[i] + "!")
  winners = findhighest(playerpoints, players)
  return winners

#done with describing all procedures used later in the game
print("This game is about rock, paper, scissors for multiple players. Each player gets to take turns against the computer to accumulate points based on wins (2pts), ties (1pt), or loses (0). After, if there are any ties, there will be a tiebreaker for this complex angle to the classic game.")
#here are the rules
players=[]
playerpoints=[]
numofplayers = input("how many players do we have with us today? (please input less than 6) ")
while (not numofplayers.isnumeric() or int(numofplayers)>5 ):
  numofplayers = input("That was invalid! Please re-enter: how many players do we have with us today? ")
#decides number of players
for i in range(int(numofplayers)):
  players.append(input("add a player's name!"))
  playerpoints.append(0)
print ("here are the players: " + str(players))
#here, the list of players is made and the rules are given
numofrounds = input("how many rounds do you want to play today? (please input less than 6) ")
while (not numofrounds.isnumeric() or int(numofrounds)> 5):
  numofrounds = input("That was invalid! Please re-enter: how many rounds do you want to play today? ")
  #decides number of rounds
winners = play(numofrounds, players, playerpoints)
# this is when the play procedure is called
if (len(winners))>1:
  print ("WE HAVE A TIEBREAKER ROUND! There will be one final round with just the two tied candidates. Whoever wins from this will be crowned winner. If the winners tie again, they all get declared as the final winner after the tie breaker round. Let's begin: ")
  print ("the players going into the tiebreaker round are: " + str(winners))
  numofrounds = 2
  #starting tiebreakers
  winnerscores = []
  for i in range(len(winners)):
    winnerscores.append(0)
  winners1 = play(numofrounds, winners, winnerscores)
  print ("the final winner/s are/is: ")
  print (winners1)
else:
  print ("the winner is... " + str(winners))