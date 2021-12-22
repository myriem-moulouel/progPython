# exercice 5:

from turtle import *

def escalier(longueur):
    down()
    for i in range(2):
        forward(longueur)
        if i%2 == 0:
            left(90)
        else:
            right(90)
    up()
    return

#up()
#clear()
n = int(input("saisissez n le nombre de marche de l'escalier : "))
longueur = 40
for i in range(n):
    escalier(longueur)
