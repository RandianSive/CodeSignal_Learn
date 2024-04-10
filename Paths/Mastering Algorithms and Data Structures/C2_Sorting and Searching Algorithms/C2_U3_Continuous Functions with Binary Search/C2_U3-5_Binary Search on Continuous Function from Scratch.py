# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math

# Define a continuous function 'f'
def f(x):
    return x**3 - 5 * x**2 + 5

# Binary Search Function on Continuous Space
def binary_search_continuous(func, target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if func(mid) < target:
            left = mid
        else:
            right = mid
    return (left + right) / 2

# Define precision, target value, and interval bounds
epsilon = 1e-6  # precision
target = 0      # target value for f(x)
start = 2       # starting point of the interval
end = 5         # ending point of the interval

# Implement the binary search function and print out the value of 'x' for which f(x) is approximately 0
result = binary_search_continuous(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 within the interval [", start, ",", end, "] is:", result)



'''
# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math

# Define a continuous function 'f'
def f(x):
    return x**3 - 5 * x**2 + 5

# TODO: Write the Binary Search Function that performs the search on the continuous function in the interval [2, 5]

# TODO: Define precision, target value, and interval bounds

# TODO: Implement the binary search function and print out the value of 'x' for which f(x) is approximately 0.
'''