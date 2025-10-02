import csv
from datetime import datetime
import convert_dates
def calculate_age(birth_date_str):
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
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        
        # Date actuelle
        today = datetime.now()
        
        # Calcul de l'âge
        age = today.year - birth_date.year
        
        # Vérifier si l'anniversaire de cette année est déjà passé
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
            
        return age
        
    except ValueError as e:
        print(f"Erreur lors du parsing de la date {birth_date_str}: {e}")
        return None

def main():
    csv_file_name = "MOCK_DATA.csv"
    with open(csv_file_name, newline="") as f:
        reader = csv.DictReader(f)
        for d in reader:
            d['birth_date'] = convert_dates.convert_date_format(d['birth_date'])
            age = calculate_age(d['birth_date'])
            d['age'] = age
            print(d)


if __name__ == '__main__':
    main()
