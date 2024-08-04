import sqlite3

conn = sqlite3.connect('ma_base_de_donnees.db')

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS etudiants")
cur.execute("""CREATE TABLE IF NOT EXISTS etudiants(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenom TEXT,
    age INTEGER,
    classe TEXT)
            """)
cur.execute("""INSERT INTO Etudiants(id, nom, prenom, age, classe) 
            VALUES(1, 'Dupont', 'Jean', 15, '2A')
            """)
cur.execute("""INSERT INTO Etudiants(id, nom, prenom, age, classe) 
            VALUES(2, 'Sawadogo', 'Brice', 16, '2A')
            """)
cur.execute("""INSERT INTO Etudiants(id, nom, prenom, age, classe) 
            VALUES(3, 'Ouedraogo', 'Rahim', 17, '2A')
            """)
cur.execute("""INSERT INTO Etudiants(id, nom, prenom, age, classe) 
            VALUES(4, 'Zongo', 'Claude', 17, '2A')
            """)
conn.commit()
conn.close()
    
