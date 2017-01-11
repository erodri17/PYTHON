#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: Elmer Rodriguez
# Institution: University of Rochester
# Professor: Richard Sarkis
# Course: CSC 161: INTRO TO PROGRAMMING
# Assignment: Computer and Programs
# All Rights Reserved


# File: lab_computer_programs.py
# A simple program illustrating chaotic behavior.

#Defining the main function
def main():

    #Printing a line to the user in order to program some context of the program
    print("\nThis program illustrates a chaotic function")
    #The following line is asking the user "How manu numbers should the program print?" and storing that information on the variable (n)
    n = input("How many numbers should I print? ")
    #The following line is asking the user "Enter a number between 0 and 1:" and storing that information on the variable (x)
    x = input("Enter a number between 0 and 1: ")
    #Running a loop within the parameters provided by the user (n) and printing an output stored in the variable (x)
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

#calling the main function
main()
