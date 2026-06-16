import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def salvar_cep(dados: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO consultas_cep (cep, logradouro, bairro, cidade, estado)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        dados.get("cep"),
        dados.get("logradouro"),
        dados.get("bairro"),
        dados.get("localidade"),
        dados.get("uf")
    ))
    conn.commit()
    cursor.close()
    conn.close()

def listar_ceps():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cep, logradouro, bairro, cidade, estado, consultado_em
        FROM consultas_cep
        ORDER BY consultado_em DESC
    """)
    registros = cursor.fetchall()
    cursor.close()
    conn.close()
    return registros