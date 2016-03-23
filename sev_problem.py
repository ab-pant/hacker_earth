__author__ = 'abpant'
import math

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

set_size=int(raw_input("Enter the number of sequences")); #"Enter number of sequences you want:";
res=[0]*set_size
for i in range(0,set_size):
    sample_seq=map(int,raw_input("Enter the values of a,H, THETA_MAX").split(" "));
    angle=sample_seq[2];
    print angle,math.tan(math.radians(angle));
    temp=math.tan(math.radians(angle));

    res[i]=math.tan(math.radians(angle))*sample_seq[0];
    print res[i];

print " ".join(str(e) for e in res);
print temp/1000;
new_temp=temp*1000;
print new_temp;
print new_campus/1000;
print
