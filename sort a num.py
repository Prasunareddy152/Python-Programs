n=int(input())
sort=0
for i in range(9):
    count=0
    temp=n
    isPresent=False
    while(temp!=0):
        ld=temp%10
        if i==ld:
            isPresent=True
            count=count+1
for j in range(count):
    sort=(sort*10+i)
temp=temp//10 
    
print(sort)