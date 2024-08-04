import sqlite3
import tkinter as tk
from tkinter import ttk
import uuid

# Connexion à la base de données (crée un fichier ma_base1.db s'il n'existe pas)
conn = sqlite3.connect("ma_base1.db")
cursor = conn.cursor()

# Création d'une table (par exemple, une table "utilisateurs1")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs1 (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        date_naissance INTEGER,
        ville_origine TEXT,
        ville_acceuil TEXT
    )
""")

# Fermeture de la connexion
conn.close()

def enregistrer_utilisateur():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    ville_origine = ttk_ville_origine.get()
    ville_acceuil = ttk_ville_acceuil.get()

    # Appel de la fonction pour enregistrer l'utilisateur
    # enregistrer_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil)
    print("Utilisateur enregistré :", nom, prenom, date_naissance, ville_origine, ville_acceuil)

def modifier_utilisateur():
    # Appel de la fonction pour modifier l'utilisateur
    # modifier_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil)
    print("Utilisateur modifié")

def supprimer_utilisateur():
    # Appel de la fonction pour supprimer l'utilisateur
    # supprimer_utilisateur(identifiant)
    print("Utilisateur supprimé")

root = tk.Tk()
root.title("Gestion des utilisateurs")
root.geometry("800x600")

# Widgets
label_nom = tk.Label(root, text="Nom :")
entry_nom = tk.Entry(root)

label_prenom = tk.Label(root, text="Prénom :")
entry_prenom = tk.Entry(root)

label_date_naissance = tk.Label(root, text="Date de naissance :")
entry_date_naissance = tk.Entry(root)

label_ville_origine = tk.Label(root, text="Ville d'Origine :")
ttk_ville_origine = ttk.Combobox(root, state="readonly")
ttk_ville_origine["values"] = ("Selectionner", "Ville1", "Ville2", "Ville3")
ttk_ville_origine.current(0)

label_ville_acceuil = tk.Label(root, text="Ville d'Accueil :")
ttk_ville_acceuil = ttk.Combobox(root, state="readonly")
ttk_ville_acceuil["values"] = ("Selectionner", "VilleA", "VilleB", "VilleC")
ttk_ville_acceuil.current(0)

bouton_enregistrer = tk.Button(root, text="Enregistrer", command=enregistrer_utilisateur)
bouton_modifier = tk.Button(root, text="Modifier", command=modifier_utilisateur)
bouton_supprimer = tk.Button(root, text="Supprimer", command=supprimer_utilisateur)

# Placement des widgets
# À vous de personnaliser la disposition des widgets dans votre interface !

root.mainloop()
