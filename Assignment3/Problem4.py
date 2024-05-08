iNo = int(input("Enter number :"))
tmp = iNo
reverse = 0

while iNo != 0 :
    rem = iNo % 10
    reverse = (reverse * 10)+rem
    iNo //= 10
if(tmp==reverse) :
    print(tmp,"is a palindrome number")
else :
    print(tmp,"is a not palindrome number")
    
