# try:
#     New_file = open("function.py", "x")
# except:
#     New_file = open("Disturb.txt", "w")
#     New_file.write ("this file is now working")
# else:
#     print ("You have done rubbish")

try:
    New_file = open("function.py", "x")
except:
    New_file = open("Disturb.txt", "r")
    New_file.write ("this file working")

finally:
    New_file = open("Disturb.txt", "a")
    New_file.write ("\n" +"this working")
