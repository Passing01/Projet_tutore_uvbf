from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import uuid

conn = sqlite3.connect('Burkina_Faso5.db')
cur = conn.cursor()

# Création de la table s'il n'existe pas
cur.execute('''CREATE TABLE IF NOT EXISTS Deplaces1(
    identifiant TEXT PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    date_naissance TEXT,
    ville_origine TEXT,
    nouvelle_ville TEXT
    )''')

class Deplaces:
    def __init__(self, root):
        self.root = root
        self.root.title("Inscription")
        self.root.geometry("1920x1000+0+0")
        
        Gestion_frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Gestion_frame.place(x=10, y=25, width=560, height=600)
        
        self.identifiant = StringVar()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.date_naissance = StringVar()
        self.ville_origine = StringVar()
        self.nouvelle_ville = StringVar()
        
        gestion_title = Label(Gestion_frame, text="Inscription", font=("times new roman", 30, "bold"), bg="cyan")
        gestion_title.place(x=50, y=50)
        
        idnomcomple = Label(Gestion_frame, text="Nom", font=("times new roman", 20), bg="cyan")
        idnomcomple.place(x=50, y=150)
        nom_txt = Entry(Gestion_frame, textvariable=self.nom, font=("times new roman", 20), bg="lightcyan")
        nom_txt.place(x=220, y=150, width=250)
        
        Prenom = Label(Gestion_frame, text="Prenom", font=("times new roman", 20), bg="cyan")
        Prenom.place(x=50, y=200)
        prenom_txt = Entry(Gestion_frame, textvariable=self.prenom, font=("times new roman", 20), bg="lightcyan")
        prenom_txt.place(x=220, y=200, width=250)
        
        Date = Label(Gestion_frame, text="Date naissance", font=("times new roman", 20), bg="cyan")
        Date.place(x=50, y=250)
        date_txt = Entry(Gestion_frame, textvariable=self.date_naissance, font=("times new roman", 20), bg="lightcyan")
        date_txt.place(x=220, y=250, width=250)
        
        ville = Label(Gestion_frame, text="Ville d'origine", font=("times new roman", 20), bg="cyan")
        ville.place(x=50, y=300)
        Ville_txt = ttk.Combobox(Gestion_frame, textvariable=self.ville_origine, font=("times new roman", 20), state="readonly")
        Ville_txt["values"] = ("Ouagadougou", "Bobo Dioulasso", "Ouahigouya", "Fada N'Gourma", "Kaya", "Djibo")
        Ville_txt.place(x=220, y=300, width=250)
        Ville_txt.current(0)
        
        Nouvelle = Label(Gestion_frame, text="Nouvelle Ville", font=("times new roman", 20), bg="cyan")
        Nouvelle.place(x=50, y=350)
        nouvelle_txt = ttk.Combobox(Gestion_frame, textvariable=self.nouvelle_ville, font=("times new roman", 20), state="readonly")
        nouvelle_txt["values"] = ("Ouagadougou", "Bobo Dioulasso", "Ouahigouya", "Fada N'Gourma", "Kaya", "Djibo")
        nouvelle_txt.place(x=220, y=350, width=250)
        nouvelle_txt.current(0)
        
        btn_ajouter = Button(Gestion_frame, command=self.ajou_deplaces, text="Ajouter", font=("times new roman", 15), bd=10, relief=GROOVE, bg="green")
        btn_ajouter.place(x=10, y=450, width=100)
        
        btn_modifier = Button(Gestion_frame,command=self.modifier, text="Modifier", font=("times new roman",15),bd=10,relief=GROOVE, bg="yellow")
        btn_modifier.place(x=100,y=450, width=50)
        
        btn_supprimer = Button(Gestion_frame,command=self.supprimer, text="Supprimer", font=("times new roman",15),bd=10,relief=GROOVE, bg="red")
        btn_supprimer.place(x=200,y=450, width=50)
        
        btn_reinitialiser = Button(Gestion_frame,command=self.reini, text="Reinitialiser", font=("times new roman",15),bd=10,relief=GROOVE, bg="gray")
        btn_reinitialiser.place(x=300,y=450, width=50)
        
        # Autres boutons et partie de l'interface supprimés pour simplifier
        
        # Affichage des données sous forme de tableau
        Details_frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Details_frame.place(x=550, y=25, width=800, height=600)
        
        result_frame = Frame(Details_frame, bd=5, relief=GROOVE, bg="white")
        result_frame.place(x=0, y=50, width=850, height=400)
        
        Scroll_x = Scrollbar(result_frame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(result_frame, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_frame, columns=("id", "nom", "prenom", "date_naissance", "ville_origine", "nouv_ville"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        
        self.tabl_resul.heading("id", text="Identifiant")
        self.tabl_resul.heading("nom", text="Nom")
        self.tabl_resul.heading("prenom", text="Prenom")
        self.tabl_resul.heading("date_naissance", text="Date_naissance")
        self.tabl_resul.heading("ville_origine", text="ville_origine")
        self.tabl_resul.heading("nouv_ville", text="nouv_ville")
        #self.tabl_resul.heading("adresse", text="Adresse")
        
        self.tabl_resul["show"] = "headings"
        
        self.tabl_resul.column("id",width=150)
        self.tabl_resul.column("nom",width=100)
        self.tabl_resul.column("prenom",width=150)
        self.tabl_resul.column("date_naissance",width=120)
        self.tabl_resul.column("ville_origine",width=150)
        self.tabl_resul.column("nouv_ville",width=100)
        #self.tabl_resul.column("adresse",width=200)
        
        # Configuration des colonnes du tableau et bindings
        
        self.tabl_resul.pack()
        self.tabl_resul.bind("<ButtonRelease-1>")
        self.afficherResultat()
        
    def ajou_deplaces(self):
        # Fonction pour ajouter un nouvel enregistrement
        if self.nom.get() == "" or self.prenom.get() == "":
            messagebox.showerror("Erreur", "Vous n'avez pas rempli les champs obligatoires.", parent=self.root)
        else:
            identifiant = str(uuid.uuid4())
            cur.execute("INSERT INTO Deplaces1(identifiant, nom, prenom, date_naissance, ville_origine, nouvelle_ville) values(?,?,?,?,?,?)",
                        (identifiant, self.nom.get(), self.prenom.get(), self.date_naissance.get(), self.ville_origine.get(), self.nouvelle_ville.get()))
            conn.commit()
            self.afficherResultat()
            self.reini()
            messagebox.showinfo("Succes", "Enregistrement effectué")
        
    def afficherResultat(self):
        cur.execute("SELECT * FROM Deplaces1")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("", END, values=row)
        
        conn.commit()
        
    
    def reini(self):
        self.nom.set("")
        self.prenom.set("")
        self.date_naissance.set("")
        self.ville_origine.set("")
        self.nouvelle_ville.set("")
        #self.adresse_txt.delete("1.0", END)
        
    def information(self,ev):
        cursors_row = self.tabl_resul.focus()
        contents = self.tabl_resul.item(cursors_row)
        row = contents["values"]
        self.identifiant.set(row[0]),
        self.nom.set(row[1]),
        self.prenom.set(row[2]),
        self.date_naissance.set(row[3]),
        self.ville_origine.set(row[4]),
        self.nouvelle_ville.set(row[5]),
        
    def modifier(self):
        #conn = sqlite3.connect('Burkina_Faso4.db')
        #cur = conn.cursor()
        identifiant = str(uuid.uuid4())
        cur.execute("UPDATE Deplaces1 SET nom=?, mail=?, sexe=?, contact=?, date=?, adresse=? WHERE identifiant=?", 
                    (
                        identifiant,
                        self.nom.get(),
                        self.prenom.get(),
                        self.date_naissance.get(),
                        self.ville_origine.get(),
                        self.nouvelle_ville.get(),
                    ))
        
        conn.commit()
        messagebox.showinfo("Succes", "Modification effectuer")
        self.afficherResultat()
        self.reini()
        conn.close()
        
    def supprimer(self):
        #conn = sqlite3.connect('Burkina_Faso4.db')
        #cur = conn.cursor()
        identifiant = str(uuid.uuid4())
        cur.execute("DELETE FROM Deplaces1 WHERE identifiant=?", (identifiant))
        
        conn.commit()
        self.afficherResultat()
        self.reini()
        conn.close()
        
    # Autres fonctions simplifiées pour la lisibilité

root = Tk()
obj = Deplaces(root)
root.mainloop()