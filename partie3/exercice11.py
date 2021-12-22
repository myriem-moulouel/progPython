def permute(l):
    def remplace(x):
        return 1 - x
    return list(map( remplace, l ))

print(permute( [ 1, 0, 1, 1, 1, 0 ] ))