a=input()
ans=""
for i in a:
    if ord(i)<=ord('v'):
        ans+=chr(ord(i)+5)
    else:
        ans+=chr(ord(i)-ord('v')+ord('a'))
print(ans)