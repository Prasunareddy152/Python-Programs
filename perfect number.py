n=int(input())
sum=0
for num in range(1,n):
    if n%num==0:
        sum=sum+num
if sum==n:
    print("perfect number")
else:
    print("Not a perfect number")
    