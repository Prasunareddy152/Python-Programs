n=int(input())
list=[]
ans=0
c=0
for _ in range(n):
    a=int(input())
    if a==1:
        ans+=c
    else:
        c+=1
print(ans)
        
                
    