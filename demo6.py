import sqlite3
import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry,Button
from tkinter import ttk
import calendar
import uuid

# Connexion à la base de données (crée un fichier ma_base.db s'il n'existe pas)
conn = sqlite3.connect("ma_base1.db")

# Création d'un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Création d'une table (par exemple, une table "utilisateurs")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs1 (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        date_naissance INTEGER,
        Ville_origine TEXT,
        Ville_acceuil TEXT
    )
""")

# Fermeture de la connexion
conn.close()

def ajouter_utilisateur():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    ville_origine = ttk_ville_origine.get()
    ville_acceuil = ttk_ville_acceuil.get() 
    
    ajouter_utilisateur(nom, prenom, date_naissance,ville_origine,ville_acceuil)
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    identifiant = str(uuid.uuid4())
    cursor.execute('''INSERT INTO utilisateurs1 (id, nom, prenom, date_naissance, ville_origine, ville_acceuil)
                       VALUES (?,?,?,?,?,?)''', (identifiant,nom, prenom, date_naissance, ville_origine, ville_acceuil))
    print("Utilisateur enregistrer :", nom, prenom, date_naissance, ville_origine, ville_acceuil)
    conn.commit()
    conn.close()
    # Connexion à la base de données
    #conn = sqlite3.connect("ma_base1.db")
    #cursor = conn.cursor()

    # Insertion d'un nouvel utilisateur
#def ajouter_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil):
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    identifiant = str(uuid.uuid4())
    cursor.execute('''INSERT INTO utilisateurs1 (id,nom, prenom, date_naissance, ville_origine, ville_acceuil) 
                   VALUES (?, ?, ?, ?, ?,)''', (identifiant, nom, prenom, date_naissance, ville_origine, ville_acceuil))
    conn.commit()

    # Fermeture de la connexion
    conn.close()
    
def modifier_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil):
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE utilisateurs1 SET nom=?, prenom=?, date_naissance=?, ville_origine=?, ville_acceuil=? 
                   #WHERE id=?''', (nom, prenom, date_naissance, ville_origine, ville_acceuil))
    modifier_utilisateur(nom, prenom, date_naissance, ville_origine, ville_acceuil)
    print("Utilisateur modifier")
    conn.commit()

    # Fermeture de la connexion
    conn.close()
    
def supprimer_utilisateur(identifiant):
    conn = sqlite3.connect('ma_base1.db')
    cursor = conn.cursor()
    identifiant = str(uuid.uuid4())
    cursor.execute('''DELETE FROM utilisateurs1 WHERE id=?''', (identifiant))
    supprimer_utilisateur(identifiant)
    print("Utilisateur supprime")
    conn.commit()

    # Fermeture de la connexion
    conn.close()
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestion des utilisateurs")
    root=root
    root.title("Inscription")
    root.geometry("1920x1000+0+0")

frame1 = Frame(root, bg="gray")
frame1.place(x=500, y=200,width=700,height=500)

title = Label(frame1, text="Inscription Deplaces", font=("time new roman", 20, "bold"), bg="grey", fg="green").place(x=50,y=30)

# Widgets
label_prenom = Label(frame1, text="Prenom :", font=("time new roman", 20, "bold"), bg="grey", fg="black").place(x=370,y=100)
entry_prenom = Entry(frame1, font=("times new roman", 15), bg="lightgrey", fg="black").place(x=370,y=130, width=250)

label_nom = Label(frame1, text="Nom :", font=("time new roman", 20, "bold"), bg="grey", fg="black").place(x=50,y=100)
entry_nom = Entry(frame1, font=("times new roman",15), bg="lightgrey").place(x=50, y=130,width=250)

label_date_naissance = Label(frame1, text="Date de naissance", font=("time new roman",15, "bold"), bg="grey", fg="black").place(x=50,y=180)
entry_date_naissance = Entry(frame1, font=("times new roman",15), bg="lightgrey").place(x=50, y=210,width=250)

#label_date_naissance = Label(frame1, text="Date",font=("time new roman", 15), bg="grey",fg="black").place(x=50,y=100)
#entry_date_naissance = calendar(frame1, font=("times new roman", 15), bg="lightgrey", date_pattern="dd/mm/yy")

#ville d'origine
#label_ville_origine = tk.Label(frame1, text="Ville d'Origine :", font=("time new roman", 20, "bold"), bg="grey", fg="black").place(x=370,y=180)
#ttk_ville_origine = ttk.Combobox(frame1, font=("times new roman",15), state="readonly").place(x=370, y=210,width=250)
#ttk_ville_origine["values"] = ("Selectionner", "Ouagadougou", "Bobo Dioulasso", "Koudougou")
#ttk_ville_origine.current(0)
# Assurez-vous que ttk_ville_origine est correctement initialisé
ttk_ville_origine = ttk.Combobox(root, state="readonly")
ttk_ville_origine["values"] = ("Selectionner", "Ouagadougou", "Bobo Dioulasso", "Koudougou")
ttk_ville_origine.current(0)  # Sélectionnez la première valeur par défaut


#ville d'acceuil
#label_ville_acceuil = Label(frame1, text="Ville d'Acceuil :", font=("time new roman", 15, "bold"), bg="grey", fg="black").place(x=50,y=250)
#ttk_ville_acceuil = ttk.Combobox(root, font=("times new roman",15), state="readonly").place(x=50, y=300,width=250)
#ttk_ville_acceuil["values"] = ("Selectionner", "Ouagadougou", "Bobo Dioulasso", "Koudougou", "Ouahigouya", "Kaya", "Dori", "Djibo", "Gaoua")
#ttk_ville_acceuil.current(0)
# Assurez-vous que ttk_ville_acceuil est correctement initialisé
ttk_ville_acceuil = ttk.Combobox(root, state="readonly")
ttk_ville_acceuil["values"] = ("Selectionner", "Ouagadougou", "Bobo Dioulasso", "Koudougou", "Ouahigouya", "Kaya", "Dori", "Djibo", "Gaoua")
ttk_ville_acceuil.current(0)  # Sélectionnez la première valeur par défaut


bouton_ajouter = tk.Button(frame1, text="Ajouter",font=("time new roman",15, "bold"),command=ajouter_utilisateur, bg="green", fg="black").place(x=100,y=400)
bouton_modifier = tk.Button(frame1, text="Modifier",font=("time new roman",15, "bold"),command=modifier_utilisateur, bg="blue", fg="black").place(x=300,y=400)
bouton_supprimer = tk.Button(frame1, text="Supprimer",font=("time new roman",15, "bold"),command=supprimer_utilisateur, bg="red", fg="black").place(x=400,y=400)



root.mainloop()
