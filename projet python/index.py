from os import name
import sqlite3
import uuid

# Fonction pour créer la base de données et la table si elles n'existent pas
def creer_base_de_donnees():
    conn = sqlite3.connect(r'db/ouedraogo.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS deplaces (
                        id TEXT PRIMARY KEY,
                        nom TEXT,
                        prenom TEXT,
                        date_naissance TEXT,
                        ville_origine TEXT,
                        nouvelle_ville TEXT
                    )''')
    conn.commit()
    conn.close()

# Fonction pour enregistrer un déplacé dans la base de données
def enregistrer_deplace(nom, prenom, date_naissance, ville_origine, nouvelle_ville):
    conn = sqlite3.connect(r'db/ouedraogo.db')
    cursor = conn.cursor()
    identifiant = str(uuid.uuid4())
    cursor.execute('''INSERT INTO deplaces (id, nom, prenom, date_naissance, ville_origine, nouvelle_ville)
                    VALUES (?, ?, ?, ?, ?, ?)''', (identifiant, nom, prenom, date_naissance, ville_origine, nouvelle_ville))
    conn.commit()
    conn.close()

# Fonction pour modifier les informations d'un déplacé en utilisant son identifiant
def modifier_deplace(identifiant, nom, prenom, date_naissance, ville_origine, nouvelle_ville):
    conn = sqlite3.connect(r'db/ouedraogo.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE deplaces SET nom=?, prenom=?, date_naissance=?, ville_origine=?, nouvelle_ville=?
                    WHERE id=?''', (nom, prenom, date_naissance, ville_origine, nouvelle_ville, identifiant))
    conn.commit()
    conn.close()

# Fonction pour supprimer un déplacé en utilisant son identifiant
def supprimer_deplace(identifiant):
    conn = sqlite3.connect(r'db/ouedraogo.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM deplaces WHERE id=?''', (identifiant,))
    conn.commit()
    conn.close()

# Fonction pour afficher le menu et gérer les actions
def menu():
    while True:
        print("\nMenu:")
        print("1. Ajouter un déplacé")
        print("2. Modifier un déplacé")
        print("3. Supprimer un déplacé")
        print("4. Quitter")
        
        choix = input("Choisissez une action: ")

        if choix == "1":
            ajouter_deplace()
        elif choix == "2":
            modifier_deplace_menu()
        elif choix == "3":
            supprimer_deplace_menu()
        elif choix == "4":
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Fonction pour ajouter un déplacé en saisissant les données de façon interactive
def ajouter_deplace():
    nom = input("Entrez le nom: ")
    prenom = input("Entrez le prénom: ")
    date_naissance = input("Entrez la date de naissance (AAAA-MM-JJ): ")
    ville_origine = input("Entrez la ville d'origine: ")
    nouvelle_ville = input("Entrez la nouvelle ville: ")

    enregistrer_deplace(nom, prenom, date_naissance, ville_origine, nouvelle_ville)
    print("Déplacé ajouté avec succès.")

# Fonction pour modifier un déplacé en saisissant l'identifiant et les nouvelles données de façon interactive
def modifier_deplace_menu():
    identifiant = input("Entrez l'identifiant du déplacé à modifier: ")
    nom = input("Entrez le nouveau nom: ")
    prenom = input("Entrez le nouveau prénom: ")
    date_naissance = input("Entrez la nouvelle date de naissance (AAAA-MM-JJ): ")
    ville_origine = input("Entrez la nouvelle ville d'origine: ")
    nouvelle_ville = input("Entrez la nouvelle ville de destination: ")

    modifier_deplace(identifiant, nom, prenom, date_naissance, ville_origine, nouvelle_ville)
    print("Déplacé modifié avec succès.")

# Fonction pour supprimer un déplacé en saisissant son identifiant de façon interactive
def supprimer_deplace_menu():
    identifiant = input("Entrez l'identifiant du déplacé à supprimer: ")
    supprimer_deplace(identifiant)
    print("Déplacé supprimé avec succès.")

# Programme principal
if name == "_main_":
    creer_base_de_donnees()
    menu()