#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     19-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calculatetax(salary, percent=20):
    taxAmount=salary*percent/100
    print(taxAmount)
salary=float(input("salary: "))
percent=float(input("tax percentage: "))

calculatetax(salary)
calculatetax(salary,percent)