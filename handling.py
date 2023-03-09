file = open('./Trial.txt',"a")
# print(file.read())
# print(file.read(15))
# print(file.readline())

# looping all the item in a file 
# for x in file:
#     print(x)


# closing a file 
# file.close()

# write to an exiting file 
file.write('Now this is the finall content')
print(file.read())
file.close()
