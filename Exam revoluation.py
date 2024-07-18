def myfun(X,Y,N):
    ans=0
    for i in range(1,N):
        if arr[i]!=arr[i-1]:
            ans+=1
    return ans
N=int(input("No.of Students"))
K=int(input("No.of Revoluations"))
arr=list(map(int,input().split()))[:N]
for i in range(K):
    X=int(input("index position to update"))
    Y=int(input("Marks"))
    print(myfun(X,Y,N))