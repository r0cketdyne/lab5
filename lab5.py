# Lab5.py
# This program computes a person's car insurance based on their age and
# the number of tickets they have received. The table for insurance
# computation is given in Lab Assignment #3b.
# STEP 1: Prompt the user for the person's age, read it in, convert to number
inscost = 0
currency = '$'
age = int(input("Please enter the Customer's age: "))
# STEP 2: Prompt the user for the person's number of tickets and read it in
tickets = int(input("Please enter the number of tickets: "))

if age < 21:
    inscost = 1750*tickets
elif age >= 21 and age <= 24:
    inscost = 1450*tickets
elif age > 24:
    inscost = 1200*tickets
else:
    print('Noooo....')
        
    
print("\nGiven the data you've put in it's been determined that the customer is indeed", age, "years old.")
print("\nI've also calculated their computed insurance cost to be", currency + str(inscost))
# STEP 3: Compute the insurance cost based on the table given in the assignment
# Step 4: Print out the resulting insurance cost message



"""
RULE 1
If Person's Age Is
Less than 21 
$1500 + $250 x number of tickets

RULE 2
If Person's Age Is
From 21 through 24
$1200 + $250 x number of tickets


RULE 3
If Person's Age is
25 or older
$1000 + $200 x number of tickets

BRINGING IT ALL TOGETHER
Print a message explaining the person's age and number of tickets on one line, and then print a message
on the next line showing the computed insurance cost. Include a $ sign before the cost when you print it
out!
"""