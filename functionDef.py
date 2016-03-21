__author__ = 'abpant'

def isIn(x,y):
    presentOne=0;
    presentTwo=0;
    if x.find(y)>=0:
        print 'X has Y';
        presentOne=1;
        #return presentOne;
    else:
        print 'X doesnt have Y'

    if y.find(x)>=0:
        print 'Y has X';
        presentTwo=1;
        #return presentTwo;
    else:
        print 'Y doesnt have X'

    if x in y:
        print 'This is X in Y';

    if y in x:
        print 'This is Y in X';


isIn('awesome','awesome');
