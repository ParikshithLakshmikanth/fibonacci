def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# To get the Fibonacci series up to the nth term
n = int(input("Enter any number: "))
for i in range(1, n + 1):
    print(fibonacci(i))
