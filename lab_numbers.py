# Name: Elmer Rodriguez
# Institution: University of Rochester
# Professor: Richard Sarkis
# Course: CSC 161: INTRO TO PROGRAMMING
# Assignment: Numbers
# All Rights Reserved

#import math library
import math

class main():
    #The program should print a short introduction about its purpose.
        print('This program calculate the square root of a given number using the Newtons method')
    #Prompt the user for the value xx to find x root(x).
        x = input('What is the number for which you want to calculate the square root?')
    #Prompt the user for the number of times to improve the guess.
        n = input('How many iterations do you want to use?')
    #Using Newtwon's method in order to estimate the square root
        def newtownMethod(x,n):
            guessValue = 0.5 * x
            finalValueOfGuess = 0.5 * (guessValue+x/guessValue)
            guessValue = finalValueOfGuess
            return finalValueOfGuess
    #The difference variable that stores the valie of the deffirence between my estimate and the actual result
        difference = math.sqrt(x) - newtownMethod(x,n);
        guess = newtownMethod(x,n)
    #Printing the results
        print('My guess for the square root of ',x,' is ',guess)
        print('The difference between my guess and the real result is ',difference )
    #Main method
main()