# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:06:23 2022

@author: saiki
"""

num1 = float(input("enter number1"))
op = input("enter oper")
num2 = float(input("enter number2"))

if op == "+" :
    print (num1+num2)
elif op == "-" :
    print (num1-num2)
elif op == "*":
    print (num1*num2)
elif op == "/":
    print (num1/num2)


NEW CODE 

dict = {'a': 100, 'b': 200, 'c': 300}
sum=0

for i in dict :
    sum=sum+dict[i]
print (sum)    
