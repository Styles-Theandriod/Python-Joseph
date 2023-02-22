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
print(type(myDictionary))# know the type of class 
print(myDictionary)
# using the keys to get all the values form our dictionary 

print(myDictionary.keys())

# get item from the dictionary Using the get method
print(myDictionary.get('Name'))

print(myDictionary['Age'])

OurDictionary = dict(Name = "Style", lastName ="Theandriod") 
# the same as using {} but now using a keyword 

print(len(OurDictionary)) # length of the dictionary 

dictionary = {
    'Name' : 'StringAfrika',
    'school' : 'Bizmarrow Tedhnologies'
}

print(dictionary.keys())

dictionary['brand'] = "white"
print(dictionary)


# getting the values from the dictionary 
print(dictionary.values())

# print('\n') line breaker 
# print(dictionary.items()) Get all item from the dictionary

# to check if a key is available

if 'Name' in dictionary:
    print("Woo i am here")
else:
    print('Woo Please add me!!')


# To Update an item in a dictionary 
# dictionary.update({'Name': 'Onyekachi'},{'Nam': 'Steven'} )
print(dictionary)

# adding an item using the update keyword will also add an
# item if itz does not exist 
# Update() 

# Removing an item in a dictionary 
dictionary.pop("Name")
print(dictionary)

# Removing the last Inserted Item in the dictionary 
dictionary.popitem()
print(dictionary)

# Using the del keyword to delete  dictionary entirely 
# del dictionary
# print(dictionary)

# using the clear method to clear the dictionary entirely 
# dictionary.clear()
print(dictionary)



# Looping Through the dictionary 
friday = ['monday', 'Tuesday', 'wednesday', 'Thursday']
for x in friday:
    print(x)
    


