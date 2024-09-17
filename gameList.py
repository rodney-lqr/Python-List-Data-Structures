gameList = [
    "The Warriors", "Grand Theft Auto V", "League of Legends",
    "God of War", "Guitar Hero", "GTA: San Andreas",
    "Manhunt", "Bully", "DOTA 2",
    "Tekken", "Super Mario", "PacMan",
    "Fix it Felix Jr.", "It takes two", "Wukong",
]

print()
print(gameList)
print()
print("The 7th index is: ", gameList[7])
print()
gameList[4] = "Minecraft"
print()
gameList.remove(gameList[9])

for x in gameList:
    print(x)

print()
print(gameList[5:10])
print()
print("The last index is: ", gameList[-1])
print()
