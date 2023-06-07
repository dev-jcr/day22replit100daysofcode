# Libraries, getpass use, random library. Guess the random number
from getpass import getpass as getpass
from random import *
import math
while True:
  # User input
  while True:
    guessed = getpass("Write the number that will be guessed or 'r' for a random number: ")
    # input check
    if guessed == "r" or guessed == "R":
      guessed = randrange(1, 1000000)
      break
    elif guessed.__contains__('-'):
      print("No negative numbers, bye!")
      exit()
    else:
      flag = True
      try:
        int(guessed)
      except ValueError:
        flag = False
        print()
        print("Invalid input, you dummy! Only numbers")
        print()
        continue        
    digits = 0
    guessed = int(guessed)
    if guessed > 0:
        digits = int(math.log10(guessed))+1
    elif guessed == 0:
        digits = 1
    else:
        digits = int(math.log10(-guessed))+2 # +1 if you don't count the '-' 
    if digits > 10:
      print("Use a number between 0 and 1.000.000")
      continue
    else:
      break
# Guess the number
  counter = 0
  while True:
    counter +=1
    print()
    guess = input("Guess the number!: ")
    # input check
    flag_guess = True
    try:
      int(flag_guess)
    except ValueError:
      flag_guess = False
    if flag_guess == False:
      print("You didn't inserted an integer, you dummy!")
      continue
    else:
      guess = int(guess)
      guessed = int(guessed)
      if guess > guessed:
        print ("Too high!")
        continue
      elif guess < guessed:
        print("Too low!")
        continue  
      else:
        print()
        print(""" "You guessed it!" The number is """,guessed,)
        break
  print()
  print("Congratulations! You made it after",counter,"attemps.")
  print()
  continue