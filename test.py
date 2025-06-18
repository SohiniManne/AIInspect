"""Prints the nth Fibonacci number divisible by m."""

n, m = 4, 3
a, b, count = 0, 1, 0

while True:
    a, b = b, a + b  # Compute next Fibonacci number

    if b % m == 0:  # Check if divisible by m
        count += 1

        if count == n:  # If nth multiple is found, print it
            print(b)
            break
