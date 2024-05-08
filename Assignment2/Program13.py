perc = float(input("Enter percentage :"))

if perc > 90:
    print('Grade : A')
elif 80 < perc <=90 :
    print("Grade : B")
elif 60 <= perc <=80 :
    print("Grade : C")
elif perc < 60 :
    print("Grade : D")
