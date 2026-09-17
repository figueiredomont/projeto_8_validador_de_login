import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
nome_banco = 'cadastro.db'

script_tabela = """CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password  TEXT NOT NULL
            );"""

try:
    with sqlite3.connect(nome_banco) as conn:
        # Cria um cursor
        cur = conn.cursor()

        # Executa o script
        cur.execute(script_tabela)

        # Salva as alterações no banco de dados
        conn.commit()

        print("Tabelas Criadas com Sucesso")
except sqlite3.OperationalError as e:
    print("ERRO: ", e)

def cadastrar_usuario(nome,email,senha):

    script_cadastrar = "INSERT INTO usuarios (username, email, password) VALUES (?,?,?)"
    try:
        with sqlite3.connect(nome_banco) as conn:
                
            # Cria um cursor
            cur = conn.cursor()


            cur.execute(script_cadastrar,(nome,email,senha))


            conn.commit()

        
            
    except sqlite3.OperationalError as e:
        print("ERRO: ", e)

def consultar_usuario(username):
    script_consulte_usuario = """ SELECT * FROM usuarios
                             WHERE username = ?  """

    try:
        with sqlite3.connect(nome_banco) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            cur.execute(script_consulte_usuario,(username,))
            res = cur.fetchone()
            return res 
    except sqlite3.OperationalError as e:
        print("ERRO: ",e)


def validar_login(usuario,senha):
    resultado_consulta = consultar_usuario(usuario)
    if resultado_consulta:
        return check_password_hash(resultado_consulta['password'],senha)
    else:
        return False