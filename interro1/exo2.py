from functools import reduce


# on suppose que la longueur de la liste > 1
def seconde_max(l):
    f = lambda x,y: (y, x[0]) if y >= x[0] else ( (x[0], y) if y>=x[1] else x )
    return reduce(f, l, (l[0], l[0]))

print(seconde_max([1,2,5,2,6,9,7]))


# et on prend le deuxieme element de la paire
l = [1,2,5,2,6,9,7]

print("le deuxieme plus grand element de l = ", seconde_max(l)[1])
