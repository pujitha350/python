lst=[]
n=int(input("enter no of elements:"))
for i in range(n):
    val=int(input("enter value"))
    lst.append(val)
#add element into end of list
ele=int(input("enter element you want to add into list:"))
lst.append(ele)
print(lst)
element=int(input("enter element you want to insert"))
pos=int(input("enter position:"))
lst.insert(pos,element)
print(lst)
#slicing'
start=int(input("enter stating position:"))
end=int(input("enter last position"))
print(lst[start:end+1]) 
