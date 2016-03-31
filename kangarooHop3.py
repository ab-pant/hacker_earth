__author__ = 'abpant'

setSize=int(raw_input("Enter the number of sequences:"));  #"Enter the number of sequences:"
res=[0]*setSize;

for i in range(0, setSize):
    values=map(int,raw_input("Enter the values of A,B and M").strip().split(" "));   #"Enter the values of A,B and M"
    A=values[0];
    B=values[1];
    M=values[2];
    print values;
    print "A B M",A,B,M;

    count=(B-A)/M;
    rem1=(B-A+1)%M;     # is the range divisible
    rem2=B%M;           # is final value divisible
    if rem2<rem1:       # if remainder of range is less than remainder of last value then one more jump is possible
        count=count+1;

    res[i]=count;

print "\n".join(str(e) for e in res);


