# MOULOUEL Myriem 

from abc import abstractmethod, ABC

class Rope(ABC):
    def __init__(self):
        self.length = 0
    @abstractmethod
    def __getitem__(self,i):
        pass
    @abstractmethod
    def __add__(self,r):
        pass
    @abstractmethod
    def __str__(self):
        pass



class App(Rope):
    def __init__(self,left,right):
        self.length = left.length + right.length
        self.left = left
        self.right = right
    
    def __getitem__(self,i):
        l = self.left.length
        if isinstance(i,slice):
            i1 = i.start
            i2 = i.stop
            if i1*i2 >= 0: # le cas ou i1 et i2 sont tous les deux positifs ou négatifs
                if i1<0 and i2<0:
                    i1 = -i1 + 1
                    i2 = -i2 + 1
                if i1<l:
                    if i2<l:
                        return self.left[i1:i2]
                    else:
                        return self.left[i1:l] + self.right[0:i2-l]
                elif i1>=l:
                    return self.right[i1-l:i2-l]
            else: # le cas où l'un des deux est négatif et l'autre positif
                if i1>i2:
                    s1 = self.right[i1:0]
                    if i2<l:
                        s2 = self.left[0:i2]
                        return ''.join(set(s1).intersection(s2))
                    else:
                        return s1
                else:
                    return ''
        else:
            if i>=0 and i<l:
                return self.left[i]
            elif i>=0 and i>=l:
                return self.right[i-l]
            elif i<0 and (i+l)>0:
                return self.right[i]
            elif i<0 and (i+l)<=0:
                return self.left[i+l-1]
    
    def __add__(self,r):
        self.right = self.right + r
        return self
    
    def __str__(self):
        return self.left.__str__() + self.right.__str__()



class Str(Rope):
    def __init__(self,s):
        self.length = len(str(s))
        self.s = s
    
    def __getitem__(self,i):
        if isinstance(i,slice):
            return self.s[i]
        elif i<self.length:
            return self.s[i]
    
    def __add__(self,r):
        n = r.length + self.length
        if isinstance(r,Str):
            if n<=10:
                if r.length > self.length:
                    r.s = self.s + str(r)
                    r.length = r.length + self.length
                    return r
                else:
                    self.s = self.s + str(r)
                    self.length = n
                    return self
            else:
                return App(self, r)
        else:
            if r.left.length >= self.length:
                r.left = self + r.left
                return r
            else:
                return App(self, r)
    
    def __str__(self):
        return str(self.s)

r = App(Str("La structure de"),App(App(Str("corde per"),Str("met de manipuler")),App(Str(" de grandes "),Str("chaînes"))))

print("~~~~~~~~~~~~~~~~~~~Test __str__~~~~~~~~~~~~~~~~~~~")
print("r : ",r)
print("longueur de App(Str(' de grandes '),Str('chaînes')) = ",App(Str(" de grandes "),Str("chaînes")).length)


print("")
print("~~~~~~~~~~~~~~~~~~~Test __getitem__~~~~~~~~~~~~~~~~~~~")
print("on suppose que les indices sont positifs")
print("r[6] = ",r[0])
print("r[23] = ",r[23])
print("r[59] = ",r[59])
print("r[0:23]  :  ",r[0:23])
print("r[21:54]  :  ",r[21:54])
print("r[-6:-1]  :  ",r[-6:-1])

print("")
print("~~~~~~~~~~~~~~~~~~~Test __add__~~~~~~~~~~~~~~~~~~~")

print("")
print("Construction de ===> (Str('debut de la ') + Str('chai')) + Str('ne')")
r2 = (Str("debut de la ") + Str("chai")) + Str("ne")
print(r2)
print("left => ",r2.left)
print("right => ",r2.right)

print("")
print("Construction de ===> Str('nous') + Str(' s') + Str('ommes')")
r3 = Str("nous") + Str(" s") + Str("ommes")
print(r3)
print("left => ",r3.left)
print("right => ",r3.right)

print("")
print("Construction de ===> Str('je s') + App(Str('uis tres '),Str('content'))")
r4 = (Str("je s") + App(Str("uis tres "),Str("content")))
print(r4)
print("left => ",r4.left)
print("right => ",r4.right)

