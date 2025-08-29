#!/usr/bin/env python3

def print_fibonacci(n):
    """Prints the Fibonacci sequence up to length n."""
    if n <= 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    elif n == 2:
        print([0, 1])
        return

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print(fib)
