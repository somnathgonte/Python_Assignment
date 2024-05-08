unit=int(input("Enter unit :"))

if unit <= 100 :
    print("No charge")
elif 200 >= unit > 100 :
    print('Price :',unit*5)
elif unit > 200 :
    print("Price :",unit*10)
    
if unit > 0 and unit <= 100 :
    print 
elif unit > 100 and unit <=200 :
    charges = (unit - 100)*5
    print(charges)
else :
    cherges = (unit - 200)*10+(500)