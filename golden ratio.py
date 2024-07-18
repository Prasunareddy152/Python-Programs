n=int(input())
distance=10
x,y=0,0
c='R'
for i in range(n):
    if c=='R':
        x=x+distance
        distance=distance+10
        c='U'
    elif c=='U':
        y=y+distance
        distance=distance+10
        c='L'
    elif c=='L':
        x=x-distance
        distance
        distance=distance+10
        c='D'
    elif c=='D':
        y=y-distance
        distance=distance+10
        c='A'
    elif c=='A':
        x=x+distance
        distance=distance+10
        c='R'
print(x,y)