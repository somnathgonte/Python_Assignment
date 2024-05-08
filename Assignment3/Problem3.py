iNo = int(input("Enter number:"))
count = 0
tmp=iNo
while iNo != 0:
    count=count+1
    iNo //=10
print("The number of digits in ",tmp,':',count)
