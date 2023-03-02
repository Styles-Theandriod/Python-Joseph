<<<<<<< HEAD
# def Add(fname):
#     a = 5
#     b = 20
#     print(a + b,"\n",fname)

# Add('emmanuel')

def our_function(fname):
    print(fname + 'Refsnes')
our_function('Emma')
our_function('chi')
our_function('Steven')


# dont know the amount of aguments in 
# a function please and please add a * before 
# the parameter name in the function

def my_children(*child):

    print("my second child is" + child[1])

my_children("emil", 'Philip', "David")

# Keyword Argument using Key = value format 

def Family(child1 , child2, child3):
    print('I am' + child3 + 'In the family')

Family(child1 = 'emma', child2 = 'Joe', child3 = 'Elon Musk')


# Arbitrary keyword Arguments, **kwags 

def Another_functions(**Data):
    print("His first Name is " + " " + Data["lname"])
Another_functions(fname = "Micheal", lname = "Felix macoss")

print('\n')

# Deafault Parameter Values in Python 
def our_value(language= "Youruba"):
    print("I am an " + language + ' Boy')

our_value()
# our_value('Igbo')
# our_value('Tiv')
# our_value('Ondo')

# passing a List as an Argument  in python 
def my_food(food):
    for x in food:
        print(x)

fruits = ['green pea', 'Beans', "Soya Beans"]

my_food(fruits)


# Returning values into The Terminal 
def Our_Values(x):
    return x + 5

print(Our_Values(5))
print(Our_Values(10))
print(Our_Values(15))
print(Our_Values(20))
=======
# def Add(fname):
#     a = 5
#     b = 20
#     print(a + b,"\n",fname)

# Add('emmanuel')

def our_function(fname):
    print(fname + 'Refsnes')
our_function('Emma')
our_function('chi')
our_function('Steven')


# dont know the amount of aguments in 
# a function please and please add a * before 
# the parameter name in the function

def my_children(*child):

    print("my second child is" + child[1])

my_children("emil", 'Philip', "David")

# Keyword Argument using Key = value format 

def Family(child1 , child2, child3):
    print('I am' + child3 + 'In the family')

Family(child1 = 'emma', child2 = 'Joe', child3 = 'Elon Musk')


# Arbitrary keyword Arguments, **kwags 

def Another_functions(**Data):
    print("His first Name is " + " " + Data["lname"])
Another_functions(fname = "Micheal", lname = "Felix macoss")

print('\n')

# Deafault Parameter Values in Python 
def our_value(language= "Youruba"):
    print("I am an " + language + ' Boy')

our_value()
# our_value('Igbo')
# our_value('Tiv')
# our_value('Ondo')

# passing a List as an Argument  in python 
def my_food(food):
    for x in food:
        print(x)

fruits = ['green pea', 'Beans', "Soya Beans"]

my_food(fruits)


# Returning values into The Terminal 
def Our_Values(x):
    return x + 5

print(Our_Values(5))
print(Our_Values(10))
print(Our_Values(15))
print(Our_Values(20))
>>>>>>> 43f14d8bf8d5dc92d7b585ef89b61f86da110c61
