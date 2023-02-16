names = ["Bob", "James", "Emeka", "Okeke", "Jennifer", "Kimberly"]

# print(names[0])

sentence = names[2] + " is a big boy. He clubs at Cubana almost every two days."
# print(sentence)

# print(names)

# MODIFYING ELEMENTS IN A LIST
names[2] = "Emeka Wire Wire"
# print(names)

# ADDING ELEMENTS TO A LIST
names.append("Puffy")
# print(names)

# ADDING ELEMENTS TO LIST USING THE INSERT METHOD
names.insert(2, "Tega")
# print(names)

# REMOVING ELEMENTS FROM A LIST USING THE pop() METHOD
names.pop()
# print(names)

# REMOVING ELEMENTS FROM A LIST USING THE del METHOD
del names[3]
# print(names)

# REMOVING ELEMENTS FROM A LIST USING THE pop() METHOD
names.pop(4)
# print(names)

# REMOVING ELEMENTS FROM A LIST USING THE remove() METHOD
names.remove('James')
# print(names)




####### ORGANIZING A LIST #######
numbers = [92, 3, 66, 101, 32, 75]
# print(numbers)

numbers.sort()

# SORTING A LIST TEMPORARILY
new_list = sorted(numbers)

print(new_list)

# REVERSE A LIST
numbers.reverse()
print(numbers)

# FIND THE LENGTH OF A LIST
print('Length -', len(numbers))