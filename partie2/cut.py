import sys

arguments = sys.argv

separateur = arguments[2]

tab1 = arguments[4]

tab2 = tab1.split(",")

tab4 = []
for seq in tab2:
    tab3 = seq.split("-")
    couple = (int(tab3[0]),int(tab3[1]))
    tab4.append(couple)

tab4 = sorted(tab4)

f = open(arguments[5],"r")
fichier = f.readlines()

tableau = []

for ligne in fichier:
    tableau.append(ligne.split(separateur))

rendu = []

for ligne in tableau:
    r = []
    for elem in tab4:
        l = ligne[elem[0]-1:elem[1]]
        for ri in l:
            if ri not in r:
                r.append(ri)
    rendu.append(r)




for ligne in rendu:
    print(",".join(ligne))