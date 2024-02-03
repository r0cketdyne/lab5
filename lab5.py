# Lab Exercise 5: lab5.py
# 2/3/24
# Matthew Stephenson
# This program computes a person's car insurance based on their age and
# the number of tickets they have received.
inscost = 0
#initialized a var where I intend to reassign to a particular int as denoted by supplied table at canvas doc
currency = '$'
#added a currency ticker here to contat at instcost var to log to the standard i/o 
age = int(input("Please enter the Customer's age: "))
#at the wireframe / blueprint of this code supplied in canvas it was not condensed. made two lines one 
tickets = int(input("Please enter the number of tickets: "))
#did the same thing here as I did at line 11; there were two lines at this particular expression at the code wireframe supplied in canvas

if age < 21:
    inscost = 1500 + 250 * tickets
#imported logic from table at canvas document
elif 21 <= age <= 24:
    inscost = 1200 + 250 * tickets
#imported logic from table at canvas document
elif age >= 25:
    inscost = 1000 + 200 * tickets
#imported logic from table at canvas document
else:
#imported logic from table at canvas document. please see comments below the else statement
    print('Noooo....')
#if none of the conditionals at the elif statements above are met this executes implying a program failure.
        
    
print("\nGiven the data you've put in it's been determined that the customer is indeed", age, "years old.")
print("\nI've also calculated their computed insurance cost to be", currency + str(inscost))
#Would have used the newline feature but canvas docs explicitly stated to print twice

"""
TABLE CONVERSION / LOGIC
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