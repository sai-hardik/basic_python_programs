# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:30:03 2020

@author: babut
"""

def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x/y
                
print("select operation.")
print("1.add") 
print("2.substract") 
print("3.multiply") 
print("4.divide") 
choice = input("enter choice(1/2/3/4):")
num1 = int(input("enter num 1:"))
num2 = int(input("enter num 2:"))


if choice == '1':
  print(num1,"+",num2,"=", add(num1,num2))
  
elif choice == '2':
    print(num1,"-",num2,"=", substract(num1,num2))
elif choice == '3':  
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("invalid output")
    