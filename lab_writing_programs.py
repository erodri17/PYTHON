#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: Elmer Rodriguez
# Institution: University of Rochester
# Professor: Richard Sarkis
# Course: CSC 161: INTRO TO PROGRAMMING
# Assignment: Writing Simple Programs
# All Rights Reserved


# Writing Simple Programs

# I would like you to write an interactive Python calculator program.

# The program should allow the user to type an arithmetic expression, and then print the value of the # expression. A friendly message should prompt them for the expression they want to evaulate!

# Include a definite loop so that the user can perform 100 different expression calculations. e.g.:

# Enter a mathematical expression: 1 + 1
# 1 + 1 = 2
# Enter a mathematical expression: 3 * 3.1459
# 3 * 3.1459 = 9.4377
# Enter a mathematical expression:
# Your program should print a friendly introduction (one line is fine) that explains what it does
# when the program first runs.
# Source: http://www.pas.rochester.edu/~rsarkis/csc161/labs/writing-programs.html


 #Program Pseudocode
'''
PSEUDOCODE:
We can evaluate Python calculations by using the eval() function. We just need to do that 100 times.
def main():
    # print explanation of program
    for i in range(100):
        # Get input
        # Print eval(input)

# call main program
'''
# Source: https://www.crashwhite.com/introcompsci/materials/assignments/exercises/ch02ex11.py
# Defining the main function
def main():

    # Printing a line to the user in order to program some context of the program
    print("INTERACTIVE CALCULATOR PROGRAM")

    # Running a loop in order to prevent the user from making more than 100 arithmetic expressions
    for i in range(100):

    # The following line is asking the user "Enter a mathematical expression: " and storing that
    # information on the variable (n)
        n = input("Enter a mathematical expression ")

    # printing the final evaluation of the arithmetic expression
        print (input(n))

# calling the main function
main()

# Submission Filename: Your submission requires that you hand in a file called lab_writing_programs

'''
Works Cited
Crashwhite.com. N.p., n.d. Web. 17 Nov. 2016. <https://www.crashwhite.com/introcompsci/materials/assignments/exercises/ch02ex11.py>.
Sarkis, Richard. "Writing Simple Programs¶." Writing Simple Programs — CSC 161: Intro to Programming 0.1 Documentation. N.p., n.d. Web. 17 Nov. 2016. <http://www.pas.rochester.edu/~rsarkis/csc161/labs/writing-programs.html>.

'''


