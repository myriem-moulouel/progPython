def fst(l):
    def gauche(paire):
        return paire[0]
    return list(map(gauche, l))

print(fst( [(1,2), (5,7), (3, 9), (6, 0)] ))