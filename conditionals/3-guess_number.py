'''Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the 
prompt appears again until the guess is correct, on successful guess, user will
get a "Well guessed!" message, and the program will exit.'''

#My answer
import random
number = 0
guess = random.randint(1, 9)
while number != guess:
    number = int(input('Guess a number between 1 and 10 until you get it right : '))
if int(number) == int(guess):
    print('Well guessed!')
    exit()

#The dev answer
# import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')

#the dev code is more efficiente, and with less lines. he had declared 2 variables in a line
#aproach the while != as a conditional, he doesn't use if.