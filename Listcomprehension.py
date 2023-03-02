Books = ["Rich and poor Dad", "48 Laws of power ", "Think like a man"]

NewList = [] 

# looping through a list and returning the newList 
# for x in Books:
#     if "R" in x:
#         NewList.append(x)

# print(NewList)

# short Hand property for List comprehension
NewList = [x for x in Books if "48" in x]
print(NewList)

# Only accept items that are not 48
NewList = [x for x in Books if x !='48' ]

# without an if statement 
NewList = [x for x in Books]
print(NewList)

# we can also use a range function to create an iterable 
NewList = [x for x in range(10)]
print(NewList)

# Accept only numbers lower than 5
Newlist = [x for x in range(10) if x < 5]
print(Newlist)

# Set The newlist to upper case 
Newlist = [x.upper() for x in Books]
print(Newlist)

# Setting all the newList values to Hello World 
myItem = ["Python", "PHP", "Javascript", "Node Js", "CPP"]
newlist = ['hello world' for x in myItem]
print(newlist)

newlist = [x if x != "Python"  else "orange" for x in myItem]
print(newlist)