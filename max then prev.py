def myfun():
    n=int(input())
    arr=[]

    for i in range(n):
        element=int(input())
        arr.append(element)
    ans=0
    max1=arr[0]
    for j in arr:
        if j>max1:
            ans+=1
    return ans
print(myfun()+1)