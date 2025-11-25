num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
op=input("enter an arthimetic operator")
if op=="+":
    print("adittion of two numbers is:",num1+num2)
elif op=="-":
    print("subtraction of two numbers:",num1-num2)
elif op=="*":
    print("multiplication of two numbers:",num1*num2)
elif op=="/":
    print("division of two numbers:",num1/num2)
else:
    print("invalid operator")