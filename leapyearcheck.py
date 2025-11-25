a=int(input("enter a year:"))
if(a%100==0 and a%400!=0):
    print(f"{a} is a not leap year")
elif(a%4==0):
    print(f"{a} is a leap year")
else:
    print(f"{a} is not leap year")    
