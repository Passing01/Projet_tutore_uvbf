import tkinter
from tkinter import *
import sqlite3
from tkinter import ttk,messagebox

conn = sqlite3.connect('Mariam.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Deplaces(
                        id TEXT PRIMARY KEY,
                        nom TEXT,
                        prenom TEXT,
                        date_naissance TEXT,
                        ville_origine TEXT,
                        ville_acceuil TEXT)
                        """)
conn.commit()
conn.close()

class formSQLite3:
    def __init__(self,root) :
        self.root=root
        self.root.title("formulaire avec une base de donnee")
        self.root.geometry("1920x1000+0+0")
        
        #champ du formulaire
        frame1 = Frame(self.root,bg="gray")
        frame1.place(x=500, y=200, width=700,height=500)
        
        title = Label(frame1, text="formulaire", font=("time new rom",20, "bold"), bg="grey", fg="green").place(x=50,y=30)
        #nom
        text_prenom = Label(frame1, text="Prenom",font=("time new roman", 15), bg="grey",fg="black").place(x=370,y=100)
        self.ecr_prenom = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.ecr_prenom.place(x=370, y=130, width=250)
        #prenom
        text_nom = Label(frame1, text="Nom",font=("time new roman", 15), bg="grey",fg="black").place(x=50,y=100)
        self.ecr_nom = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.ecr_nom.place(x=50, y=130, width=250)
        #Date de naissance
        text_date_naissance = Label(frame1, text="Date de naissance",font=("time new roman", 15), bg="grey",fg="black").place(x=370,y=160)
        self.ecr_date_naissance = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.ecr_date_naissance.place(x=370, y=190, width=250)
        #ville d'origine
        text_ville_origine = Label(frame1, text="Ville d'Origine",font=("time new roman", 15), bg="grey",fg="black").place(x=50,y=220)
        self.ecr_ville_origine = ttk.Combobox(frame1, font=("time new roman", 15), state="readonly")
        self.ecr_ville_origine["values"]=("Selectionner","Ouagadougou","Bobo Dioulasso","Koudougou","Ouahigouya","Djibo","Kaya")
        self.ecr_ville_origine.place(x=50, y=250, width=250)
        self.ecr_ville_origine.current(0)
        #ville d'acceuil
        text_ville_acceuil = Label(frame1, text="Ville d'acceuil",font=("time new roman", 15), bg="grey",fg="black").place(x=370,y=220)
        self.ecr_ville_acceuil = ttk.Combobox(frame1, font=("time new roman", 15), state="readonly")
        self.ecr_ville_acceuil["values"]=("Selectionner","Ouagadougou","Bobo Dioulasso","Koudougou","Ouahigouya","Djibo","Kaya")
        self.ecr_ville_acceuil.place(x=370, y=250, width=250)
        self.ecr_ville_acceuil.current(0)
        #nationaliter
        #text_nationaliter = Label(frame1, text="Nationaliter",font=("time new roman", 15), bg="grey",fg="black").place(x=370,y=220)
        #self.ecr_nationaliter = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        #self.ecr_nationaliter.place(x=370, y=250, width=250)
        #date
        #text_date = Label(frame1, text="Date",font=("time new roman", 15), bg="grey",fg="black").place(x=50,y=100)
        #self.ecr_date = DateEntry(frame1, font=("times new roman", 15), bg="lightgrey", date_pattern="dd/mm/yy")
        #self.ecr_date.place(x=50, y=310, width=250)
        
        btn = Button(frame1, text="Valider",font=("time new roman", 15,"bold"),command=self.formulaire_donnee, bg="cyan",fg="black").place(x=300,y=400)
        
    def formulaire_donnee(self):
        if self.ecr_nom.get()=="" or self.ecr_prenom.get()=="" or self.ecr_date_naissance.get()=="":
            messagebox.showerror("Erreur", "Remplissez tous les champ", parent=self.root)
        try:
            con = sqlite3.connect(database="Mariam")
            cur = con.cursor()
            cur.execute("SELECT * FROM Deplaces WHERE nom=?", self.ecr_nom.get())
            row = cur.fetchone()
            
            if row != None:
                messagebox.showerror("Erreur", "Ce nom existe deja, essayer un autre nom", parent=self.root)
            else:
                cur.execute("INSERT INTO Deplaces(nom, prenom, date_naissance, ville_origine, ville_acceuil), values(?,?,?,?,?)",
                            (self.ecr_nom.get(),
                            self.ecr_prenom.get(),
                            self.ecr_date_naissance.get(),
                            self.ecr_ville_origine.get(),
                            self.ecr_ville_acceuil.get(),
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Ajout effectuer!!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Erreur",f"Erreur de Connexion :{str(es)}", parent = self.root)
    

root=Tk()
obj = formSQLite3(root)
root.mainloop()
