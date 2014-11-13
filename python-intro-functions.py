    
    #
    # Example file for working with functions
    #
    
#define a function


def func1():
    print "I am a function"   
    
    
func1() 
print func1  # Will print the object location in memory. all funct are objects on python
print func1()



#function with a variable number of arguments

def multi_add(*args): #* aloud as many arguments
    result = 0;
    for i in args:
        result = result + i;
    return result


print multi_add(2,3,1,10)

def sum(a,b):
    return a + b

a = sum(3,4)


import math
import random

def volume(radius, height):
  pi = 3.14159
  return pi * radius ** 2 * height

print "volume of cylinder with radius", 1, "and height 2 is", volume(1,2)
print "volume of cylinder with radius", 2, "and height 1 is", volume(2,1)


print volume

def volume2(height, radius):
    return height * math.pi * (radius ** 2)

a = valume2(2,4)

print a
    



from math import pi


