#Creating and adding items from the list
groupOne = ["Mark", "James", "Walter", "Perci", "Joana"]
groupTwo = ["Rodney", "Danica", "Jayson", "Leon", "Blake"]
groupThree = ["Harold", "Kobs", "Jenny", "Marie", "Chris"]
#Concatenating all the groups together
allStudents = groupOne + groupTwo + groupThree
#Printing index number 11
allStudents[11] = "John"
print()
print()
#Printing the 15th index of the list
print("The 15th index is: ", allStudents[-2])
print()
print()
#Modified the item in index number 11
print("The updated student: ", allStudents[10])
print()
print()
#Deleting the 9th index
allStudents.remove(allStudents[8])
print()
print()
print(allStudents)

