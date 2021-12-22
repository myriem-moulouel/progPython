import sys

#f = input("saisissez un fichier txt : ")
f = "test.txt"
fichier_opened = open(f,"r")
fichier = fichier_opened.readlines()

# nombre de ligne
nb_lignes = len(fichier)
print("le nombre de lignes : ", nb_lignes)
print("____________________________________________________")

# nombre de caractères
nb_car = 0
for ligne in fichier:
    nb_car+=len(ligne)
print("le nombre de caractères : ",nb_car)
print("____________________________________________________")

# nombre de mots
nb_mots = 0
for ligne in fichier:
    nb_mots+=len(ligne.split(" "))
print("le nombre de mots : ", nb_mots)
print("____________________________________________________")

# mot le plus fréquent
liste_mots = []
for ligne in fichier:
    l = ligne.split(" ")
    for i in l:
        i = i.replace('\n','')
        liste_mots.append(i)

liste_vue = []
occurence_max = 0
mot_frequent = ""
for mot in liste_mots:
    if mot not in liste_vue:
        liste_vue.append(mot)
        occurence = liste_mots.count(mot)
        if occurence_max < occurence:
            mot_frequent = mot
            occurence_max = occurence
print("le mot le plus frequent est : ",mot_frequent)
print("____________________________________________________")

# mot le plus long
longueur_max = 0
mot_long = ""
for mot in liste_mots:
    longueur = len(mot)
    if longueur_max <= longueur:
        mot_long = mot
        longueur_max = longueur
print("le mot le plus long est : ",mot_long," de taille : ",longueur_max)
print("____________________________________________________")

# moyenne du nombre de mots par ligne
nb_lignes = 0
nb_mots_ligne = 0
for ligne in fichier:
    nb_lignes+=1
    l = ligne.split(" ")
    nb_mots_ligne += len(l)
moyenne = nb_mots_ligne//nb_lignes
print("la moyenne du nombre de mots par ligne : ",moyenne)
print("____________________________________________________")

# lettre la plus fréquente
concatenation = []
for ligne in fichier:
    l = ligne.replace('\n','')
    l = l.split(',')
    print(l)
    concatenation+=l
#concatenation = ('').join(concatenation)
print(concatenation)

lettre_frequente = ''
occ_max = 0
for l in concatenation:
    nb = concatenation.count(l)
    if nb>occ_max:
        lettre_frequente = l
        occ_max = nb
print("la lettre la plus fréquente est : ",lettre_frequente," avec ",occ_max," occurence")
print("____________________________________________________")
