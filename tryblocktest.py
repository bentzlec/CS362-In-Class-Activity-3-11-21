import unittest

def add(x, y):
    return (x + y)

def sub(x, y):
    return (x - y)

def mult(x, y):
    return (x * y)

def div(x, y):
    return (x / y)

#Alternative testing to unit testing: use try / except block

try:
    add(68, 97)

    sub(97, 23)

    mult(5, 5)

    div(90, 9)

    div(3, 0)
except ZeroDivisionError:
    print ("Divide by zero error!")
except ValueError:
    print ("Value error!")
except OverflowError:
    print ("Overflow error!")

