import uuid
import sqlite3

conn = sqlite3.connect(r'db/Rahim.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Person(
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    date_naissance INTEGER)
            """)
conn.commit()
conn.close()

class Person:
    def __init__(self, nom, prenom, date_naissance):
        self.identifiant = str(uuid.uuid4())  # Génère un identifiant unique
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

class Annuaire:
    def __init__(self):
        self.personnes = {}  # Dictionnaire pour stocker les personnes

    def enregistrer_personne(self, nom, prenom, date_naissance):
        personne = Person(nom, prenom, date_naissance)
        self.personnes[personne.identifiant] = personne
        print(f"Personne enregistrée avec l'identifiant : {personne.identifiant}")

    def modifier_informations(self, identifiant, nom=None, prenom=None, date_naissance=None):
        if identifiant in self.personnes:
            personne = self.personnes[identifiant]
            if nom:
                personne.nom = nom
            if prenom:
                personne.prenom = prenom
            if date_naissance:
                personne.date_naissance = date_naissance
            print("Informations mises à jour avec succès !")
        else:
            print("Identifiant introuvable.")

    def supprimer_personne(self, identifiant):
        if identifiant in self.personnes:
            del self.personnes[identifiant]
            print("Personne supprimée avec succès !")
        else:
            print("Identifiant introuvable.")

# Exemple d'utilisation
annuaire = Annuaire()
annuaire.enregistrer_personne("Dupont", "Alice", "1990-05-15")
annuaire.enregistrer_personne("Martin", "Bob", "1985-09-20")

# Modifier les informations d'une personne
annuaire.modifier_informations("identifiant_de_la_personne", nom="NouveauNom", prenom="NouveauPrenom")

# Supprimer une personne
annuaire.supprimer_personne("identifiant_de_la_personne")
