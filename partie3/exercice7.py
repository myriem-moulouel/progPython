def fact(n):
    return (lambda f,x: 1 if x==0 else x*f(f, x-1))( (lambda f,x: 1 if x==0 else x*f(f, x-1)), n )

print(fact(3))
