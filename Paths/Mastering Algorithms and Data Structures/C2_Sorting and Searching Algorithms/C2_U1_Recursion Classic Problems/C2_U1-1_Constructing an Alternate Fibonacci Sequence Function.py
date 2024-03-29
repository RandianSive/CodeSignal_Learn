def alt_fib(n,computed={0: 2, 1: 3}):
    # implement this

    if n not in computed:
        computed[n] = alt_fib(n - 1, computed) + alt_fib(n - 2, computed)
    return computed[n]
    
    


# Test the function with some values
print(alt_fib(0))  # Expected output: 2
print(alt_fib(1))  # Expected output: 3
print(alt_fib(2))  # Expected output: 5
print(alt_fib(3))  # Expected output: 8
print(alt_fib(4))  # Expected output: 13
print(alt_fib(5))  # Expected output: 21