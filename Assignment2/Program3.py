marks1=float(input("Enter marks1 :"))
marks2=float(input("Enter marks2 :"))
marks3=float(input("Enter marks3 :"))
marks4=float(input("Enter marks4 :"))
marks5=float(input("Enter marks5 :"))

sum = marks1+marks2+marks3+marks4+marks5
avg = sum/5
print(avg)

if avg < 35 :
    print('Fail')
elif avg <= 60 :
    print('Second class')
elif avg <= 75 :
    print('First class')
else :
    print('Distinction')
