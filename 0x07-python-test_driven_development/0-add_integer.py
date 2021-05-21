#!/usr/bin/python3
""" 
My calculation module
a is the first integer
b is the second integer
"""
def add_integer(a, b=98):
    """ 'add_integer(a, b)' function that adds two integers/floats
        a is the first integer
        b is the second integer """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))