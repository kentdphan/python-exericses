# File:        major.py
# Author:      Kent Phan
# Date:        5/26/2018
# Lab Section: ?
# UMBC email:  kphan1@umbc.edu
# Description: This program shows the proper layout of code in a Python file,
#              and greets the user with the name of the programmer.

def main():
    numOfRevenues = int(input("How many revenues would you like to enter? "))

    while numOfRevenues <= 0:
        print("You must enter a number greater than zero.")
        numOfRevenues = int(input("How many revenues would you like to enter? "))
    
    minRevenue = 0
    maxRevenue = 0    
    count = 1
    while count <= numOfRevenues:
        revenueAmount = float(input("Enter a revenue: "))
        if minRevenue > revenueAmount:
            minRevenue = revenueAmount
        elif maxRevenue < revenueAmount:
            maxRevenue = revenueAmount
        # Initalizes the current revenue value to min and max revenues
	elif minRevenue == 0 or maxRevenue == 0:
            minRevenue = revenueAmount
            maxRevenue = revenueAmount
        count += 1

    print("The minimum revenue entered was ", minRevenue)
    print("The maximum revenue entered was ", maxRevenue)
main()
