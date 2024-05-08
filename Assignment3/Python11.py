start = int(input("Enter start point"))
stop = int(input("Enter end point:"))

for i in range(start,stop+1):
    if(i%2!=0):
        print(i)
