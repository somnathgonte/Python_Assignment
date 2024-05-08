side1=int(input("Enter side1 :"))
side2=int(input("Enter side2 :"))
side3=int(input("Enter side3 :"))

if side1==side2 and side2==side3 :
    print('Equilateral Triangle')
elif side1!=side2 and side2 !=side3 :
    print('Scalene traingle')
else :
    print('Isosceles')
