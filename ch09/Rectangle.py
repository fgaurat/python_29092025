class Rectangle:

    # Constructeur
    def __init__(self,a,b):
        self.__longueur = a
        self.__largeur = b
    
    @property
    def longueur(self):
        """
        La longueur
        """
        return self.__longueur
    
    @longueur.setter
    def longueur(self,l):
        if l>=0:
            self.__longueur = l
    @property
    def largeur(self):
        return self.__largeur
    @largeur.setter
    def largeur(self,l):
        if l>=0:
            self.__largeur = l
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur


    def __eq__(self, value: object) -> bool:
        return self.longueur == value.longueur and self.largeur == value.largeur


        return f"Rectangle: {self.longueur=}, {self.largeur=}"
    # longueur = property(get_longueur,set_longueur,doc="propriété longueur")
    # largeur = property(get_largeur,set_largeur,doc="propriété largeur")
    # surface = property(get_surface,doc="propriété surface")