#king movement in chess board
l=int(input("enter row of first peice:"))
m=int(input("enter column of first peice:"))
n=int(input("enter row of second peice:"))
o=int(input("enter column of second peice:"))
if n==l-1 and (m==o+1 or m==o-1):
    print("yes")
elif n==l-1 and (m==m or m==m-1 or m==m+1):
    print("yes")
elif n==l+1 and (m==m or m==m-1 or m==m+1):
    print("yes")
else:
    print("no")                 