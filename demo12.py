
import tkinter
from tkinter import END, Label,Entry
from tkinter import Tk
import tkinter as tk
from tkinter import Button 
import sqlite3

root = Tk()
root.title('formulaire')
root.geometry('450x450')

conn = sqlite3.connect('Burkina_Faso3.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS deplaces(
    matricule TEXT,
    prenom TEXT,
    nom TEXT,
    email TEXT,
    tel INTEGER
    )''')


def submit():
    conn = sqlite3.connect('Burkina_Faso3.db')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO deplaces VALUES (:matricule, :prenom, :nom, :email, :tel)",
                {
                    'matricule': e_matricule.get(),
                    'prenom': e_prenom.get(),
                    'nom': e_nom.get(),
                    'email': e_email.get(),
                    'tel': e_tel.get()
                }
                )
    
    conn.commit()
    conn.close()
    
    e_matricule.delete(0, END)
    e_prenom.delete(0, END)
    e_nom.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    
    
def afficher():
    conn = sqlite3.connect('Burkina_Faso3.db')
    cur = conn.cursor()
    
    res = cur.execute("SELECT *, oid FROM Deplaces")
    records = res.fetchall()
    
    p_records = ""
    
    for record in records:
        p_records += str(record) + "\n"
        
    query_label = Label(root, text=p_records)
    query_label.grid(row=7,column=0,columnspan=2)
    
    conn.commit()
    conn.close()
    

matricule = Label(root, text="matricule: ")
prenom = Label(root, text="Prenom: ")
nom = Label(root, text="Nom")
email = Label(root, text="Email")
tel = Label(root, text="Telephone")

e_matricule = Entry(root, width=35)
e_prenom = Entry(root, width=35)
e_nom = Entry(root, width=35)
e_email = Entry(root, width=35)
e_tel = Entry(root, width=35)


matricule.grid(row=0,column=0, padx=15, pady=20)
e_matricule.grid(row=0, column=1, padx=15)

prenom.grid(row=1,column=0, padx=15)
e_prenom.grid(row=1, column=1, padx=15)

nom.grid(row=2,column=0, padx=15, pady=20)
e_nom.grid(row=2, column=1, padx=15)

email.grid(row=3,column=0, padx=15)
e_email.grid(row=3, column=1, padx=15)

tel.grid(row=4,column=0, padx=15, pady=20)
e_tel.grid(row=4, column=1, padx=15)


save = Button(root, text="Enregistrer", width=30, command=submit)
save.grid(row=5, column=1, columnspan=2)

show_records = Button(root, text="Voir les enregistrements", width=30, command=afficher)
show_records.grid(row=6, column=1, columnspan=2, pady=15)


conn.commit()
conn.close()



root.mainloop()
