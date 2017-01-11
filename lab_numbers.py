# Name: Elmer Rodriguez
# Institution: University of Rochester
# Professor: Richard Sarkis
# Course: CSC 161: INTRO TO PROGRAMMING
# Assignment: Numbers
# All Rights Reserved

#The program should print a short introduction about its purpose.
print('This program calculate the square root of a given number using the Newton's method')

#Prompt the user for the value xx to find x√x.
x = input('What is the number for which you want to calculate the square root?')


#Prompt the user for the number of times to improve the guess.
n = input('How many iterations do you want to use?')

#Using Newtwon's method in order to estimate the square root
def newtownMethod(x,n):
    guessValue = 0.5 * x #Starting guess value of (x/2)
    for i in range(n):
        finalValueOfGuess = 0.5 * (guessValue + x/ guessValue)
        guessValue = finalValueOfGuess

    return finalValueOfGuess


#Subtract final estimate from the value of math.sqrt(x) to show how accurate your estimate is.
math.sqrt(x)

main