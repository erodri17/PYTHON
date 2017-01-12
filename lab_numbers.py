# Name: Elmer Rodriguez
# Institution: University of Rochester
# Professor: Richard Sarkis
# Course: CSC 161: INTRO TO PROGRAMMING
# Assignment: Numbers
# All Rights Reserved

#Import math library
import math

def main():
    #The program should print a short introduction about its purpose.
        print('This program calculate the square root of a given number using the Newtons method')
    #Prompt the user for the value xx to find x root(x).
        x = input('What is the number for which you want to calculate the square root?')
    #Prompt the user for the number of times to improve the guess.
        n = input('How many iterations do you want to use?')
    #Using Newtwon's method in order to estimate the square root
        estimation = x * 0.5
        for i in range(n):
    #The variable estimation stores the result from calculation using Newtons method
            estimation = (estimation + (x / estimation))/ 2.0
            print(i + 1, estimation, estimation - math.sqrt(x))
    #Printing the results
        print('My guess for the square root of ',x,' is ', estimation)
        print('The difference between my guess and the real result is ', estimation- math.sqrt(x))
#Main method
main()


'''
lab_numbers.py OUTPUT

This program calculate the square root of a given number using the Newtons method
What is the number for which you want to calculate the square root?100
How many iterations do you want to use?10
(1, 26.0, 16.0)
(2, 14.923076923076923, 4.923076923076923)
(3, 10.812053925455988, 0.812053925455988)
(4, 10.030495203889796, 0.030495203889795874)
(5, 10.000046356507898, 4.63565078980821e-05)
(6, 10.000000000107445, 1.0744471978796355e-10)
(7, 10.0, 0.0)
(8, 10.0, 0.0)
(9, 10.0, 0.0)
(10, 10.0, 0.0)
('My guess for the square root of ', 100, ' is ', 10.0)
('The difference between my guess and the real result is ', 0.0)

'''