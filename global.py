def myfunc():
  global x
  x = 300

myfunc()

print(x)

# changing a global variable inside a function 
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)