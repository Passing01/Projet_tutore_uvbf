from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

conn = sqlite3.connect('Burkina_Faso4.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Etudiants(
    id TEXT PRIMARY KEY,
    nom TEXT,
    mail TEXT,
    sexe TEXT,
    contact TEXT,
    date TEXT,
    adresse TEXT
    )''')

class etudiant:
    def __init__(self, root):
        self.root=root
        self.root.title("insription")
        self.root.geometry("1920x1000+0+0")
        #formulaire
        Gestion_frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Gestion_frame.place(x=50,y=25,width=400,height=700)
        
        self.id = StringVar()
        self.nom = StringVar()
        self.mail = StringVar()
        self.sexe = StringVar()
        self.contact = StringVar()
        self.dat = StringVar()
        
        self.recherch_par = StringVar()
        self.recherch = StringVar()
        
        
        gestion_title = Label(Gestion_frame, text="Information de l'etudiant", font=("times new roman", 30, "bold"), bg="cyan")
        gestion_title.place(x=50,y=50)
        
        idEtudiant = Label(Gestion_frame, text="IDEtudiant", font=("times new roman", 20), bg="cyan")
        idEtudiant.place(x=50,y=150)
        
        id_txt = Entry(Gestion_frame, textvariable=self.id, font=("times new roman", 20), bg="lightcyan")
        id_txt.place(x=220,y=150,width=50)
        
        idnomcomple = Label(Gestion_frame, text="Nom complet", font=("times new roman", 20), bg="cyan")
        idnomcomple.place(x=50,y=210)
        
        nom_txt = Entry(Gestion_frame, textvariable=self.nom, font=("times new roman", 20), bg="lightcyan")
        nom_txt.place(x=220,y=210,width=100)
        
        Email = Label(Gestion_frame, text="Email", font=("times new roman", 20), bg="cyan")
        Email.place(x=50,y=260)
        
        email_txt = Entry(Gestion_frame, textvariable=self.mail, font=("times new roman", 20), bg="lightcyan")
        email_txt.place(x=220,y=260,width=100)
        
        Sexe = Label(Gestion_frame, text="Sexe", font=("times new roman", 20), bg="cyan")
        Sexe.place(x=50,y=310)
        
        sexe_txt = ttk.Combobox(Gestion_frame,textvariable=self.sexe, font=("times new roman", 20), state="readonly")
        sexe_txt["values"] = ("Homme", "Femme")
        sexe_txt.place(x=220,y=310, width=100)
        sexe_txt.current(0)
        
        contact = Label(Gestion_frame, text="Contact", font=("times new roman", 20), bg="cyan")
        contact.place(x=50,y=360)
        
        contact_txt = Entry(Gestion_frame, textvariable=self.contact, font=("times new roman", 20), bg="lightcyan")
        contact_txt.place(x=220,y=360,width=100)
        
        Dat = Label(Gestion_frame, text="Date naissance", font=("times new roman", 20), bg="cyan")
        Dat.place(x=50,y=410)
        
        date_txt = Entry(Gestion_frame, textvariable=self.dat, font=("times new roman", 20), bg="lightcyan")
        date_txt.place(x=220,y=410,width=100)
        
        Adresse = Label(Gestion_frame, text="Adresse", font=("times new roman", 20), bg="cyan")
        Adresse.place(x=50,y=460)
        
        self.adresse_txt = Text(Gestion_frame, font=("times new roman", 20))
        self.adresse_txt.place(x=220,y=460,width=100,height=100)
        
        btn_ajouter = Button(Gestion_frame,command=self.ajou_etudiant, text="Ajouter", font=("times new roman",15),bd=10,relief=GROOVE, bg="green")
        btn_ajouter.place(x=10,y=600, width=50)
        
        btn_modifier = Button(Gestion_frame,command=self.modifier, text="Modifier", font=("times new roman",15),bd=10,relief=GROOVE, bg="yellow")
        btn_modifier.place(x=50,y=600, width=50)
        
        btn_supprimer = Button(Gestion_frame,command=self.supprimer, text="Supprimer", font=("times new roman",15),bd=10,relief=GROOVE, bg="red")
        btn_supprimer.place(x=100,y=600, width=50)
        
        btn_reinitialiser = Button(Gestion_frame,command=self.reini, text="Reinitialiser", font=("times new roman",15),bd=10,relief=GROOVE, bg="gray")
        btn_reinitialiser.place(x=150,y=600, width=50)
        
        #Affichage
        Details_frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Details_frame.place(x=500,y=25,width=1100,height=700)
        
        Affiche_resultat = Label(Details_frame, text="Rechercher par", font=("times new roman",30,"bold"), bg="cyan")
        Affiche_resultat.place(x=50,y=50)
        
        rech = ttk.Combobox(Details_frame,textvariable=self.recherch_par, font=("times new roman", 20), state="readonly")
        rech["values"] = ("id", "nom", "contact")
        rech.place(x=250,y=55,width=100,height=40)
        
        rech_txt = Entry(Details_frame,textvariable=self.recherch, font=("times new roman", 20), bd=5, relief=GROOVE)
        rech_txt.place(x=350, y=55, width=250, height=40)
        
        btn_rech = Button(Details_frame,command=self.rechercher_info, text="Rechercher", font=("times new roman", 15), bd=10, bg="grey", relief=GROOVE)
        btn_rech.place(x=510,y=55,width=120, height=40)
        
        btn_afftout = Button(Details_frame, text="Afficher Tout", font=("times new roman", 15), bd=10, bg="grey", relief=GROOVE)
        btn_afftout.place(x=610,y=55,width=135, height=40)
        
        #affichage
        result_frame = Frame(Details_frame, bd=5, relief=GROOVE, bg="white")
        result_frame.place(x=10,y=110,width=1000,height=570)
        
        Scroll_x = Scrollbar(result_frame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(result_frame, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_frame, columns=("id", "nom", "mail", "sexe", "contact", "date", "adresse"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        
        self.tabl_resul.heading("id", text="ID Etudiant")
        self.tabl_resul.heading("nom", text="nom Complet")
        self.tabl_resul.heading("mail", text="E-mail")
        self.tabl_resul.heading("sexe", text="sexe")
        self.tabl_resul.heading("contact", text="contact")
        self.tabl_resul.heading("date", text="Date naissance")
        self.tabl_resul.heading("adresse", text="Adresse")
        
        self.tabl_resul["show"] = "headings"
        
        self.tabl_resul.column("id",width=100)
        self.tabl_resul.column("nom",width=100)
        self.tabl_resul.column("mail",width=100)
        self.tabl_resul.column("sexe",width=100)
        self.tabl_resul.column("contact",width=100)
        self.tabl_resul.column("date",width=100)
        self.tabl_resul.column("adresse",width=150)
        
        self.tabl_resul.pack()
        self.tabl_resul.bind("<ButtonRelease-1>", self.information)
        self.afficherResultat()
        
        
    def ajou_etudiant(self):
        if self.id.get()=="" or self.nom.get()=="" or self.mail.get()=="":
            messagebox.showerror("Erreur", "Vous n'avez pa rempli les champs obigatoire.", parent=self.root)
        else:
            conn = sqlite3.connect('Burkina_Faso4.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO Etudiants values(?,?,?,?,?,?,?)",
                        (
                            self.id.get(), 
                            self.nom.get(), 
                            self.mail.get(), 
                            self.sexe.get(), 
                            self.contact.get(),
                            self.dat.get(),
                            self.adresse_txt.get("1.0", END),
                        ))
            
            conn.commit()
            self.afficherResultat()
            self.reini()
            conn.close()
            messagebox.showinfo("Succes", "Enregistrement effectuer")
            
    def afficherResultat(self):
        conn = sqlite3.connect('Burkina_Faso4.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Etudiants")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("", END, values=row)
        
        conn.commit()
        conn.close()
        
    def reini(self):
        self.id.set("")
        self.nom.set("")
        self.mail.set("")
        self.sexe.set("")
        self.contact.set("")
        self.dat.set("")
        self.adresse_txt.delete("1.0", END)
        
    def information(self,ev):
        cursors_row = self.tabl_resul.focus()
        contents = self.tabl_resul.item(cursors_row)
        row = contents["values"]
        self.id.set(row[0]),
        self.nom.set(row[1]),
        self.mail.set(row[2]),
        self.sexe.set(row[3]),
        self.contact.set(row[4]),
        self.dat.set(row[5]),
        self.adresse_txt.delete("1.0", END)
        self.adresse_txt.insert(END, row[6])
        
    def modifier(self):
        conn = sqlite3.connect('Burkina_Faso4.db')
        cur = conn.cursor()
        cur.execute("UPDATE Etudiants SET nom=?, mail=?, sexe=?, contact=?, date=?, adresse=? WHERE id=?", 
                    (
                        self.nom.get(),
                        self.mail.get(),
                        self.sexe.get(),
                        self.contact.get(),
                        self.dat.get(),
                        self.adresse_txt.get("1.0",END),
                        self.id.get(),
                    ))
        
        conn.commit()
        messagebox.showinfo("Succes", "Modification effectuer")
        self.afficherResultat()
        self.reini()
        conn.close()
        
    def supprimer(self):
        conn = sqlite3.connect('Burkina_Faso4.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM Etudiants WHERE id=?", self.id.get())
        
        conn.commit()
        self.afficherResultat()
        self.reini()
        conn.close()
        
    def rechercher_info(self):
        conn = sqlite3.connect('Burkina_Faso4.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Etudiants WHERE "+str(self.recherch_par.get())+" LIKE '?"+str(self.recherch.get())+"?'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert('', END, values=row)
        conn.commit()
        conn.close()
        
root=Tk()
odj = etudiant(root)
root.mainloop()
