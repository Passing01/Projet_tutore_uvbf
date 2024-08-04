import sqlite3

conn = sqlite3.connect('Burkina_Faso.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Deplaces(
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT, 
    date de naissance INTEGER, 
    ville d_origine TEXT, 
    nouvelle ville TEXT)
    """)
def inscrire_deplaces(id, nom, prenom, date_de_naissance, ville_d_origine, nouvelle_ville):
                      cur.execute("INSERT INTO Deplaces(id, nom, prenom, date de naissance, ville d'origine, nouvelle ville) VALUES(? ? ? ? ? ?)",('id','nom','prenom', 'date de naissances', 'ville d''origine', 'nouvelle ville'))
                      conn.commit()
                      print("Le deplaces a ete bien enregistrer")

nom = input("Entrez le nom du deplaces: ")
prenom = input("Entrez le prenom du deplaces: ")
date_de_naissance = int(input("la date de naissance du deplaces: "))
ville_d_origine = input("Entrez la ville d'origine du deplaces: ")
nouvelle_ville = input("Entrez la ville d'acceuille du deplaces: ")

inscrire_deplaces(id, nom, prenom, date_de_naissance, ville_d_origine, nouvelle_ville)

conn.close()
