from Rectangle import Rectangle


class Carre(Rectangle):


    def __init__(self, c):
        super().__init__(c,c)
        self.__cote = c
    
    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,c):
        self.__cote = c
        self.longueur = c
        self.largeur = c
    
    def __str__(self):
        return f"Carré {self.cote}"
    