import sqlite3

DB_PATH = "chinook.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result