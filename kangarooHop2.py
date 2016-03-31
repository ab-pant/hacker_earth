__author__ = 'abpant'
import time;

setSize=int(raw_input());  #"Enter the number of sequences:"
res=[0]*setSize;
def findMultiples(start,stop,growth):
    count=0;
    for i in range(start,stop+1):
        if i%growth==0:
            count=count+1;
    return count;

start_time=time.time();
for i in range(0, setSize):
    values=map(int,raw_input().strip().split(" "));   #"Enter the values of A,B and M"
    A=values[0];
    B=values[1];
    M=values[2];

    res[i]=findMultiples(A,B,M);

print "\n".join(str(e) for e in res);
print "Elapsed time :", time.time()-start_time;


