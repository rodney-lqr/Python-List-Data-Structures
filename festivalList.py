festivals = [
    "Carnival (Rio de Janeiro)",
    "Oktoberfest (Munich)",
    "Coachella (Indio, California)",
    "Burning Man (Black Rock Desert, Nevada)",
    "Tomorrowland (Boom, Belgium)",
    "La Tomatina (Buñol, Spain)",
    "Holi (India)",
    "Day of the Dead (Mexico)",
    "Edinburgh Fringe Festival (Scotland)",
    "Venice Carnival (Italy)",
    "Glastonbury Festival (England)",
    "Mardi Gras (New Orleans)",
    "Bonnaroo (Manchester, Tennessee)",
    "Comic-Con International (San Diego)",
    "Fuji Rock Festival (Japan)"
]

print()
print(festivals)
print()
print("The 7th index is: ", festivals[6])
print()
festivals[10] = "Diwali"
del festivals[8]
for x in festivals:
    print(x)
print()
print(festivals[4:11])
print()
print(festivals[-1])
print()