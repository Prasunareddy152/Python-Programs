
N = int(input().strip())  # Number of books available
costs = list(map(int, input().strip().split()))  # Costs of the books
X = int(input().strip())  # Total number of credits
costs.sort()

num_books = 0
credits_left = X
for cost in costs:
    if credits_left >= cost:
        num_books += 1
        credits_left -= cost
    else:
        break
print(num_books)
