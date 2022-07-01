def merge(a, mid, low, high, b):
    i = low
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if a[i] < a[j]:
            b[k] = a[i]
            i = i+1
            k = k+1
        else:
            b[k] = a[j]
            j = j+1
            k = k+1
    while i <= mid:
        b[k] = a[i]
        i = i+1
        k = k+1
    while j <= high:
        b[k] = a[j]
        k = k+1
        j = j+1
    for i in range(low, high+1):
        a[i] = b[i]


def mergesort(a, low, high, b):
    if low < high:
        mid = (low + high) // 2
        mergesort(a, low, mid, b)
        mergesort(a, mid + 1, high, b)
        merge(a, mid, low, high, b)


a = []
n = int(input("enter the elements"))
b = [0]*n

for i in range(0, n):
    a.append(int(input()))

print("function")
mergesort(a, 0, n-1, b)

print(a)
