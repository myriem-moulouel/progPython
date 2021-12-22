# Partie 3 : Programmation fonctionnelle
# exercice 5:

def car_S1(x):
    return x>0

def car_S2(x):
    def pairs(x):
        return x%2 == 0
    def pos_nul(x):
        return x>=0
    return pairs(x) and pos_nul(x)

def car_S3(x):
    def appartient(liste,x):
        return x in liste
    return appartient([0, 3, 7, 9], x)

def car_S4(x):
    return x in range(10,1001)

def car_S5(x):
    return x >0 and x<=0

def ajout(x, car_S):
    return lambda y: car_S(y) or y==x

##############################################################################


#testes
car_y=ajout(-20,car_S4)
print(car_y(-21))