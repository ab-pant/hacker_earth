__author__ = 'abpant'

setSize=int(raw_input("Enter the number of sequences:"));  #"Enter the number of sequences:"
res=[0]*setSize;
def findMultiple(start,stop,growth):
    count=0;
    temp=start;
       # its a multiple
    if stop-start>growth:
        while(temp<=stop):
            print "TEMP:", temp;
            temp=temp+growth;
            count=count+1;
        if stop%growth==0:
            return count;
        else:
            return count+1;
    elif stop-start==growth:
        return 1;
    else:
        return 0;


for i in range(0, setSize):
    values=map(int,raw_input("Enter the values of A,B and M").strip().split(" "));   #"Enter the values of A,B and M"
    A=values[0];
    B=values[1];
    M=values[2];
    print values;
    print "A B M",A,B,M;
    res[i]=findMultiple(A,B,M);

print "\n".join(str(e) for e in res);


