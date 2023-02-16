# C - Create
# R - Read
# U - Update
# D - Delete

cars = ["BMW", "Mercedes Benz", "Mustang", "Tesla", "Audi"]

# for car in cars:
#     if car == "Mustang":
#         print("Yeah!! I just got a black mustang.")
#     elif car == "Tesla":
#         print("Tesla things things on my mind next year.")
#     else:
#         print("I'm considering.")

students = ["Jennifer", "Edith", "Stephanie", "Chikamso","Diamond"]

# for student in students:
#     if student == "Edith":
#         print(student + " is the class captain.")
#     elif student == "Jennifer":
#         print(student + " is the assistant class captain.")
#     elif student == "Stephanie":
#         print(student + " is the assistant class captain.")
#     elif student == "Chikamso":
#         print(student + " is the assistant class captain.")
#     else:
#         print(student + " is a regular class member.")

charged = False

# if charged == True:
#     print("I don't need to take my charger out.")
# else:
#     print("I need to take my charger out")


# CHECKING IF A VALUE IS IN A LIST
if "Princess" in students:
    print("Princess is part of this class")
else:
    print("Princess please go to your class.")


# CHECKING IF A VALUE IS NOT IN A LIST
if "Stephanie" not in students:
    print("Stephanie you are not a memeber of this class.")
else:
    print("Stephanie welcome to class.")