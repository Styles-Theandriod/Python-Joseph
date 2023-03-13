# iterators is an object that 
# contains a countable number of values

# An iterator is an object that can be iterated upon,
# meaning that you can traverse through all the values

# Technically in Python an iterator is an object 
# which implements the iterator pro

# import sys
# sys.path.append("")

# from classes import person

# y = person("Mike", "Olsen")

# print(y.fname)


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

mywords = "SENTENCES"

print(iter(mywords))

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# iterate the values of turple 
# myTurple = ("orange", "Apple", "Banana")

# for item in myTurple:
#     print(item)

# mywords = "SENTENCES"

# while mywords < 8:
#     mywords += 1
   
    


# iterate the values of a string

# myStr = "orange"

# for item in myStr:
#     print(item)


# class Numbers:
#     def iter (self):
#         self.num = 1
#         return self
#     def next (self):
#         y = self.num 
#         self.num += 1
#         return y
    
# myclass = Numbers()
# myiter = iter(myclass)

# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))

# to stop an iteration 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)