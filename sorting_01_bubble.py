def bubblesort(l,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
            
l=[]
n=int(input("enter the elements"))

for i in range(0,n):
    l.append(int(input()))
list1=bubblesort(l,n)
print(list1)

l.sort()
print("l",l)


