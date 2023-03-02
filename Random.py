import random;

# random.seed(10)
# print(random.random())

# using the choice random method 

fruits = ["banna", "orange", 'pawpaw', "mango"]
print(random.choice(fruits)) #randomly select values to print

random.shuffle(fruits)
print(fruits)