iNo = int(input("Enter number :"))
sum = 0
tmp = iNo
while iNo != 0 :
    rem = iNo%10
    sum = sum+rem
    iNo //= 10
print("The sum of digit of",tmp,"is :",sum)
