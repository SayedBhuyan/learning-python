presents = ["Sayed", "Tareq", "Sultan", "Hassan", "Alim", "Sohel", 'Rakib'] # came on time
presents.append("Muhammad") # coming late


presents.sort()
# presents.reverse()

presents.insert(0, "Teacher") # teacher came and set before everyone else

# presents.pop(-2)

# presents.remove("Teacher") # teacher or anyone can leave

libraryPresents = presents.copy() # students moved to library
libraryPresents.append("Abdul") # abdul also joined in library
libraryPresents.append("Hassan") # two students same name in the same class
print("Library Presents", libraryPresents)

print(libraryPresents.index("Rakib")) # check the position of a student in class

print(libraryPresents.count("Hassan"))

presents.clear() # class finish

print(presents)
print(len(presents))



# print((presents + ['|']) * 3)

#print(students[2:])
# print(students[-1])


# isPresent = input("Who you wan't to call in class?")

# print(isPresent in presents)






'''i = 0;
while i < 4:
    print(students[i])
    i = i+1'''