n=int(input())
largest=0
while (n!=0):
    ld=n%10
    if ld>largest:
        largest=ld
    n=n//10
print(largest)