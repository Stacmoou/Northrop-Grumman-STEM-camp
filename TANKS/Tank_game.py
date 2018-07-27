#Tank game using our Tank class
from Tank import Tank

print("Welcome to the Tank game!")

tanks = {}
numPlayers = int( input("How many players? ") )
for player in range(1, numPlayers+1):
    printString = "Player" + str(player) + "'s name: "
    tanks[player] = Tank( input(printString) )

    aliveTanks = len(tanks)

while aliveTanks >1:
# List the tanks and their stats
    print()
    for playerNum in tanks.keys():
        print(playerNum, tanks[playerNum])
# Loop for players to take turns
    for playerNum in tanks.keys():
        playerTank = tanks[playerNum]

        if not playerTank.alive:
            continue
        print()
        print(playerTank.name + ", it's your turn!")
        target = int(input(tanks[playerNum].name + " fires at player: "))
#checking for player, alive, and not self
        try:
            targetTank = tanks[target]
        except KeyError as name:
            print("There is no player", str(name), "!")
            continue
        if not targetTank.alive:
            print("Player", str(target)+ ",", targetTank.name + ",is dead!")
            continue
        if targetTank.name == playerTank.name:
            print("You shouldn't fire at yourself!")
            continue
        print()
        print("*" * 30)

        playerTank.fireAt(targetTank)
        if not targetTank.alive:
            aliveTanks -= 1

        print("*" * 30)

#Determine the winner
for tank in tanks.values():
    if tank.alive:
        print(tank.name, "is the winner!")
        break
