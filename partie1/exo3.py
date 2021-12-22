# exercice 3 :
print("exercice 3 :")

def add_termes(n):
    if n==0:
        return 0
    else:
        return n + add_termes(n-1)

n = int(input("saisissez une valeur de n : "))

f = add_termes(n)
print(str(n)+" addition des termes : "+str(f))

assert add_termes(4) == 10
