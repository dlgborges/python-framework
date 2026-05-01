import sqlite3

def salvar_no_banco(texto):
    conn = sqlite3.connect('./database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS notas(texto TEXT)')
    c.execute('INSERT INTO notas VALUES (?)', (texto,))
    conn.commit()
    conn.close()

def ler_do_banco() -> list:
    conn = sqlite3.connect('./database.db')
    c = conn.cursor() #para poder manusear SQL no Python
    try:
        c.execute('SELECT * FROM notas')
    except sqlite3.OperationalError as error:
        error.__str__()
        
    dados = c.fetchall()
    conn.close()
    return dados
