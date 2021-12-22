longueur = float(input("saisissez la longueur : "))
largeur = float(input("saisissez la largeur : "))

(x,y) = (float(input("saisissez la posision x : ")), float(input("saisissez la posision y : ")))

(dx,dy) = (float(input("saisissez le deplacement -longueur<=dx<=longueur : ")), float(input("saisissez le deplacement -largeur<=dy<=largeur : ")))

def check_position( x, y, longueur, largeur):

    if x <= longueur and x >= 0 and y <= largeur and y >= 0 :
        return True
    else:
        return False  

def billard ( x, y, dx, dy, longueur, largeur):

    distanceX = x + dx
    distanceY = y + dy
    print("(dx,dy)",(dx,dy))
    
    while not(check_position( distanceX, distanceY, longueur, largeur)):
        print((distanceX, distanceY))
        if distanceX > longueur :
            n = (longueur-x)*dy/dx
            dx = -dx-x+longueur
            dy = dy - n
            
            y = y + n
            x = longueur
            print("-1 (dx,dy)",(dx,dy))


        elif distanceX < 0 :
            n = (x*dy)/dx
            dx = -dx-x
            dy = dy - n

            y = y + n
            x = 0
            print("-2 (dx,dy)",(dx,dy))


        elif distanceY > largeur :
            n = (largeur-y)*dx/dy
            dy = -dy-y+largeur
            dx = dx - n
            
            x = x + n
            y = largeur
            print("-3 (dx,dy)",(dx,dy))


        elif distanceY <0 :
            n = (y*dx)/dy
            dy = -dy-y
            dx = dx - n

            x = x + n
            y = 0
            print("-4 (dx,dy)",(dx,dy))


        distanceX = x + dx
        distanceY = y + dy

    return (distanceX, distanceY)

print(billard(x,y, dx, dy, longueur,largeur))