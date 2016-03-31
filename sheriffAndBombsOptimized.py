__author__ = 'abpant'

__author__ = 'abpant'

setSize=int(raw_input());  #"Enter set size:"
resList=[];
finalList=[];
x=[0]*setSize;y=[0]*setSize;r=[0]*setSize;
sumX=0;
sumY=0;

for i in range(0,setSize):
    cord=map(int,raw_input().strip().split(" "));   #"Enter the x, y and r values: "
    x[i]=cord[0];
    y[i]=cord[1];
    r[i]=cord[2];

sumOfAllXcoeff=0;
sumOfAllYcoeff=0;
sqrSumX=0;
sqrSumY=0;
sqrSumR=0;

for i in range(0,setSize):
    sumOfAllXcoeff=sumOfAllXcoeff+x[i];
    sumOfAllYcoeff=sumOfAllYcoeff+y[i];
    sqrSumX=sqrSumX+pow(x[i],2);
    sqrSumY=sqrSumY+pow(y[i],2);
    sqrSumR=sqrSumR+pow(r[i],2);

# mathematical equation ==> setSize*(x**2)+setSize*(y**2)-2*(sumOfAllXcoeff)*x-2*(sumOfAllYcoeff)*y+(sqrSumX+sqrSumY)=sqrSumR;
count=0;
#range should be min(0,min(x[i])-r[i]) and max(1000,max(x[i])-r[i])
for i in range(0,setSize):
    for p in range(0,1000):   #x[i]-r[i],x[i]+r[i]
        for q in range(0,1000):  #y[i]-r[i],y[i]+r[i]
            if ((setSize*(p**2))+(setSize*(q**2))-(2*(sumOfAllXcoeff)*p)-(2*(sumOfAllYcoeff)*q)+(sqrSumX+sqrSumY))<=sqrSumR:
                count=count+1;

print count;

