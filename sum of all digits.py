'''num=int(input())
sum=0
for i in range(num):
    if num!=0:
        ld=num%10
        sum=sum+ld
        num=num//10
print(sum)'''


num=int(input())
sum=0
while num!=0:
    ld=num%10
    sum=sum+ld
    num=num//10
print(sum)
