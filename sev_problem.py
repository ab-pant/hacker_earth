__author__ = 'abpant'
import math

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

target=open("sevProblemFile.txt",'w');
target.truncate();
set_size=int(raw_input()); #"Enter the number of sequences";
res=[0]*set_size
for i in range(0,set_size):
    sample_seq=map(float,raw_input().strip().split(" "));     #"Enter the values of a,H, THETA_MAX"
    angle=sample_seq[2];
    #print "A,H, theta", sample_seq[0],sample_seq[1],sample_seq[2];
    #print sample_seq[1]/sample_seq[0];
    #print angle,math.tan(math.radians(angle));
    #print math.tan(math.radians(angle))," --",(float(sample_seq[1])/float(sample_seq[0]));
    if math.tan(math.radians(angle))<(float(sample_seq[1])/float(sample_seq[0])):
        res[i]=int(math.ceil(sample_seq[1]-(sample_seq[0]*float(math.tan(math.radians(angle))*0.5))));
        #print "RES:",math.floor(sample_seq[1]-float(sample_seq[0]*math.tan(sample_seq[2]*math.pi/180)*0.5));
        '''print "FINAL RESULT",res[i];
    temp=str(math.tan(math.radians(angle)))[0:4];
    print temp;
    res[i]=math.tan(math.radians(angle))*sample_seq[0];
    print res[i];       int(math.ceil(sample_seq[1]-(sample_seq[0]*float(math.tan(sample_seq[2]*math.pi/180))*0.5)))'''

    else:
        #print "I am here!"
        res[i]=int(math.ceil(sample_seq[1]*(sample_seq[1]/(sample_seq[0]*2*math.tan(math.radians(angle))))));

print i;
print " \n".join(str(e) for e in res);
target.write( "\n".join(str(e) for e in res));
target.close();
