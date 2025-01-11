def fib_recursion(n):
    if n == 1:
        return 1
    else:
        return n * fib_recursion(n-1)
