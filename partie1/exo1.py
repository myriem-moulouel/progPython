# Partie 1 : Les bases de la programmation en python

# exercice 1 :
import math

print("exercice 1 :")
def intersection( a, b, c, d ):
    if a != c:
        x = (d-b)/(a-c)
    else:
        x = math.inf
    return ( x, a*x+b)

a = int(input("saisissez a = "))
b = int(input("saisissez b = "))
c = int(input("saisissez c = "))
d = int(input("saisissez d = "))

(x,y) = intersection( a, b, c, d )

if x == math.inf:
    print("Il n'y a pas d'intersection de y="+str(a)+"x+"+str(b)+" et y="+str(c)+"x+"+str(d))
else:
    print("intersection de y="+str(a)+"x+"+str(b)+" et y="+str(c)+"x+"+str(d)+" : c'est le point ("+str(x)+","+str(y)+")")

# si les droites sont paralelles on aura a = c, donc on aura une division par 0

