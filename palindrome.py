def palindrome(num):
    num=str(num)
    for i in num:
        if num[::]==num[::-1]:
            return True
        else:
            return False
num=int(input())
print(palindrome(num))