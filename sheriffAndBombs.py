__author__ = 'abpant'

setSize=int(raw_input());  #"Enter set size:"
resList=[];
finalList=[];
for i in range(0,setSize):
    cord=map(int,raw_input().strip().split(" "));   #"Enter the x, y and r values: "
    x=cord[0];
    y=cord[1];
    r=cord[2];
    tempList=[];
    rSqr=r**2;
    #ideally 0 to 10000 for x and y
    #to optimize we reduce the window
    for l in range(x-r,x+r):
        for m in range(y-r,y+r):
            if (pow(l-x,2)+pow(m-y,2))<=rSqr:
                tempList.append(str(l)+str(" ")+str(m));
                #print tempList;
    #print tempList;
    resList.append(tempList);

#print resList;

# We will now compare the 1st list with all others and find the common values.
# Only common values survive in the check
for i in range(0,len(resList[0])):
    for j in range(1,setSize):
        for k in range(0,len(resList[j])):      #print resList[0][0];
            if resList[0][i]==resList[j][k]:
                finalList.append(resList[0][i]);

print len(finalList);

