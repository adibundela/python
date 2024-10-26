
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
fib_gtr = fibonacci(100000)

for num in fib_gtr:
    print(num)