from dataclasses import dataclass
from datetime import datetime
@dataclass
class Customer:
    id:str=""
    first_name:str=""
    last_name:str=""
    email:str=""
    gender:str=""
    ip_address:str=""
    birth_date:str=""


    # def convert_date_format(self):
    #     """
    #     Convertit une date du format yyyy-mm-dd vers dd/mm/yyyy

    #     Returns:
    #         str: Date au format dd/mm/yyyy
            
    #     Example:
    #         >>> convert_date_format("2000-04-07")
    #         "07/04/2000"
    #     """
    #     try:
    #         # Parse la date au format yyyy-mm-dd
    #         date_obj = datetime.strptime(self.birth_date, "%Y-%m-%d")
    #         # Convertit au format dd/mm/yyyy
    #         return date_obj.strftime("%d/%m/%Y")
    #     except ValueError as e:
    #         print(f"Erreur lors de la conversion de la date {self.birth_date}: {e}")
    #         return self.birth_date  # Retourne la date originale en cas d'erreur

    @property
    def age(self):
        """
        Calcule l'âge à partir d'une date de naissance au format dd/mm/yyyy
        
        Args:
            birth_date_str (str): Date de naissance au format "dd/mm/yyyy"
            
        Returns:
            int: Âge en années
            
        Example:
            >>> calculate_age("26/02/1992")
            33
        """
        try:
            # Parse la date de naissance (format dd/mm/yyyy)
            birth_date = datetime.strptime(self.birth_date, "%d/%m/%Y")
            
            # Date actuelle
            today = datetime.now()
            
            # Calcul de l'âge
            age = today.year - birth_date.year
            
            # Vérifier si l'anniversaire de cette année est déjà passé
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
                
            return age
            
        except ValueError as e:
            print(f"Erreur lors du parsing de la date {self.birth_date}: {e}")
            return None
