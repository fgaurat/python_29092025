from glob import glob
import csv


def read_csv_first_names(csv_file_path):
    """
    Lit un fichier CSV et retourne tous les first_name
    
    Args:
        csv_file_path (str): Chemin vers le fichier CSV
        
    Returns:
        list: Liste des prénoms trouvés dans le fichier
    """
    first_names = []
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8', newline='') as f:
            # Utiliser DictReader pour lire le CSV
            reader = csv.DictReader(f)
            
            # Parcourir chaque ligne du CSV
            for row in reader:
                # Vérifier si la colonne 'first_name' existe
                if 'first_name' in row and row['first_name']:
                    first_names.append(row['first_name'])
                    
        print(f"✅ Fichier {csv_file_path}: {len(first_names)} prénoms trouvés")
        
    except FileNotFoundError:
        print(f"❌ Erreur: Fichier {csv_file_path} non trouvé")
    except Exception as e:
        print(f"❌ Erreur lors de la lecture de {csv_file_path}: {e}")
    
    return first_names


def main():
    """
    Fonction principale qui lit tous les fichiers CSV et affiche les first_name
    """
    # Récupérer tous les fichiers CSV dans le dossier data
    all_csv = glob('data/*.csv')
    print(f"📁 Fichiers CSV trouvés: {len(all_csv)}")
    print("-" * 50)
    
    # Liste pour stocker tous les prénoms
    all_first_names = []
    
    # Traiter chaque fichier CSV
    for csv_file in all_csv:
        print(f"\n📄 Traitement du fichier: {csv_file}")
        
        # Lire les prénoms du fichier CSV
        first_names = read_csv_first_names(csv_file)
        
        # Ajouter les prénoms à la liste globale
        all_first_names.extend(first_names)
    
    print(all_first_names)
if __name__ == '__main__':
    main()
