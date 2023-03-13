# # class Myclass:
# #     Num = 25
# #     list = ['egg', 'josh']

# # p1 = Myclass()
# # print(p1.list)

# # class person:
# #     def __int__(self, name, age):
# #         self.name = name
# #         self.age = age

# # result = person("josh", 36)

# # print(result.name)
# # print(result.age)

# # class car:
# #     def __int__(self, make, model, year):
# #         self.make = make
# #         self.model = model 
# #         self.year = year 

# # # my_car = car('audi', 'a6', 2016, "fish")

# # print(car(self).make())


# # class person:
# #     def __int__(self, name, age):
# #         self.name = name
# #         self.age = age

# # p1 = person("john", 36)

# # print(p1.name)
# # print(p1.age)

# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p1 = Person("John", 36)

# # print(p1)

# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# #   def __str__(self):
# #     return f"{self.name}({self.age})"    

# # p1 = Person("John", 36)

# # print(p1)


# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# #   def myfunc(self):
# #     print("Hello my name is " + self.name)

# # p1 = Person("John", 36)
# # p1.myfunc()


# class Person:
#   'This is an object'
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person(name = 'emmanuel', age = 300)
# # p1.age = 65
# del p1.age

# def person():
#     print('i am running myself')

# result = Person("Zara", 2000)

# print("result.__doc__ :",  result.__doc__)
# print("result.__name__ :",  result.__name__)









# class Employee:
#    'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print ("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary)

# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__)

class person:
   def __init__ (self,fname, lname):
      self.fname = fname
      self.lname = lname
   def printname(self):
      print(self.fname, self.lname)

class student(person):
   def __init__(self, fname,lname,year):
      super().__init__(fname,lname)
      self.graduationyear = year
   # To add a method 
   def welcome(self):
      print("welcome", self.fname, self.lname, "to the class of", self.graduationyear)

x = student("Mike", "Olsen", 2019)
x.welcome()
