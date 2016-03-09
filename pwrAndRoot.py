__author__ = 'abpant'
import math

var = int(raw_input("Enter a number to check:"));
itr=0;
temp=0;

while(itr<var):
    sqr=math.pow(itr,2);
    cube=math.pow(itr,3);
    fourth=math.pow(itr,4);
    fifth=math.pow(itr,5);
    if (sqr==var):
        temp=1;
        break;
    if (cube==var):
        temp=2;
        break;
    if (fourth==var):
        temp=3;
        break;
    if (fifth==var):
        temp=4;
        break;
    if (itr==var):
        temp=5;
        break;
    itr=itr+1;

print temp;