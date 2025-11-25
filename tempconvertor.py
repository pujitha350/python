temp=int(input("enter temperature:"))
unit=input("enter unit of temperature(c or k or f)")
if(unit=="c"):
    print(f"temperature in fahrenheit:{(temp*9/5)+32}")
    print(f"temperature in kelvin:{temp+273.15}")
elif(unit=="f"):
    print(f"temperature in celsius:{(temp-32)*5/9}") 
    print(f"temperature in kelvin:{temp+459.67}*5/9")
else:
    print(f"temperature in celsius:{temp-273.15}")
    print(f"temperature in fahrenheit:{(temp-273.15)*9/5+32}")       