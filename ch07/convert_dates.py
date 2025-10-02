#!/usr/bin/env python3
"""
Script pour convertir les dates du format yyyy-mm-dd vers dd/mm/yyyy
dans le fichier MOCK_DATA.csv
"""

import csv
from datetime import datetime

def convert_date_format(date_string):
    """
    Convertit une date du format yyyy-mm-dd vers dd/mm/yyyy
    
    Args:
        date_string (str): Date au format yyyy-mm-dd
        
    Returns:
        str: Date au format dd/mm/yyyy
        
    Example:
        >>> convert_date_format("2000-04-07")
        "07/04/2000"
    """
    try:
        # Parse la date au format yyyy-mm-dd
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        # Convertit au format dd/mm/yyyy
        return date_obj.strftime("%d/%m/%Y")
    except ValueError as e:
        print(f"Erreur lors de la conversion de la date {date_string}: {e}")
        return date_string  # Retourne la date originale en cas d'erreur

def process_csv_file(input_file, output_file):
    """
    Traite le fichier CSV pour convertir les dates de birth_date
    
    Args:
        input_file (str): Chemin vers le fichier CSV d'entrée
        output_file (str): Chemin vers le fichier CSV de sortie
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            
            # Créer les objets lecteur et écrivain CSV
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            
            # Vérifier que les noms de colonnes ont été lus correctement
            if fieldnames is None:
                raise ValueError("Impossible de lire les noms de colonnes du fichier CSV")
                
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            # Écrire l'en-tête
            writer.writeheader()
            
            # Traiter chaque ligne
            for row in reader:
                # Convertir la date de naissance
                if 'birth_date' in row and row['birth_date']:
                    row['birth_date'] = convert_date_format(row['birth_date'])
                
                # Écrire la ligne modifiée
                writer.writerow(row)
                
        print(f"Conversion terminée ! Le fichier {output_file} a été créé.")
        
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")

def demo_conversion():
    """
    Démonstration de la conversion de date
    """
    # Exemples de dates à convertir
    test_dates = ["2000-04-07", "1992-02-26", "1996-04-14", "1992-06-05"]
    
    print("Démonstration de la conversion de dates :")
    print("Format d'origine : yyyy-mm-dd")
    print("Format cible : dd/mm/yyyy")
    print("-" * 40)
    
    for date in test_dates:
        converted = convert_date_format(date)
        print(f"{date} → {converted}")

if __name__ == "__main__":
    # Démonstration
    demo_conversion()
    print("\n" + "="*50 + "\n")
    
    # Traitement du fichier CSV
    input_file = "MOCK_DATA.csv"
    output_file = "MOCK_DATA_converted.csv"
    
    print(f"Conversion du fichier {input_file}...")
    process_csv_file(input_file, output_file)