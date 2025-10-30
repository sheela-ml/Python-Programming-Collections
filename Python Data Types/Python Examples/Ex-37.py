# Map Filter Reduce.py
# Demonstrate map, filter, and functools.reduce.

from functools import reduce

nums = [1,2,3,4,5]
squares = list(map(lambda x: x*x, nums))
evens = list(filter(lambda x: x%2==0, nums))
sum_vals = reduce(lambda a,b: a+b, nums)

if __name__ == '__main__':
    print("Squares:", squares)
    print("Evens:", evens)
    print("Sum:", sum_vals)

