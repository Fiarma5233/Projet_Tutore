import os
import psycopg2
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def get_db_connection():
    """Crée et retourne une connexion à la base de données PostgreSQL."""
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    return conn

# def get_all_bourses():
#     """Récupère toutes les bourses de la base de données."""
#     conn = get_db_connection()
#     cur = conn.cursor()

#     # Exécuter la requête pour récupérer les données des bourses
#     cur.execute('SELECT * FROM opportunities_etudes')
#     bourses = cur.fetchall()

#     # Fermer le curseur et la connexion
#     cur.close()
#     conn.close()

#     return bourses


def get_all_bourses():
    """Récupère toutes les bourses de la base de données, y compris celles du Burkina Faso et d'autres pays."""
    conn = get_db_connection()
    cur = conn.cursor()

    # Exécuter la requête pour récupérer toutes les bourses
    cur.execute('SELECT * FROM opportunities_etudes')
    toutes_les_bourses = cur.fetchall()

    # Exécuter la requête pour récupérer uniquement les bourses du Burkina Faso
    cur.execute("SELECT * FROM opportunities_etudes WHERE pays = 'Burkina Faso'")
    bourses_burkina_faso = cur.fetchall()

    # Exécuter d'autres requêtes si nécessaire, par exemple pour le Sénégal
    cur.execute("SELECT * FROM opportunities_etudes WHERE pays = 'Sénégal'")
    bourses_senegal = cur.fetchall()

    # Fermer le curseur et la connexion
    cur.close()
    conn.close()

    # Retourner un dictionnaire contenant toutes les bourses et les bourses par pays
    return {
        'toutes_les_bourses': toutes_les_bourses,
        'bourses_burkina_faso': bourses_burkina_faso,
        'bourses_senegal': bourses_senegal
    }