import tkinter
from tkinter import END, Label,Entry
from tkinter import Tk
import tkinter as tk
from tkinter import Button,messagebox 
import sqlite3
import uuid

root = Tk()
root.title('formulaire')
root.geometry('450x450')

conn = sqlite3.connect('Burkina_Faso4.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS deplaces(
    id TEXT PRIMARY KEY,
    prenom TEXT,
    nom TEXT,
    date_naissance TEXT,
    ville_origine TEXT,
    ville_acceuil TEXT
    )''')


def submit():
    conn = sqlite3.connect('Burkina_Faso4.db')
    cur = conn.cursor()
    
    identifiant = str(uuid.uuid4())
    
    cur.execute("INSERT INTO deplaces VALUES (:id, :prenom, :nom, :date_naissance, :ville_origine, :ville_acceuil)",
                {
                    'id': identifiant,
                    'prenom': e_prenom.get(),
                    'nom': e_nom.get(),
                    'date_naissance': e_date_naissance.get(),
                    'ville_origine': e_ville_origine.get(),
                    'ville_acceuil': e_ville_acceuil.get()
                }
                )
    
    
    conn.commit()
    conn.close()
    
    e_prenom.delete(0, END)
    e_nom.delete(0, END)
    e_date_naissance.delete(0, END)
    e_ville_origine.delete(0, END)
    e_ville_acceuil.delete(0, END)
    
    if e_prenom.get()=="" or e_nom.get()=="":
        messagebox.showerror("Erreur", "Veullez saisir tout les champs", parent=root)
    else:
        try:
            conn = sqlite3.connect('Burkina_Faso4.db')
            cur = conn.cursor()
            cur = conn.execute("SELECT * FROM deplaces WHERE prenom=?",(e_prenom.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Invalide", parent=root)
            else:
                messagebox.showinfo("Enregistrer")
                conn.close()
            
        
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}", parent=root)
    
def modifier():
    identifiant_modif = input("Entrez l'identifiant de l'enregistrement a modifier: ")
    
    nouveau_prenom = input("Nouveau prenom: ")
    nouveau_nom = input("Nouveau nom: ")
    nouveau_date_naissance = input("Nouvelle date de naissance: ")
    nouveau_ville_origine = input("nouvelle ville d'origine: ")
    nouveau_ville_acceuil = input("Nouvelle ville d'acceuil: ")
    
    conn = sqlite3.connect('Burkina_Faso4.db')
    cur = conn.cursor()
    identifiant = str(uuid.uuid4())
    cur.execute("UPDATE deplaces SET prenom=?, nom=?, date_naissance=?, ville_origine=?, ville_acceuil=? WHERE id=?",
                (nouveau_prenom, nouveau_nom, nouveau_date_naissance, nouveau_ville_origine, nouveau_ville_acceuil, identifiant_modif ))
    submit()
    
    conn.commit()
    conn.close()
    
def supprimer():
    identifiant_suppr = input("Entrez l'identifiant de l'enregistrement a supprimer: ")
    
    conn = sqlite3.connect('Burkina_Faso4.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM deplaces WHERE id=?", (identifiant_suppr,))
    
    conn.commit()
    conn.close()
    
    
def afficher():
    conn = sqlite3.connect('Burkina_Faso4.db')
    cur = conn.cursor()
    
    res = cur.execute("SELECT *, oid FROM Deplaces")
    records = res.fetchall()
    
    p_records = ""
    
    for record in records:
        p_records += str(record) + "\n"
        
    query_label = Label(root, text=p_records)
    query_label.grid(row=10,column=0,columnspan=2)
    
    conn.commit()
    conn.close()
    

prenom = Label(root, text="Prenom: ")
nom = Label(root, text="Nom")
date_naissance = Label(root, text="Date de naissance")
ville_origine = Label(root, text="Ville d'origine")
ville_acceuil = Label(root, text="Ville d'acceuil")

e_prenom = Entry(root, width=35)
e_nom = Entry(root, width=35)
e_date_naissance = Entry(root, width=35)
e_ville_origine = Entry(root, width=35)
e_ville_acceuil = Entry(root, width=35)

prenom.grid(row=1,column=0, padx=15)
e_prenom.grid(row=1, column=1, padx=15)

nom.grid(row=2,column=0, padx=15, pady=20)
e_nom.grid(row=2, column=1, padx=15)

date_naissance.grid(row=3,column=0, padx=15)
e_date_naissance.grid(row=3, column=1, padx=15)

ville_origine.grid(row=4,column=0, padx=15, pady=20)
e_ville_origine.grid(row=4, column=1, padx=15)

ville_acceuil.grid(row=5, column=0, padx=15, pady=20)
e_ville_acceuil.grid(row=5, column=1, padx=15)


save = Button(root, text="Enregistrer", width=30, command=submit)
save.grid(row=6, column=1, columnspan=2)

modifie = Button(root, text="Modifier", width=30, command=modifier)
modifie.grid(row=7, column=1, columnspan=2)

suppri = Button(root, text="Supprimer", width=30, command=supprimer)
suppri.grid(row=8, column=1,columnspan=2)

show_records = Button(root, text="Voir les enregistrements", width=30, command=afficher)
show_records.grid(row=9, column=1, columnspan=2, pady=15)



conn.commit()
conn.close()

root.mainloop()
