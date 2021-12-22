from functools import reduce 

def maximum(l):
    def max_elem(a, b):
        if a<b:
            return b
        else:
            return a
    return reduce(max_elem, l)

print(maximum( [-4, 5, 7, 9, 0, 3] ))