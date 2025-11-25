def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(f"a:{a}andb:{b}")
a=int(input("enter a value:"))
b=int(input("enter b value:"))
swap(a,b)