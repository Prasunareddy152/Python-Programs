def myfun(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
nums=list(map(int,input().split()))
target=int(input())
print(myfun(nums,target))