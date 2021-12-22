from functools import reduce

def somme_des_carrees(l):
    def carres(x):
        return x**2

    def somme(x, y ):
        return x + y

    return reduce( somme, map(carres, l ))


s = somme_des_carrees([1, 2, 3, 4])
print(s)