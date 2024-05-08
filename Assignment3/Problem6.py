iNo = int(input("Enter number :"))
no = 1
print("Table of",iNo,':')
while no <= 10 :
    table = no * iNo
    tmp = no
    no = no+1
    print(iNo,'*',tmp,'=',table)
