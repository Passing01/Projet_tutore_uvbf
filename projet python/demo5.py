import sqlite3


def setup_db(database_name):
        conn = sqlite3.connect(database_name)
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXIST Login
        (
                id VARCHAR PRIMARY KEY NOT NULL,
                username VARCHAR(128) NOT NULL,
                password VARCHAR(128) NOT NULL
        )
                    """)
       
setup_db('test.db') 