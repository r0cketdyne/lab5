#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:14:18 2024

@author: stephenson
"""
#NESTED CONTROL STRUCT
#seems like cell and tabular problems at grids can be broken down into decision trees
#this is very interesting.
tax_multiplier = 0
#set empty var for taxrate multiplier. need to initiate it
user_sal = int(input("mf what is your salary...200K Tc I hope"))
user_stat = str(input("are you married? hope not. seems like a terrible deal.\n if so, type married and press enter"))
#first prompt user for salary and filing status
if  user_sal >= 100000 and user_stat == 'married':
    tax_multiplier = 0.20
    user_sal += 100000*tax_multiplier
    print(user_sal)
elif user_sal >= 100000 and user_stat != 'married':
    tax_multiplier = 0.18
    user_sal += 10000*tax_multiplier
elif user_sal >= 50000 and user_stat == 'married':
    tax_multiplier = 0.18
    user_sal += 50000*tax_multiplier
    print(user_sal)
elif user_sal >= 50000 and user_stat != 'married':
    tax_multiplier = 0.15
    user_sal += 50000*tax_multiplier
else:
    user_sal += user_sal*0.10
    print(user_sal)