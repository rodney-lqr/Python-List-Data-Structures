dinosaurNames = ["Allosaurus", "Stegosaurus", "Brachiosaurus", "Velociraptor", "Ankylosaurus", "Spinosaurus", "Dilophosaurus", "Pterodactyl"]

print()
print(dinosaurNames)
print()
print("The 4th index is: ", dinosaurNames[3])
print()
dinosaurNames[5] = "Tyrannosaurus Rex"
del dinosaurNames[6]
for x in dinosaurNames:
    print(x)

print()
print("The last index is: ", dinosaurNames[-1])
print()