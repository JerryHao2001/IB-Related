# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 07:21:10 2018

@author: 11658
"""

print("Please think of a number between 0 and 100!")
guess = 50
high,low = 100 ,0
while True:
    print("Is your secret number {}?".format(guess))
    jug = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if jug == 'c':
        break
    elif jug == "h":
        high = guess
        guess = int((guess + low)/2)
    elif jug == 'l':
        low = guess
        guess = int((guess + high)/2)
    else :
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", guess)
