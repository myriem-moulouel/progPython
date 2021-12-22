f = lambda x : (lambda f, y: 1 if y==0 else y * f(f, y-1))( (lambda f, y: 1 if y==0 else y * f(f, y-1)), x )

print(f(5))
print(2*3*4*5)
# le langage scim
