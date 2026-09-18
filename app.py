import sqlite3
import os

def conectar_banco():
    # CORRETO: Buscando de variável de ambiente, nunca no código
    senha_banco = os.getenv("DB_PASSWORD", "senha_padrao_local")
    print("Conexão estabelecida de forma segura.")

def buscar_usuario(nome_usuario):
    # CORRETO: Uso de parâmetros (?) para evitar SQL Injection
    conn = sqlite3.connect('banco_exemplo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = ?"
    cursor.execute(query, (nome_usuario,))
    return cursor.fetchall()