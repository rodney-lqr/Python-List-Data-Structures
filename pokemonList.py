pokemons = ["Charmander", "Bulbasaur", 
    "Squirtle", "Eevee", 
    "Gengar", "Lucario", 
    "Dragonite", "Mewtwo", 
    "Gyarados", "Togepi", 
    "Jigglypuff", "Snorlax", 
    "Magikarp", "Espeon"
]

print()
print(pokemons)
print()
print("The 9th index is: ", pokemons[8])
print()
pokemons[11] = "Pikachu"
del pokemons[10]
for x in pokemons:
    print(x)

print()
print(pokemons[3:6])
print()
print("The last index is: ", pokemons[-1])
print()
