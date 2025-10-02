#!/usr/bin/env python3
"""
Script pour calculer l'âge à partir des données JSON avec birth_date
"""

import json
from datetime import datetime

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

def process_json_data():
    """
    Traite les données JSON pour calculer l'âge de chaque personne
    """
    try:
        # Charger les données JSON
        with open("MOCK_DATA.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print("Calcul des âges à partir des données JSON:")
        print("=" * 60)
        
        # Traiter chaque personne dans les données
        for d in data:
            if 'birth_date' in d and d['birth_date']:
                # Calculer l'âge
                age = calculate_age(d['birth_date'])
                
                if age is not None:
                    # Ajouter l'âge au dictionnaire
                    d['age'] = age
                    
                    # Afficher les informations
                    print(f"ID: {d['id']:>3} | "
                          f"{d['first_name']} {d['last_name']:<20} | "
                          f"Né(e) le: {d['birth_date']} | "
                          f"Âge: {age:>2} ans")
                else:
                    print(f"❌ Impossible de calculer l'âge pour {d['first_name']} {d['last_name']}")
            else:
                print(f"❌ Date de naissance manquante pour {d.get('first_name', 'Inconnu')}")
        
        # Statistiques
        ages = [d.get('age') for d in data if d.get('age') is not None]
        if ages:
            print("\n" + "=" * 60)
            print("📊 STATISTIQUES:")
            print(f"   Nombre de personnes: {len(data)}")
            print(f"   Âges calculés: {len(ages)}")
            print(f"   Âge moyen: {sum(ages) / len(ages):.1f} ans")
            print(f"   Âge minimum: {min(ages)} ans")
            print(f"   Âge maximum: {max(ages)} ans")
        
        return data
        
    except FileNotFoundError:
        print("❌ Erreur: Le fichier MOCK_DATA.json n'a pas été trouvé.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erreur lors de la lecture du JSON: {e}")
        return None

def demo_age_calculation():
    """
    Démonstration du calcul d'âge avec quelques exemples
    """
    print("🧮 Démonstration du calcul d'âge:")
    print("-" * 40)
    
    # Exemples de dates de naissance
    test_dates = [
        "26/02/1992",  # Berrie Hearse
        "14/04/1996",  # Crosby De la Barre
        "05/06/1992",  # Friederike Goodge
        "01/01/2000",  # Exemple du millénaire
        "31/12/1980"   # Exemple années 80
    ]
    
    for date in test_dates:
        age = calculate_age(date)
        if age is not None:
            print(f"Date de naissance: {date} → Âge: {age} ans")

if __name__ == "__main__":
    # Démonstration
    demo_age_calculation()
    print("\n" + "=" * 60 + "\n")
    
    # Traitement des données JSON
    processed_data = process_json_data()
    
    if processed_data:
        print(f"\n✅ Traitement terminé ! {len(processed_data)} enregistrements traités.")