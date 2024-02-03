# Lab5.py
# This program computes a person's car insurance based on their age and
# the number of tickets they have received. The table for insurance
# computation is given in Lab Assignment #3b.
# STEP 1: Prompt the user for the person's age, read it in, convert to number
inscost = 0
age = int(input("Please enter the Customer's age: "))
# STEP 2: Prompt the user for the person's number of tickets and read it in
tickets = int(input("Please enter the number of tickets: "))

if age < 21:
    inscost = 1750*tickets
    print("insurance costs you ", inscost)
elif age >= 21 and age <= 24:
    inscost = 1450*tickets
    print("insurance costs you ", inscost)
elif age > 24:
    inscost = 1200*tickets
    print("insurance costs you ", inscost)
else:
    print('Noooo....')
        
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
"""