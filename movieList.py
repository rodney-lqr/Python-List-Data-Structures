movieListOne = [
    'Avengers',
    'Hacksaw Ridge',
    'Interstellar',
    'Nerve',
    'Ready Player One',
    'How to Train your Dragon',
    'Dunkirk',
    'Enteng Kabisote',
    'Captain America',
    'Hulk',
]

movieListTwo= [
    'Avengers: Endgame',
    'Avengers: Age of Ultron',
    'Wreck it Ralph',
    'Alladin',
    'Sonic the Hedgehog',
    'The Flu',
    'Ninja Turtles',
    'Batman',
    'Gagamboy',
    'Spiderman',
]

allMovies = movieListOne + movieListTwo
print()
print(allMovies)
print()
print("The 12th index is: ", allMovies[12])
print()
allMovies[15] = "Inception"
print()
allMovies.remove(allMovies[18])
print(allMovies)
print()
print(allMovies[8:13])
print()
print(allMovies[-1])
print()