v=int(input())
w=int(input())
if w<=2 or w<v or w%2==1:
    print("Invalid input")
else:
    x=(4*v-w)/2
print(int(x),int(v-x))