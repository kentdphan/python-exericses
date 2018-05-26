# File:        super.py
# Author:      Kent Phan
# Date:        5/26/2018
# Lab Section: ?
# UMBC email:  kphan1@umbc.edu
# Description: This program shows the proper layout of code in a Python file,
#              and greets the user with the name of the programmer.

def main():
    userInput = input("Are you a hero or a villain? ")
    
    if userInput.lower() == "villain":
        villainName = input("What is your name? ")
        print(villainName, "sounds pretty evil!")
    elif userInput.lower() == "hero":
        numOfSaved = int(input("How many people have you saved? "))
        if numOfSaved <= 10:
            print("Go on more patrols!")
        elif numOfSaved > 10 and numOfSaved < 100:
            print("Sounds like you're making a difference!")
        elif numOfSaved >= 100:
            print("Wow, great job saving the city!")
        
main()
