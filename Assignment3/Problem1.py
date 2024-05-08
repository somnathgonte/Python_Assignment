no = int(input("Enter number"))
reverse = 0
tmp = no

while no != 0 :
    rem = no % 10
    reverse = (reverse * 10)+rem
    no = no // 10
print('Reverse of ',tmp,':',reverse)



