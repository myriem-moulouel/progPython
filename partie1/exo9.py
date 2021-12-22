# exercice 9:
# les diviseurs d'un nombre


def diviseurs(n):
    l = []

    for i in range(1,n+1):
        if i not in l and n%i==0:
            l.append(i)
    
    return l

n = int(input("saisissez une valeur pour n : "))

print(diviseurs(n))