s=input()
star=0
hash1=0
for i in s:
    if i=='*':
        star+=1
    elif i=='#':
        hash1+=1
if star>hash1:
    print("positive integer")
elif star<hash1:
    print("nagative integer")
else:
    print(0)