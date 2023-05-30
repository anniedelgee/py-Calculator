'''
Part 1

Create a simple calculator application that asks a user to enter two numbers and the operation ( eg. +, -, x, etc.) that they'd like to perform on the numbers. Display the answer to the equation. 

Every equation entered by the user should be written to a text file.
Use defensive programming to write this program in a manner that is robust and handles unexpected events and user inputs. 

 '''

'''

Part 2 

Now extend your program to give the user the option to either enter two numbers and an operator, like before, 
    OR
to read all the equations from a new txt file (the user should add the name of the txt file as an input)
    AND
print out all the equations together with the results.

use defensive coding to ensure that the program does not crash if the file does not exist 
and that the user is prompted agaian to enter the name of the file.

'''

import math

# get user input- numbers
print("This application is a calculator that will take two values and an operator ( +, -, *, / ), compose an equation and return the solution.")

#VARIBALES START
# first number
first_val= float(input("Please enter your first value: "))
#print(first_val)

#second number
second_val= float(input("Please enter your second value: "))
#print(second_val)

# operator
operator= input("What operator are you carrying out? Enter calculation symbol: ")
#print(operator)

#VARIBALES END

#create text file
file = open("calculator.txt", "w")

# create operation
if (operator == '+'):
    answer= (first_val + second_val)
    print(" The sum of " + str(first_val) + " and " + str(second_val) + " is " + str(round(answer, 2)))
elif (operator == '-'):
    answer= (first_val - second_val)
    print(" The difference between " + str(first_val) + " and " + str(second_val) + " is " + str(round(answer, 2)))
elif(operator == '*'):
    answer= (first_val * second_val)
    print(" The product of " + str(first_val) + " and " + str(second_val) + " is " + str(round(answer, 2)))
elif (operator == '/'):
    answer= (first_val / second_val)
    print(" The quotient of " + str(first_val) + " and " + str(second_val) + " is " + str(round(answer, 2)))
else:
    print("please enter valid numerical values and arithmetic operators. this is a calculator not chatgpt.")

 # convert values to represetnations to write to file. 

first_val= repr(first_val)
second_val = repr(second_val)
operator= repr(operator)
answer= repr(answer)

file.write( first_val + operator + second_val + " = " + answer )

file.close



# try/ exception blocks for operators
#try/exception blocks for num 1
#repeat for num 2



