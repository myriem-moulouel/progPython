# exercice 2 :
print("exercice 2 :")

def facteur(n):
    if n==0:
        return 1
    else:
        return 2*facteur(n-1)

n = int(input("saisissez une valeur de n : "))

f = facteur(n)
print(str(n)+" occurrences de 2 : "+str(f))
