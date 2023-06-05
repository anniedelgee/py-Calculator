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
to read all the equations from a new txt file (the user should add the name of the txt file as an input) --read()
    AND
print out all the equations together with the results.

use defensive coding to ensure that the program does not crash if the file does not exist 
and that the user is prompted agaian to enter the name of the file.

'''

import math

# get user input- numbers
print("This application is a calculator that will take two values and an operator ( +, -, *, / ), compose an equation and return the solution.")

#get user to decide what function they want to perfrom

def intro():
    user_choice = input("Enter 'Calc' to do a calculation or 'File' to read the results from a text file: ").lower()
    if (user_choice == "calc"):
        print("You chose calculator, now you'll need to enter your values and operator")
        calculator()
    elif (user_choice == "file"):
        try:
            user_file = open(input("Enter the name of your text file here: "), "r")
            file_name = user_file.read()
            print(file_name)
        except FileNotFoundError as ERROR:
            print("The file you are trying to open does not exist, please try agin")
            print(ERROR)
        


# part2: read-file function
# take input from user to create new text file and print out all equation wiht resuts
#create file using user input

#Calculator function   

def calculator():
#create text file
    file = open("calculator.txt", "w")

    # first number
    try: 
        first_val= float(input("Please enter your first value: "))
        # second number
        second_val= float(input("Please enter your second value: "))
    except ValueError as ERROR:
        print("Invalid value input \n")
        print(ERROR)
        print("\nTry Again")
        return

    # operator input
    operator= input("What operation are you carrying out? Enter calculation symbol: ")

    # create equations
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
        try:
            answer= (first_val / second_val)
            print(" The quotient of " + str(first_val) + " and " + str(second_val) + " is " + str(round(answer, 2)))
        except ZeroDivisionError as ERROR:
            print("Invalid equation! Cannot divide by Zero\n")
            print(ERROR)
            print("\nTry again!")
            return
    else:
        print("please enter valid numerical values and arithmetic operators.")
        return

# convert values to representations to write to file. 

    first_val= repr(first_val)
    second_val = repr(second_val)
    operator= repr(operator)
    answer= repr(answer)
    file.write( first_val + operator + second_val + " = " + answer )
    file.close()


while True:
    intro()
'''
#try:
#create text file
#except FileNotFoundError as ERROR:
print("The file that you are trying to open does not exist")
print(ERROR)
print("\n Try Again!")
return
'''


