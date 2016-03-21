__author__ = 'abpant'
iterations=0;
epsilon=0.01;
k=24.0;
guess=k/2.0;
while abs(guess**2-k)>=epsilon:                  #run till the difference  betwenn the guess and sqr is very small
    guess=guess-(((guess**2)-k)/(2*guess));      # brackets must be taken care of
    iterations=iterations+1;
print 'Square root of ',k,'is about', guess;
print 'Iterations', iterations;


