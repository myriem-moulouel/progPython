# Partie 3 : Programmation fonctionnelle
# exercice 1:

print("Boucle sans boucle")
print("")
print("fonction foo")
print("======> version iterative")
def foo_iter(x):
    i = 0
    v = x*x
    while i<=v:
        v = v-x
        i = i+x
    return i*v

print(foo_iter(55))

print("======> version recursive")
def foo_rec(x) :
    def boucle(i,v):
        if i<=v:
            return boucle(i+x, v-x)
        else:
            return i*v
    return boucle(0,x*x)

print(foo_rec(55))


print("_____________________________________________________________________")

print("")
print("fonction bar")
print("======> version iterative")
def bar_iter(x,y):
    r = 0
    for i in range(0, 10):
        r = r+x
    for j in range(r,0,-1):
        r = r-y
    return r

print(bar_iter(-8,2))

print("======> version recursive")
def bar_rec(x,y):
    def boucle1(i, r):
        if i < 10:
            return boucle1(i+1, r+x)
        else:
            return r
    def boucle2(j, r):
        if j>0:
            return boucle2(j-1, r-y)
        else:
            return r

    return boucle2(boucle1(0,0),boucle1(0,0))

print(bar_rec(-8,2))