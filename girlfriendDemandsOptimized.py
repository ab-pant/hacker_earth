__author__ = 'abpant'
import time


inStr=str(raw_input("Enter the Demand string"));
setSize=int(raw_input("Enter the number of sets").strip());
listOfSequence=();
answer=[""]*setSize;

def getPosition(flag_1,flag_2,wrkSeq,length):
    res=[];
    if flag_1==1:
        if wrkSeq[0]%length==0:     # its a mutliple  -- ensure that wrkSeq never has value of 0
            if wrkSeq[0]==length:
                res.append(0);
            else:
                res.append(length);     # the last character eg if length is 7 and 14 is wrkSeq[0] then position is last character which is 7
                #res.append(wrkSeq[0]/length);
        else:
            res.append(wrkSeq[0]%length);   #for all non multiple cases rem is the position  .. cyclic function
    else:
        res.append(wrkSeq[0]);

    if flag_2==1:
        if wrkSeq[1]%length==0:     # its a mutliple  -- ensure that wrkSeq never has value of 0
            if wrkSeq[1]==length:
                res.append(0);
            else:
                print "You are here";
                res.append(length);     # the last character eg if length is 7 and 14 is wrkSeq[0] then position is last character which is 7
                #res.append(wrkSeq[0]/length);
        else:
            res.append(wrkSeq[1]%length);   #for all non multiple cases rem is the position  .. cyclic function
    else:
        res.append(wrkSeq[1]);

    print res;
    return res;

def actPos(x): return x-1;

for i in range(1,setSize+1):
    #initializing
    rem1,rem2=0,0;
    flag_1=0;
    flag_2=0;


    listOfSequence=raw_input("Enter sequence "+str(i)+" : ");
    mapped=map(int,listOfSequence.strip().split(" "));
    print "Mapped:", mapped;
    wrkSeq=list(map(actPos,mapped));
    print wrkSeq;
    length=len(inStr);
    print "length:", length;

    if wrkSeq[0]>=length:
        flag_1=1;
    if wrkSeq[1]>=length:
        flag_2=1;
    print flag_1,flag_2;

    #start_time = time.time();
    positions=getPosition(flag_1,flag_2,wrkSeq,length);
    #print "--- %s seconds ---" , (time.time() - start_time);

    print "Instr values are: ", inStr[positions[0]],inStr[positions[1]];
    print "Length of answer", len(answer);

    if inStr[positions[0]]==inStr[positions[1]]:
        answer[i-1]="Yes";
    else:
        answer[i-1]="No";

#print answer;
print "\n".join(str(e) for e in answer);