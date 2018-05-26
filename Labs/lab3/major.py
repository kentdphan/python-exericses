# File:        major.py
# Author:      Kent Phan
# Date:        5/26/2018
# Lab Section: ?
# UMBC email:  kphan1@umbc.edu
# Description: This program shows the proper layout of code in a Python file,
#              and greets the user with the name of the programmer.

def main():
    usersMajor = input("Please enter your major: ")
    
    # Converts the user's input to uppercase
    usersMajorUpper = usersMajor.upper() 	    

    if usersMajorUpper == "CMSC" or usersMajorUpper == "CMPE":
        print("You need to earn at least a B for CMSC 201 to count.")
    else:
        print("You need to earn at least a C for CMSC 201 to count.")  

main()
