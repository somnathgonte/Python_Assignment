no = int(input("Enter nth term :"))
iNo= int(input("Enter number :"))
sum=0
term=0
for i in range(1,no+1) :
    term = term * 10 + iNo
    sum = sum + term
print(sum)
