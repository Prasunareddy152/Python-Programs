num=int(input())
five=int((num-4)/5)

if ((num-5*five)%2)==0:
    one=2
else:
    one=1
two=(num-5*five-one)//2
print(five,two,one)