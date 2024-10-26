def sr_no(n):
    for i in range(n):
        yield i**2

# Create an generator object

gtr = sr_no(5)
# print(next(gtr))
# print(next(gtr))
# print(next(gtr))
# print(next(gtr))
# print(next(gtr))

# FIBONACIII SERIES USING GENERATOR

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
fib_gtr = fibonacci(10000000)

for num in fib_gtr:
    print(num)