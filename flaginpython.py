



# num_entry = True
# list1 = []  
# print('enter 0 to stop program')
# while num_entry:
#   ask_user = int(input("Enter the Number: ")) # If entered 0 it will stop 
#   list1.append(ask_user)
#   if ask_user == 0:
#     num_entry = False

# value = True

askUser = [int(x) for x in input('Enter a number: ').split(',')]

Maximum = max(askUser)
    
if isinstance(Maximum, int):
    print('the maximum value is: ', Maximum)

# value = False



