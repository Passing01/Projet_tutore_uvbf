import sqlite3
import tkinter as tk
from tkinter import ttk,Label,Entry
from tkinter import Frame
import uuid

# Connexion à la base de données (crée un fichier Burkina_Faso.db s'il n'existe pas)
conn = sqlite3.connect("Burkina_Faso2.db")
cursor = conn.cursor()

# Création d'une table pour les deplaces
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Deplaces (
        id TEXT PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        date_naissance TEXT,
        ville_origine TEXT,
        ville_acceuil TEXT
    )
""")

# Fermeture de la connexion
conn.close()

def enregistrer_Deplaces():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    ville_origine = ttk_ville_origine.get()
    ville_acceuil = ttk_ville_acceuil.get()

    # Générer un identifiant unique pour un deplace
    identifiant = str(uuid.uuid4())

    # Connexion à la base de données
    conn = sqlite3.connect('Burkina_Faso2.db')
    cursor = conn.cursor()

    # Insertion des données d'un deplace
    cursor.execute('''INSERT INTO Deplaces (id, nom, prenom, date_naissance, ville_origine, ville_acceuil) 
                   VALUES (?, ?, ?, ?, ?, ?)''', (identifiant, nom, prenom, date_naissance, ville_origine, ville_acceuil))
    conn.commit()

    # Fermeture de la connexion
    conn.close()

def modifier_Deplaces(identifiant, nom, prenom, date_naissance, ville_origine, ville_acceuil):
    conn = sqlite3.connect('Burkina_Faso2.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE Deplaces SET nom=?, prenom=?, date_naissance=?, ville_origine=?, ville_acceuil=?
                   WHERE id=?''', (nom, prenom, date_naissance, ville_origine, ville_acceuil, identifiant))
    conn.commit()
    conn.close()

    pass

def supprimer_Deplaces(identifiant):
    conn = sqlite3.connect('Burkina_Faso2.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Deplaces WHERE id=?''', (identifiant,))
    conn.commit()
    conn.close()

    pass

root = tk.Tk()
root.title("Gestion des Deplaces")
root.geometry("800x600")

frame1 = Frame(root, bg="gray")
frame1.place(x=500,y=200,width=700,height=500)

title = Label(frame1, text="Inscription Deplaces", font=("time new roman", 20, "bold"), bg="grey", fg="green").place(x=50,y=30)

# Widgets
label_nom = Label(frame1, text="Nom: ", font=("time new roman", 20, "bold"), bg="grey", fg="black").place(x=370,y=100)
entry_nom = Entry(frame1, font=("times new roman", 15), bg="lightgrey", fg="black").place(x=370,y=130, width=250)

#label_prenom = tk.Label(root, text="Prénom :")
#entry_prenom = tk.Entry(root)

label_prenom = Label(frame1, text="Prenom :", font=("time new roman", 20, "bold"), bg="grey", fg="black").place(x=50,y=100)
entry_prenom = Entry(frame1, font=("times new roman",15), bg="lightgrey").place(x=50, y=130,width=250)

#label_date_naissance = tk.Label(root, text="Date de naissance :")
#entry_date_naissance = tk.Entry(root)

label_date_naissance = Label(frame1, text="Date de naissance", font=("time new roman",15, "bold"), bg="grey", fg="black").place(x=50,y=180)
entry_date_naissance = Entry(frame1, font=("times new roman",15), bg="lightgrey").place(x=50, y=210,width=250)

label_ville_origine = tk.Label(frame1, text="Ville d'Origine :", font=("time new roman", 20, "bold"), bg="grey", fg="black").place(x=370,y=180)
ttk_ville_origine = ttk.Combobox(frame1, font=("times new roman", 15), state="readonly")
ttk_ville_origine.place(x=370,y=210,width=250)
ttk_ville_origine["values"] = ("Selectionner", "Ouagadougou", "Bobo Dioulasso", "Koudougou")
ttk_ville_origine.current(0)

label_ville_acceuil = tk.Label(frame1, text="Ville d'Accueil :", font=("times new roman", 15, "bold"), bg="grey", fg="black").place(x=50,y=250)
ttk_ville_acceuil = ttk.Combobox(frame1, font=("times new roman", 15), state="readonly")
ttk_ville_acceuil.place(x=50,y=300,width=250)
ttk_ville_acceuil["values"] = ("Selectionner", "Ouagadougou", "Bobo Dioulasso", "Koudougou")
ttk_ville_acceuil.current(0)

bouton_enregistrer = tk.Button(frame1, text="Enregistrer",font=("times new roman", 15, "bold"), command=enregistrer_Deplaces, bg="green", fg="black").place(x=100,y=400)
bouton_modifier = tk.Button(frame1, text="Modifier",font=("times new roman", 15, "bold"), command=modifier_Deplaces, bg="blue", fg="black").place(x=300,y=400)
bouton_supprimer = tk.Button(frame1, text="Supprimer",font=("times new roman", 15, "bold"), command=supprimer_Deplaces, bg="red", fg="black").place(x=400,y=400)

# Placement des widgets
# À vous de personnaliser la disposition des widgets dans votre interface !

root.mainloop()
