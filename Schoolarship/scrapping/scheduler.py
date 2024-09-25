import logging
from scrapping.study_opportunities import scrape_and_store_data
from scrapping.insertion import insert_data_to_postgres

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def job():
    try:
        logging.info("Scraping des données...")
        scrape_and_store_data()

        logging.info("Insertion des données dans PostgreSQL...")
        insert_data_to_postgres('opportunities_etudes.csv', './databases/postgres_create_tables.sql')

        logging.info("Tâche de scraping et d'insertion terminée.")
    except Exception as e:
        logging.error(f"Une erreur s'est produite : {str(e)}")


