import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS users')

sql_create = '''
CREATE TABLE users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT,
    IDADE TEXT,
    CEP TEXT,
    RUA TEXT,
    NUMERO TEXT,
    CIDADE TEXT,
    ESTADO TEXT,
    EMAIL TEXT
)
'''

cur.execute(sql_create)

con.commit()
con.close()