# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:38:23 2022

@author: tiara
"""

# Problem Number 1
def put_6(user):
    return int(user[0]) == 6 or int(user[-1]) == 6 #formula for this case
userInput = [int(x) for x in input("Input: ").split()] #userinput
print("Output:", put_6(userInput)) #output user
