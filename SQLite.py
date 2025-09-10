import sqlite3
con = sqlite3.connect("escola.db")
cur = con.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")
con.commit()

cur.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
)
""")
con.commit();


cur.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ("Carlos", 20, "Informática"))
cur.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ("Pedro", 22, "Redes"))
con.commit()


cur.execute("SELECT * FROM alunos")
alunos = cur.fetchall()
for aluno in alunos:
    print(aluno)

con.close()
