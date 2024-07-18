def myfun(S):
    result=0
    prev=0
    roman=roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for char in reversed(S):
        value=roman[char]
        if value<prev:
            result-=value
        else:
            result+=value
        prev=value
    return result
S=input()
print(myfun(S))
            
            
        