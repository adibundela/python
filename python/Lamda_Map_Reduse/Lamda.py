# sq of a no. 

sq = lambda x : x**2

print(sq(6))

# add 2 numbers
ad = lambda a,b: a+b

print(ad(3,4))

# find max of 2 numbers
mx = lambda x,y: x if x > y else y
print(mx(5,6))

# fibonacci series

fib  = lambda n: n if n<=1 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(10)])

# factorial
 
fact = lambda n : 1 if n<=1 else n*fact(n-1)
print([fact(i) for i in range(10)])