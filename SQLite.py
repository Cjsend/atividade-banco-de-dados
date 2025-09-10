import sqlite3


con = sqlite3.connect("meubanco.db")
cur = con.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")
con.commit()


cur.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Joao", "joao@email.com"))
cur.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Maria", "maria@email.com"))
con.commit()


cur.execute("SELECT * FROM usuarios")
usuarios = cur.fetchall()

for usuario in usuarios:
    print(usuario)

con.close()