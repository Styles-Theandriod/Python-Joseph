def add_numbers(Num1, Num2):
    # Num1 = 30
    # Num2 = 50
    print( Num1 + Num2)

add_numbers(30, 50)

# abitrary arguments 
def my_children(*child):
    print("my second child is" + child[1])

my_children("emil", 'Philip', "David")


# Keyword Argument using Key = value format 
def Family(child1 , child2, child3):
    print('I am' + child3 + 'In the family')

Family(child1 = 'emma', child2 = 'Joe', child3 = 'Elon Musk')


#  Arbitrary keyword Arguments, **kwags 
def Another_functions(**Data):
    print("His first Name is " + " " + Data["lname"])
Another_functions(fname = "Micheal", lname = "Felix macoss")

# Deafault Parameter Values in Python 
def our_value(language= "Youruba", state= "FCT"):
    print("I am an " + language + ' ' + state +  ' Boy')

our_value()
our_value('Igbo', 'Central area')
our_value('Tiv')
our_value('Ondo')


# # passing a List as an Argument  in python 
def my_food(food):
    for x in food:
        print(x)

fruits = ['green pea', 'Beans', "Soya Beans"]

my_food(fruits)

# # Returning values into The Terminal 
def Our_Values(x):
    return x + 5

print(Our_Values(5))
print(Our_Values(10))
print(Our_Values(15))
print(Our_Values(20))

# optional aguments in python 
def my_func(a = 1, b = 2, c = 3):
	print(a + b + c)
    
my_func()