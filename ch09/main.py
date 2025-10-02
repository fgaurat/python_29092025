from DataRectangle import DataRectangle
from Rectangle import Rectangle
from Carre import Carre


def main_1():

    # lng = int(input("Longueur: "))
    # lrg = int(input("Largeur: "))
    lng =15
    lrg =11
    # Appel du constructeur
    r = Rectangle(lng,lrg) # Rectangle longueur = 3, largeur = 2


    print(r.longueur)
    print(r.largeur)
    r.largeur = 12
    r.longueur = 1000
    print(r.surface)

    s = str(r)
    print(s)
    
    # print(r.get_longueur()) # 3
    # r.set_longueur(4)
    # print(r.get_longueur()) # 4

    # print(r.get_largeur()) # 2
    # r.set_largeur(1)
    # print(r.get_largeur()) # 1

    # print(r.get_surface()) # 4
    print("--- Carre ---")
    c= Carre(2)

    print(c.cote)
    print(c.surface)
    print(c)

    c.cote = 12
    print(c.surface)

def main():
    r = DataRectangle(12,5)
    r3 = DataRectangle(12,5)
    print(r.longueur,r.largeur)
    print(r)

    r1 = Rectangle(4,3)
    r2 = Rectangle(4,3)

    if r1==r2: # r1.__eq__(r2)
        print("ok")
    else:
        print("ko")

    if r==r3: # r1.__eq__(r2)
        print("ok")
    else:
        print("ko")

if __name__=='__main__':
    # main_1()
    main()
