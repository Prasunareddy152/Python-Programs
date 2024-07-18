n=int(input())
arr1=[]
even=[]
odd=[]
for i in range(0,n):
    a=int(input())
    arr1.append(a)
    if i%2==0:
        even.append(arr1[i])
    else:
        odd.append(arr1[i])
even=sorted(even)
odd=sorted(odd)
print(even)
print(odd)
print(even[-2]+odd[-2])

