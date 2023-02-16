names = ["Bob", "James", "Emeka", "Okeke", "Jennifer", "Kimberly"]

# for name in names:
#     print(name.upper())

numbers = range(1, 21)
second__numbers = list(range(21, 31))

# for number in numbers:
#     print(number)


# for number in second__numbers:
#     print(number)

# print('Maximum Number -', max(numbers))
# print('Minimum Number -', min(numbers))
# print('Sum of Numbers - ' + str(sum(numbers)))
# print('Sum of Numbers -', sum(numbers))


# SLICING A LIST
print('Sliced List -', names[2:5])

# for name in names[2:5]:
#     print(name)


# COPYING A LIST
chrisBrownChics = ["Bernice Burgos", "Sawatie", "Ari"]
drakeChics = chrisBrownChics[:]

print('Chris Brown\'s Chics -', chrisBrownChics)
print("Drake's Chics -", drakeChics)