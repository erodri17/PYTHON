# @Author: Elmer Rodriguez <elmerxavierrodriguez>
# @Date:   09-16-2017 <04:12:47 PM>
# @Email:  elmer.rodriguez6@gmail.com
# @Filename: hello.py
# @Last modified by:   elmerxavierrodriguez
# @Last modified time: 09-17-2017 <07:48:28 PM>
# @Copyright: © 2017 ELMER RODRIGUEZ ALL RIGHTS RESERVED



#Udemy - Become a Professional Programme`r
#Python Section - Covering the Basics Notes


#Python is a high level machine language

#Hello world
print()
print('Hello World')

#Comma as a space
print('Hello','there')

#Basic operations
print(1+3)
print(1-3)
print(1*3)
print(1/3)

#Floats and so on..
print(1.0 + 3.0)

#variables (number and strings)
exVar = 100
print(exVar)

strVar = "apple"
print(strVar)

#variables (functions)
opVar = exVar / 5.3
print(opVar)

#while loop
condition = 1
while condition < 10:
    print(condition)
'''
Multiple Line Comment Here
'''
condition += 1 #adds 1 to the value


#for loop
exampleList = [1,6,7,3,6,9,0]
for element in exampleList:
    print (element)

    for num in range(1,11):
        print(num)


#if statement
x = 2
y = 7
z = 10

if x > y:
    print(x,'is greater than',y) # nothing happens
if(x < y):
    print(x,'is less than',y) # it prints
if x == y:
    print(x,'is the same as',y)

#cannot do this
#if x < '2'
#        print(x, 'is less than 2')
if x <= y:
    print(x, 'is less than or equal to', y)
if z > y > x <= z > y:
    print(z,'is greater than',y,'which is greater than', x)




#if else statements
x = 13
y = 6

if x < y:
    print(x,'is less than', y)
if x > y:
    print(x,'is greater than',y)

#Elif
    x = 3
    y = 7
    z = 10

    if x > y:
        print(x,'is greater than',y)
    elif x < z:
        print(x,'is less than',z)
    elif y < z:
        print(y,'is less than ',z)
    else:
        print('nothing was the case')
'''
#functions
    def example():
        x = 1
        y = 1
        print(x+y)

example()
'''

#function parameters
def addition(num1, num2):
    answer = num1+ num2
    return answer

x = addition(5,6)
print (x)


def website(font, background_color, font_size, font_color):
    print('font:',font)
    print('background color:',background_color)
    print('font size:', font_size)
    print('font color:', font_color)

website('Times New Roman','white','12','black')

#Writing to a file
writeMe ='Example text'

saveFile = open('exmapleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close() # very important when using write


#Appending  a file
appendMe = 'Some text'

saveFile = open('exampleFile.txt','a')
saveFile.write(appendMe)
saveFile.close()

#Reading fo a file
readMe - open('exampleFile.txt','r').read()
print(readMe)

#Classes in structures

print('Using the calc.(add,sub,mult, or div to solve equations')
class calc:
    def add(x,y):
        answer = x+y
        print(answer)

    def sub(x,y):
        answer = x-y
        print(answer)

    def mult(x,y):
        answer = x*y
        print(answer)

    def div(x,y):
        answer = x/y
        print(answer)


#Input Statistics - Input from User
        name = input('What is your name?: ')
        print('Hello', name)

import statistics
exList = [5,3,2,9,7,4,3,1,8,9,9]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)


==== RESTART: /Users/elmerxavierrodriguez/Desktop/udemy_python/testing.py ====
5.454545454545454
5
9
3.0451153135353137
9.272727272727273


#import syntax
import statistics as s
exList = [5,3,2,9,7,4,3,1,8,9,9]

x = (s.mean(exList)


#modules

def exampleFunc(data):
    print(data)


#Error Handling - Try and Accept

try:
    print('Running the try....')
    print('5'+5)
except Exception as e:
    print(str(e))
    print('Code continues inward')



#List vs Tuples

#Tuples, are not inmmutable (you cant change)
#List is muttable (can change)

def example():
    return 15,19

a,b = example()

print(a)
print(b)

#Iterating through tuples is faster than a list

x = [6,2,3,6,8,9,4,3]

print(x)

print(x[5])

#add a value to teh very end of the list
x.append(12)
print(x)

#(location, value input)
x.insert(5,7)
print(x)

#remove the first 7
x.remove(7)
print(x)

#sorting list
x.sort()
print(x)

#new list
listNames=['Angel','Ken','Jovany','Elmer','John','Ron','Raulin']
listNames.sort()
print(listNames)

#changes the elements on the list - keep that in mind



#Dictionaries
#Unordered groups
gradeDict = {'Kelly':89, 'David':65, 'Jack': 95,'Samantha': 78}
print(gradeDict)
print(gradeDict['David'])
gradeDict['David']  = 56
gradeDict['Jessy'] = 92
print(gradeDict)
del gradeDict['David']
print gradeDict
gradeDict = {'Kelly':[89, 88]}





