# Fibonacci Iterative.py
# Iterative fibonacci generator.

def fib_iter(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    print(list(fib_iter(10)))

