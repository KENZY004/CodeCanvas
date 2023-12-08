#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     21-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ch=input("ch: ")
if(ch.isalpha()):
    print("alphabet")
elif(ch.isnumeric()): #here isdigit or isnumeric can be used
    print("digit")
else:
    print("neither alphabet nor digit")