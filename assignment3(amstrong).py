# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:37:14 2020

@author: 2019
"""

num = input("enter a number: ")

if (num.isdigit() == True):
    top = 0
    for i in str(num):
        say = int(i) ** len(num)
        top += say
    if (top == int(num)):
        print("{} is an Armstrong number".format(num))
    else:
        print("{} is not an Armstrong number".format(num))
  
elif ("," in num) or ("." in num):
    print("Please enter an integer number")
elif ("-" in num):
    print("Please enter a positive number")
elif (num.isdigit() != True):
    print("Do not use any entries other than numeric values")
        


