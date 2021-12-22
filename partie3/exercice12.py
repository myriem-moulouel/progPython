from functools import reduce

def compte0(l):
    def egal_zero(x):
        if x==0:
            return 1
        else:
            return 0

    def somme(a, b):
        return a+b

    return reduce(somme, list(map(egal_zero, l)) )

print(compte0( [0, 1, 3, 0, 8, 0] ))