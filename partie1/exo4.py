# exercice 4 :
s = int(input("saisissez la somme initiale : "))
t = int(input("saisissez le taux d'interets annuel entre 0 et 100 % : "))
n = int(input("saisissez le nombre d'années : "))

montant_total = s
print("le montant total initial : "+str(montant_total))
for i in range(1,n+1):
    interet = montant_total*t/100
    print("l'interet apres "+str(i)+" ans : "+str(interet))
    montant_total = montant_total+interet
    

print("le montant total après "+str(n)+" d'années : "+str(montant_total))


