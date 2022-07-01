def binarysearch(a,l,h,num):
    while l<=h:
        m=l+(h-l)//2
        if a[m]==num:
            return m
        elif a[m]<num:
            l=m+1
        else:
            h=m-1
    return -1
        
    
a=[]
n=int(input("enter the elements"))
num=int(input("enter the element which we want to search"))

for i in range(0,n):
    a.append(int(input()))
result=binarysearch(a,0,n-1,num)

if result!=-1:
    print("element is present at index",result)
else:
    print("element is not present in list")

