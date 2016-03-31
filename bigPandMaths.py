__author__ = 'abpant'
import time;
values=map(int,raw_input("Enter the values of num1 and num2").strip().split(" "));

start_time=time.time();
num1=str(values[0]);
num2=str(values[1]);
print num1,num2;

highestNum1=num1.replace('5','6'); #replace 5 with 6
highestNum2=num2.replace('5','6');

lowestNum1=num1.replace('6','5'); #replace 6 with 5
lowestNum2=num2.replace('6','5');

print int(highestNum1)+int(highestNum2),int(lowestNum1)+int(lowestNum2);

print "Elapsed time:", time.time()-start_time;