# import random

# def controls():
#     print("welcome to the Guessing Game of Heavens You have three chances to pick a number 1 - 10")

# controls()

# guess_limit = 1
# number = random.randint(1, 10)

# user = int(input('Enter a value'))

# while user != number:
#     if user > number:
#         print("You are Guessed too LOW")
#     elif user < number:
#         print('You are Guessed too HIGH')
#         continue
#     guess_limit += 1
        
#     if guess_limit == 3:
#             print("------------------------------------------------------")
#             print("You ran out of guess ;( the answer was", number, "<--")
#             print("------------------------------------------------------")
#             break    
#     else:
#         print("You guessed it right! The number is", number,
#             "and it only took you ", guess_limit, "tries")


import random

def instructions():
    print("Welcome to the number guessing game.")
    print("Guess a number between 1 and 10.")
    print("You only have 3 guesses.")

def game():
    # Guess limit so the user can only guess three times
    guess_limit = 1
    # The random guess
    actual_number = random.randint(1, 10)
    # What user can type and see
    guessed_number = int(input("What is the number?: "))
    # In case you guessed it right at the first time
    if actual_number == guessed_number:
        print("You guessed it right! The number is ", actual_number) 
    # The while loop so it can go on
    while guessed_number != actual_number:
        if guessed_number > actual_number:
            print("Lower")
        elif guessed_number < actual_number:
            print("Higher")
        
        guessed_number = int(input("What is the number?: "))
        guess_limit += 1
        if guess_limit == 4 and guessed_number != actual_number:
            print("You ran out of guess, The answer was number ",  actual_number)
            break
        
        else:
            print("You guessed it Wrong! The number is ", actual_number)    

instructions()
game()