# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:02:09 2021

@author: o
"""


def XtimesY(x:float,y:float) -> float:
    if x == 0:
        return 0
    return exponent(y*ln(x))


def exponent(x:float) -> float: 
    ans = 0.0
    index = 0
    n = 50
    for index in range (n):
        numerator = 1
        denomator = 1
        print (index)
        for i in range (index):
            numerator = numerator * x
            denomator = denomator * index
        ans += numerator/denomator
        index = index + 1
    return ans


def ln(x:float)->float:
    ans = x - 1.0
    index = 1
    while (index <= x):
        ans = ans + 2*((x-exponent(ans))/(x+exponent(ans)))
    return ans


def sqrt(x:float,y:float) -> float:
    if x == 0:
        return 0
    return XtimesY(x, 1/y)


def calculate(x:float) -> float:
    if x == 0:
        return 0
    return exponent(x)*XtimesY(7, x)*(1/x)*sqrt(x, x)

def main():
    num = int(input("Enter a number: "))
    print(calculate(num))