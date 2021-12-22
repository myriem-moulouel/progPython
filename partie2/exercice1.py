import sys

for f in sys.argv:
    print("________________________________________________________________________")
    print("Le fichier =========> ",f)
    fichier = open(f,"r")
    contenu = fichier.read()
    print(contenu)