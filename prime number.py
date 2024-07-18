
num=int(input())
isprime=True

for i in range(2,num):
    if num%i==0:
        isprime=False
if isprime==True and num!=0 and num!=1:
    print("Prime Number")
else:
    print("Not Prime number")
    

    