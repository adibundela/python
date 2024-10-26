l = [1,2,3,4,5,6,7]

def sq(x):
    return x**2
print(list(map(sq, l)))

# map with lemda fun 

print(list(map(lambda x: x**2 , l)))

