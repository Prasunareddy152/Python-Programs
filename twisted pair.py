n=int(input())
isPrime=True
for i in range(2,n+1):
    if n%i==0:
        isPrime=False
        print("not a twisted pair")
        break
    if isPrime==True:
        rev=0
        while(n!=0):
            ld=n%10
            rev=rev*10+ld
            n=n/10
for j in range(2,n+1):
    if n%j==0:
        print("Not a twisted pair")
    else:
        print("twisted pair")