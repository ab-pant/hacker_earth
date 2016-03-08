__author__ = 'abpant'

# to caluclate the largest odd number for 10 numbers entered

itr=10
numbers=list();
while(itr!=0):
    numbers.append(int(raw_input("Enter a number :")))
    itr=itr-1

#print numbers
itr=0;
oddNumbers=list();
while(itr<10):
    if (numbers[itr]%2 !=0):
        oddNumbers.append(numbers[itr]);
    itr=itr+1;

if len(oddNumbers)==0:
    print 'No Odd numbers entered';

itr =0;
itr2=len(oddNumbers);
temp=oddNumbers[0];
while(itr<len(oddNumbers)):
    #while(itr2!=0)
    if temp<oddNumbers[itr]:
        temp=oddNumbers[itr];
    itr=itr+1;

print temp;