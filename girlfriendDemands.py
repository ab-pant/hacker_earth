__author__ = 'abpant'

inStr=str(" ")+str(raw_input("Enter the Demand string"));
setSize=int(raw_input("Enter the number of sets"));
listOfSequence=();

def getPosition(flag_1,flag_2,setSize,wrkSeq,length):
    res=[];
    if flag_1==1:
        if wrkSeq[0]%length==0:     # its a mutliple  -- ensure that wrkSeq never has value of 0
            res.append(length);     # the last character eg if length is 7 and 14 is wrkSeq[0] then position is last character which is 7
            #res.append(wrkSeq[0]/length);
        else:
            res.append(wrkSeq[0]%length);   #for all non multiple cases rem is the position  .. cyclic function
    else:
        res.append(wrkSeq[0]);

    if flag_2==1:
        if wrkSeq[1]%length==0:     # its a mutliple  -- ensure that wrkSeq never has value of 0
            res.append(length);     # the last character eg if length is 7 and 14 is wrkSeq[0] then position is last character which is 7
            #res.append(wrkSeq[0]/length);
        else:
            res.append(wrkSeq[1]%length);   #for all non multiple cases rem is the position  .. cyclic function
    else:
        res.append(wrkSeq[1]);

    print res;
    return res;


for i in range(1,setSize+1):
    #initializing
    rem1,rem2=0,0;
    flag_1=0;
    flag_2=0

    listOfSequence=raw_input("Enter sequence "+str(i)+" : ");
    wrkSeq=map(int,listOfSequence.split(" "));
    print wrkSeq;
    length=len(inStr);
    print "length:", length;

    if wrkSeq[0]>=length:
        flag_1=1;
    if wrkSeq[1]>=length:
        flag_2=1;
    print flag_1,flag_2;

    positions=getPosition(flag_1,flag_2,setSize,wrkSeq,length);
    print "Instr values are: ", inStr[positions[0]],inStr[positions[1]];
    str1=inStr[positions[0]];
    str2=inStr[positions[1]];
    if str1==str2:
        print "Yes";
    else:
        print "No";