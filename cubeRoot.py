__author__ = 'abpant'

x=int(raw_input("Enter the number whose cube root you wish to find:"));
ans=0;
while(ans**3<abs(x)):
    #print 'Value of decrementing function is ', \
    abs(x) - ans**3;
    #ans=ans;
    ans=ans+1;

if ans**3!=abs(x):
    print "Not a perfect number";

if x<0:
    ans=-ans;

print "The cube root is ", ans, "for", x;
