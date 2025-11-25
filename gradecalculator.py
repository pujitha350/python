m=int(input("enter marks in maths:"))
s=int(input("enter marks in science:"))
e=int(input("enter marks in english:"))
total=m+s+e
print(f"Total marks:{total}")
print(f"average marks:{total/3}")
if total>=250:
    print("Grade A")
elif total>=200:
    print("Grade B")
else:
    print("Grade C")        