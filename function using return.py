#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      kenzn
#
# Created:     06-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def addavg(a,b):
    s=a+b
    avg=s/2
    return s,avg
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    d=a*b
    return d
#for parameters u can also use other variables like x or y
#alos input need not be always below function it can be anywhere

a=int(input("a: "))
b=int(input("b: "))
sum,average=addavg(a,b)
subtraction=sub(a,b)
multiplication=mul(a,b)

print("sum, average:",(sum,average))
print("subtraction:", subtraction)
print("multiplication:",multiplication)