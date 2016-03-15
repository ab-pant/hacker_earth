__author__ = 'abpant'

epsilon=0;
k=24.0;
guess=k/2.0;
while guess**2-k>=epsilon:                  #run till the difference  betwenn the guess and sqr is very small
    guess=guess-((guess**2-k)/2*guess);
print 'Square root of ',k,'is about', guess;

