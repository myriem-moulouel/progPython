# Partie 3 : Programmation fonctionnelle
# exercice 2:

print("Ensembles comme des fonctions")
print("")
print("_____________________________________________________________________")
print("S2 etant l'ensemble de tous les entiers (positifs ou nuls) qui sont pairs")
#########################
def car_S1(x):
    return x>0
#########################

print(car_S1(0))
print("")
print("_____________________________________________________________________")
print("S2 etant l'ensemble de tous les entiers (positifs ou nuls) qui sont pairs")
#########################
def car_S2(x):
    def pairs(x):
        return x%2 == 0
    def pos_nul(x):
        return x>=0
    return pairs(x) and pos_nul(x)
#########################

print(car_S2(203))

print("")
print("_____________________________________________________________________")
print("S3 etant l'ensemble contenant uniquement les entiers 0, 3, 7 et 9")
#########################
def car_S3(x):
    def appartient(liste,x):
        return x in liste
    return appartient([0, 3, 7, 9], x)
#########################

print(car_S3(3))

print("")
print("_____________________________________________________________________")
print("S4 etant l'ensemble des entiers entre 10 et 1000 (inclus)")
#########################
def car_S4(x):
    return x in range(10,1001)
#########################

print(car_S4(1001))

print("")
print("_____________________________________________________________________")
print("S5 etant l'ensemble vide")
#########################
def car_S5(x):
    return x >0 and x<=0
#########################

print(car_S5(10))

print("")
print("_____________________________________________________________________")
