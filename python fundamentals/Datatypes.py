# strings str
# number int, float complex
# list, turple, range
# dictionary dict
# set, frozenset
# bool
# bytes, bytearray, memoryview
# NoneType

words = '60'
secondWords = str('50')
result = words + secondWords

complex = complex(70)
print(complex)

myfloat = float(30)
print(myfloat)

myList = ["PHP", "PYTHON", "JAVASCRIPT"]
# myList = []
myList.pop(2)

myCount = myList.count("JAVASCRIPT")

# myList[2] = "emma"

print(myList)

# print(myList[0:-2])
# print(type(myList))

# myTurple = ("Glk", "Benz", "Country man")
# print(myTurple)

# myRange = range(64, 50)
# print(type(myRange))
# print(myRange)

myDictionary = {'Name': 'emmanuel', 'Age' : 30,'location' : 'Central area'}
print(type(myDictionary))
print(myDictionary)
# using the keys to get all the values form our dictionary 

print(myDictionary.keys())

# get item from the dictionary Using the get method
print(myDictionary.get('Name'))

print(myDictionary['Age'])



