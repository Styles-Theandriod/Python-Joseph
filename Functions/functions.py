def greetUser():
    print("Hello Gabby")

greetUser()

# PASSING ARGUMENTS TO A FUNCTION
# def printInformation(firstname, lastname, children):
#     children.append("Ricky")

#     print(firstname, lastname, "has", str(len(children)), "children.")

#     for child in children:
#         print(child)


# printInformation("Cristiano", "Ronaldo", ["Cristiano Jr.", "Bobby", "Amira"])

# PASSING A DEFAULT ARGUMENT TO A FUNCTION
# def printInformation(children, firstname="Harry", lastname="Maguire"):
#     print(firstname, lastname, "has", str(len(children)), "children.")

#     for child in children:
#         print(child)

# printInformation(["Bob", "Ruth"])

# RETURNING A VALUE IN FUNCTIONS
def printInformationII(firstname, lastname, children):
    sentence = firstname + " " + lastname + " " + "has" + " " + str(len(children)) + " " + "children."

    return sentence

kylian = printInformationII("Kylian", "Mbappe", ["Bob", "James"])
ronaldo = printInformationII("Cristiano", "Ronaldo", ["CR7 Jr.", "Amira", "Jenson"])
maguire = printInformationII("Harry", "Maguire", ["Bob", "James"])

print(kylian)
print(ronaldo)
print(maguire)
