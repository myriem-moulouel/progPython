# prog recursive

def fusion(l1, l2):
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    elif l1[0] <= l2[0]:
        return (l1[0], fusion(l1[1], l2) )
    elif l2[0] <= l1[0]:
        return (l2[0], fusion(l1, l2[1]) )


l1 = (1,(3,(4,None)))
l2 = (2,(5,(6,(10,None))))
print(fusion(l1, l2))



# on suppose que la longueur de la liste >= 2
def cut(l):
    def longueur(l):
        if l[1]==None:
            return 1
        else:
            return 1+longueur(l[1])
    long = longueur(l)
    print(long)
    a = l
    l1 = (a[0],None)
    a = a[1]
    print(a)
    for i in range(long//2-1):
        l1 = (a[0], l1)
        a = a[1]
            
    l2 = a

    return [l1, l2]


l1 = (6,(5,(1,(3,(4,None)))))
print(cut(l1))


# tri fusion
def tri(l):
    if l[1]==None: # le cas ou la foction a un seul element
        return l
    elif l[1][1] == None : # le cas ou on a deux element
        if l[0] <= l[1][0]:
            return l
        else:
            return (l[1][0], (l[0], None))
    else:
        ll = cut(l)
        return fusion(tri(ll[0]),tri(ll[1]))

print(tri((10,(2,(4,(6,(1,(5,None))))))))