costPrice= int(input("Enter cost price :"))

if costPrice > 100000 :
    print("Tax = 15%")
elif 50000 < costPrice <= 100000 :
    print("Tax = 10%")
elif costPrice <= 50000 :
    print("Tax = 5%")
