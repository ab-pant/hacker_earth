#this is my first program with git and github basics
#Finger ex 1 : Largest odd number of three numbers x, y and z

import sys
print (sys.version)
x=int(raw_input("Enter value for x:"))
y=int(raw_input("Enter value for y:"))
z=int(raw_input("Enter value for z:"))

if int(x)%2 == 0:

    print 'Please enter an odd number'
    x=raw_input("Please enter value of x:")

else:
    print "Passed"

if int(y)%2 == 0:
    print 'Please enter an odd number'
    x=raw_input("Please enter value of y:")

else:
    print "Passed"

if int(z)%2 == 0:
    print 'Please enter an odd number'
    x=raw_input("Please enter value of z:")

else:
    print 'Passed'

if x>y and x>y:
    print 'Largest is x'
elif y>x and y>z:
    print 'Largest is y'
else:
    print 'Largest is z'

