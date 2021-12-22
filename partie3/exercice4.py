# Partie 3 : Programmation fonctionnelle
# exercice 4:

def car_S1(x):
    return x>0

def car_S2(x):
    def pairs(x):
        return x%2 == 0
    def pos_nul(x):
        return x>=0
    return pairs(x) and pos_nul(x)

def intersection(car_S1, car_S2):
    return lambda x: car_S1(x) and car_S2(x)

##############################################################################


#testes
p = intersection(car_S1, car_S2)
print(p(2))
