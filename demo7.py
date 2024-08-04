import sqlite3
import tkinter as tk
from tkinter import ttk

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

def enregistrer_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil):
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    identifiant = str(uuid.uuid4())
    cursor.execute('''INSERT INTO utilisateurs1 (id, nom, prenom, date_naissance, ville_origine, ville_acceuil) 
                   VALUES (?, ?, ?, ?, ?, ?)''', (identifiant, nom, prenom, date_naissance, ville_origine, ville_acceuil))
    conn.commit()
    conn.close()

def modifier_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil, identifiant):
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE utilisateurs1 SET nom=?, prenom=?, date_naissance=?, ville_origine=?, ville_acceuil=?
                   WHERE id=?''', (nom, prenom, date_naissance, ville_origine, ville_acceuil, identifiant))
    conn.commit()
    conn.close()

def supprimer_utilisateur(identifiant):
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM utilisateurs1 WHERE id=?''', (identifiant,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestion des utilisateurs")
    root.geometry("1920x1000+0+0")

    # Reste du code pour créer l'interface graphique...
    # Assurez-vous d'appeler les fonctions aux bons endroits !

    root.mainloop()
