
import pandas as pd
import numpy as np
from datetime import datetime
from sqlalchemy import create_engine
from scrapping.bourses_campusfaso import scraper_bourses_campusfaso
from scrapping.bourses_greatyop import get_total_pages, generate_page_urls,extract_links_from_pages, extract_bourse_info_from_urls


def scrape_and_store_data():
    try:
       

        # Scraping des données
        df_bourses_campusfaso = scraper_bourses_campusfaso()
        
        url_bourses = 'https://greatyop.com/category/bourses/'
        total_pages_bourses = get_total_pages(url_bourses)
        
        url_stages = 'https://greatyop.com/category/stages-emplois/'
        total_pages_stages = get_total_pages(url_stages)
        
        url_formations = 'https://greatyop.com/category/formations/'
        total_pages_formations = get_total_pages(url_formations)
        
        urls_pages_bourses = generate_page_urls(url_bourses, total_pages_bourses)
        urls_pages_stages = generate_page_urls(url_stages, total_pages_stages)
        urls_pages_formations = generate_page_urls(url_formations, total_pages_formations)
        
        liens_bourses = extract_links_from_pages(urls_pages_bourses)
        liens_stages = extract_links_from_pages(urls_pages_stages)
        liens_formations = extract_links_from_pages(urls_pages_formations)
        
        bourses = extract_bourse_info_from_urls(liens_bourses)
        df_bourses = pd.DataFrame(bourses)
        
        stages = extract_bourse_info_from_urls(liens_stages)
        df_stages = pd.DataFrame(stages)
        df_stages['Type'] = 'Stage'
        
        formations = extract_bourse_info_from_urls(liens_formations)
        df_formations = pd.DataFrame(formations)
        df_formations['Type'] = 'Formation'
        
        # Concaténer tous les DataFrames
        df = pd.concat([df_bourses_campusfaso, df_bourses, df_stages, df_formations], ignore_index=True)
        
        # Nettoyage des données
        # Remplacer les valeurs manquantes par NaN
        df['Date Limite'].replace('Date limite non spécifiée', np.nan, inplace=True)
        
        # Convertir 'Nombre de bourses' en entier
        #df['Nombre de bourses'] = pd.to_numeric(df['Nombre de bourses'], errors='coerce')
        
        # Convertir 'Date Limite' en format datetime
        def parse_date(date_str):
            if pd.isnull(date_str):
                return pd.NaT
            for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
            return pd.NaT
        
        df['Date Limite'] = df['Date Limite'].apply(parse_date)
        
        # Supprimer les doublons
        df.drop_duplicates(inplace=True)
        
        # Enregistrer le DataFrame nettoyé dans un fichier CSV
        df.to_csv('cleaned_opportunities_etudes.csv', index=False)
        
        # Enregistrer les données dans PostgreSQL
        db_url = 'postgresql://opportunities:scholarship@localhost:5432/study_opportunities'
        engine = create_engine(db_url)
        
        df.to_sql('opportunities_etudes', engine, if_exists='replace', index=False, dtype={
            'Pays': 'VARCHAR',
            'Titre': 'VARCHAR',
            'Type': 'VARCHAR',
            'Description': 'TEXT',
            'Niveau': 'VARCHAR',
            'Financement': 'VARCHAR',
            'Conditions': 'TEXT',
            'Domaine Conserné': 'VARCHAR',
            'Durée d\'étude': 'VARCHAR',
            'Pays éligibles': 'VARCHAR',
            'Date Limite': 'DATE',
            'Nombre de bourses': 'VARCHAR'
        })
        
        print("Scraping terminé, données nettoyées et stockées dans PostgreSQL.")
    
    except Exception as e:
        print(f"Erreur lors du processus: {str(e)}")

# Appeler la fonction pour exécuter le processus complet
#scrape_and_store_data()
