__author__ = 'abpant'
# to get a comma seperated list of nubers and to find the sum
listOfNumbers=list();
inpStr=raw_input("PLease enter the comma seperated input list.");
listOfNumbers= inpStr.split(",");
print listOfNumbers

itr=0;
sum=0;

while itr<len(listOfNumbers):
    sum=sum+float(listOfNumbers[itr]);
    itr=itr+1;

print sum;

