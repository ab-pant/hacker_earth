__author__ = 'abpant'
import time;
start_time=time.time();
values=map(int,raw_input("Enter the Steps sequence").strip().split(" "));
stepSize=values[0];
backStep=values[1];
finalValue=values[2];
restingPlace=0;
netStep=stepSize-backStep;
count=0;
countOpt=0;

countOpt=(finalValue)/(netStep);
print "Count opt, netstep,stepsize",countOpt,netStep,stepSize;
checkVal=(countOpt)*netStep+stepSize;
print checkVal;
if checkVal>=finalValue:
    print countOpt+1;
else:
    print countOpt;

'''
This is a working solution but slow in approach
while 1:
    restingPlace=restingPlace+(netStep);
    count=count+1;
    if restingPlace+stepSize>=finalValue:
        count=count+1;
        break;

print count;
'''
print "Elapsed time :", time.time()-start_time;