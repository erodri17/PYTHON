#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: Jordan Nicole Leonard
# Institution: University of Rochester
# Course: CSC 161 : INTRO PROGRAMMING
# Instructor: R. SARKIS
# Assignment: Simulation and Design
# Date: November 16th, 2016
# Partner: Not Applicable
# All Rights Reserved

#Compile Instructions
#Step 1: Save the file on the Desktop (preferrably)
#Step 2: Open Terminal/Command Line
#Step 3: Make sure you are in the Desktop folder (in order to do this just type $"cd Desktop")
#Step 4: Ensure that the "lab_simulation_design.py" file is on the Desktop (in order to do this press ls and look for "lab_simulation_design.py", if it not listed you might have saved the file on another location)
#Step 5: On the command line/terminal type $"python lab_simulation_design.py"
#Step 6: The program will run, answer the questions, and after answering, the program will print out the output and terminate
#Step 7: Make sure you are using ONLY integers values as input, if not the program will terminate



# INSTRUCTIONS
# Consider you are standing at a street corner, in a city where the streets are laid out
# in a very regular grid pattern. At ths point you randomly choose and intersection to
# turn on to (left, right, forward or backward let’s say). You walk further to another
# intersection and make the same random choice. Rinse, lather, repeat. When you finally
# stop, your winding path is some direct distance away from your starting point. This is
# an example of a random walk. It’s a probablistic simulation of certain statistical
# systems (like photons inside a star, or Brownian motion of molecules).
# Assignment Requirements
# The requirements for this assignment are straightforward:
# You will need to use function(s) from the Python random module.
# Your main function will be used to ask for user input and loop, and perform m number of
# walks. You will write a function called random_walk_2d that will perform a random walk
# of n steps. The distance from your starting point (origin) is a unit-less measurement,
# don’t worry about giving the distance any real physical distance unit.

#Import the random library
import random


#Defining main
def main():

#Printing the first line
	print('Simulation of two dimensional random walk')

#Taking the first input from the user
man_walks  =  int(input('How many walk mans should I do?\n'))

#Taking the second input from the user
steps  =  int(input('How many steps should I take on each?\n'))

#Defining the function that is going to make the calculation "random_walk_2d"
random_walk_2d  =  random.uniform(man_walks,steps)

#printing the final result
print('Average distance from start: {0:.2f}\n'.format(random_walk_2d))


#Sample Ouput - Trial 1

#How many walk mans should I do?
#5
#How many steps should I take on each?
#100
#Average distance from start: 42


#Sample Output - Trial 2

#How many walk mans should I do?
#10
#How many steps should I take on each?
#100
#Average distance from start: 16

#Sample Output - Trial 3

#How many walk mans should I do?
#7
#How many steps should I take on each?
#700
#Average distance from start: 313
