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

a=int(input("a: "))
b=int(input("b: "))
s,avg=addavg(a,b)
sub=sub(a,b)
mul=mul(a,b)

print("sum, average:",(s,avg))
print("subtraction:", sub)
print("multiplication:",mul)
