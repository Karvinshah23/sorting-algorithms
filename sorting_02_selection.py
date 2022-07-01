def selectionsort(l,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if l[i]>l[j]:
                temp=l[j]
                l[j]=l[i]
                l[i]=temp
l=[]
n=int(input("enter the elements"))

for i in range(0,n):
    l.append(int(input()))
selectionsort(l,n)
print(l)