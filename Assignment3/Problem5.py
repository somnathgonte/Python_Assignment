iNo = int(input("Enter number :" ))
print("Divisors of",iNo,":",end=" ")
for i in range(iNo) :
    if(i != 0) :
        if(iNo%i==0) :
            print(i,sep=',',end=' ')
