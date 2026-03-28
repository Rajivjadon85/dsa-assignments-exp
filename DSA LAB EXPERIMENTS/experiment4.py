# EXPERIMENT4-FIBONACCI SERIES

# Memoized
call_count_memo = 0
memo = {}

def fibonacci_memo(n):
    global call_count_memo
    call_count_memo += 1

    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)

    return memo[n]


n=int(input("enter no:"))

call_count_memo = 0
memo.clear()

for i in range(n):
    print(fibonacci_memo(i), end=" ")

print("\n Total function calls (Memoized):", call_count_memo)

# Naive
call_count = 0

def fibonacci_naive(n):
    global call_count
    call_count += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)


n = int(input("Enter number of terms: "))

call_count = 0
for i in range(n):
    print(fibonacci_naive(i), end=" ")

print("\nTotal function calls:", call_count)