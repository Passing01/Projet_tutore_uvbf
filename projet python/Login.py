import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Connection")
        self.root.geometry("1500x780+230+250")
        self.root.config(bg="white")
        self.root.focus_force()
        
        login_frame = Frame(self.root, bg="cyan")
        login_frame.place(x=500, y=130, width=500, height=500)
        
        title = Label(login_frame, text="Connexion", font=("algerian",40,"bold"), bg="cyan",fg="black")
        title.pack(side=TOP,fill=X)
        
        lbl_email = Label(login_frame, text="E-mail", font=("times new roman", 30, "bold"), bg="cyan").place(x=150,y=100,width=200)
        lbl_password = Label(login_frame, text="Password", font=("times new roman", 30, "bold"), bg="cyan").place(x=150,y=200,width=200)
        
        self.text_email = Entry(login_frame, font=("times new roman", 20), bg="lightgray")
        self.text_email.place(x=100,y=160,width=320)
        
        self.text_password = Entry(login_frame,show="*", font=("times new roman", 20), bg="lightgray")
        self.text_password.place(x=100,y=270,width=320)
        
        creer_btn= Button(login_frame, text="Creer un nouveau compte", cursor="hand2", font=("times new roman",15), bd=0, bg="cyan",fg="green").place(x=30, y=320)
        obli_btn= Button(login_frame, text="Mot de passe oublie", cursor="hand2", font=("times new roman",15), bd=0, bg="cyan",fg="red").place(x=300, y=320)
        
        connect_btn= Button(login_frame, text="Connexion", cursor="hand2", font=("times new roman",15), bd=0, bg="lightgray",fg="green").place(x=190, y=370)
        
    def Connection(self):
        if self.text_email.get()==""or self.text_password.get()=="":
            messagebox.showerror("Erreur","Veillez saisir l'email et le mot de passe", parent=self.root)
        else:
            try:
                pass
            except Exception as ex:
                messagebox.showerror("Erreur",f"Erreur de connexion{str(ex)}", parent=self.root)
root=Tk()
obj = Login(root)
root.mainloop()