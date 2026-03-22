def evenorodd(n):
    if(n%2==0):
        return True;
    else:
        return False;
number=int(input("enter any number:"))
if(evenorodd(number)==True):
    print(f"{number} is an even number")
else:
    print(f"{number} is a  odd number")
