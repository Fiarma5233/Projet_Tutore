
# import pandas as pd
# import numpy as np

# from datetime import datetime
# from sqlalchemy import create_engine
# import psycopg2

# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes pour correspondre aux noms des champs dans la table SQL (en minuscules)
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Vérification des types de données pour la colonne 'date_limite'
# #df['date_limite'] = pd.to_datetime(df['date_limite'], errors='coerce')

# # Insertion des données dans la base de données PostgreSQL
# #df.to_sql('opportunities_etudes', engine, if_exists='append', index=False)


# df['date_limite'] = df['date_limite'].replace('Date limite non spécifiée', np.nan)

# # Convertir 'Date Limite' en format datetime
# def parse_date(date_str):
#     if pd.isnull(date_str):
#         return pd.NaT
#     for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
#         try:
#             return datetime.strptime(date_str, fmt)
#         except ValueError:
#             continue
#     return pd.NaT


# df['date_limite'] = df['date_limite'].apply(parse_date)

# # Supprimer les doublons
# df.drop_duplicates(inplace=True)

# print(df)

# # creating connexion
# conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     password='scholarship',
#     user='opportunities',
#     database='study_opportunities'
# )


# cursor_postgres = conn.cursor()

# create_postgres_query_file = open("./databases/postgres_create_tables.sql")
# create_postgres_query = create_postgres_query_file.read()

# cursor_postgres.execute(create_postgres_query)

# # commiting 
# conn.commit()

# # Enregistrer les données dans PostgreSQL
# # db_url = 'postgresql://opportunities:scholarship@localhost:5432/study_opportunities'
# #engine = create_engine(db_url)
# # engine creating to avoid warning
# engine = create_engine("postgresql+psycopg2://", creator=lambda:conn)

# a = pd.read_sql("SELECT * FROM opportunities_etudes;", con=engine)

# print(a)

# # on crrer une liste de donnees
# data = list( df.itertuples(index=None, name=None))

# # apres avoir creer le fichier contenant la requete d'insertion des donnees dans la table universite dans le dossier sql, on charge le fichier sql pour creer la table dans mysql
# merge_postgres_query_file = open('./databases/postgres_upsert.sql')
# merge_postgres_query = merge_postgres_query_file.read() # lecture 

# pd.read_sql("SELECT * FROM opportunities_etudes;", con=engine)


# import pandas as pd
# import numpy as np
# from datetime import datetime
# import psycopg2

# # Charger les données depuis le fichier CSV
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes pour correspondre aux champs de la table SQL (en minuscules)
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Remplacer les valeurs "Date limite non spécifiée" par NaN
# df['date_limite'] = df['date_limite'].replace('Date limite non spécifiée', np.nan)

# # Fonction pour convertir les dates au format datetime
# def parse_date(date_str):
#     if pd.isnull(date_str):
#         return pd.NaT
#     for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
#         try:
#             return datetime.strptime(date_str, fmt)
#         except ValueError:
#             continue
#     return pd.NaT

# # Appliquer la fonction de conversion sur la colonne 'date_limite'
# df['date_limite'] = df['date_limite'].apply(parse_date)

# # Supprimer les doublons
# df.drop_duplicates(inplace=True)

# # Connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='opportunities',
#     password='scholarship',
#     database='study_opportunities'
# )

# cursor_postgres = conn.cursor()

# # Charger la requête d'insertion depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as merge_postgres_query_file:
#     merge_postgres_query = merge_postgres_query_file.read()

# # Itérer sur chaque ligne du DataFrame et insérer les données
# for row in df.itertuples(index=False, name=None):
#     cursor_postgres.execute(merge_postgres_query, row)

# # Valider les transactions
# conn.commit()

# # Vérification : Exécuter une requête pour voir si les données sont bien insérées
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()
# for row in rows:
#     print(row)

# # Fermer la connexion
# cursor_postgres.close()
# conn.close()


# import pandas as pd
# import numpy as np
# from datetime import datetime
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes pour correspondre aux champs de la table SQL (en minuscules)
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Conserver les URLs et valeurs spéciales dans la colonne 'date_limite'
# # On ne remplace pas les valeurs spéciales ici

# # Fonction pour convertir les dates au format datetime, si elles sont valides
# def parse_date(date_str):
#     if pd.isnull(date_str) or (isinstance(date_str, str) and date_str.startswith('http')):
#         return date_str  # Conserver les URLs et NaN
#     for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
#         try:
#             return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')  # Format pour la base de données
#         except ValueError:
#             continue
#     return date_str

# # Appliquer la fonction de conversion sur la colonne 'date_limite'
# df['date_limite'] = df['date_limite'].apply(parse_date)

# # Supprimer les doublons
# df.drop_duplicates(inplace=True)

# # Connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='opportunities',
#     password='scholarship',
#     database='study_opportunities'
# )

# cursor_postgres = conn.cursor()

# # Charger et exécuter la requête de création de table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()

# # Charger la requête d'insertion depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en liste de tuples
# data = list(df.itertuples(index=False, name=None))

# # Insérer les données dans la base de données
# try:
#     execute_values(cursor_postgres, merge_postgres_query, data)
#     conn.commit()
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()

# # Vérification : Exécuter une requête pour voir toutes les données
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()
# for row in rows:
#     print(row)

# # Fermer la connexion
# cursor_postgres.close()
# conn.close()


# import pandas as pd
# import numpy as np
# from datetime import datetime
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes pour correspondre aux champs de la table SQL (en minuscules)
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Conserver les URLs et les chaînes non valides dans une nouvelle colonne
# df['date_limite_raw'] = df['date_limite']

# # Fonction pour convertir les dates au format datetime
# def parse_date(date_str):
#     if pd.isnull(date_str):
#         return pd.NaT  # Retourner NaT pour les valeurs NaN
#     for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
#         try:
#             return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')  # Format pour la base de données
#         except ValueError:
#             continue
#     return np.nan  # Retourner NaN pour les chaînes non valides

# # Convertir les dates et conserver les chaînes non valides ou les URLs
# df['date_limite'] = df['date_limite'].apply(lambda x: parse_date(x) if pd.notna(x) and not x.startswith('http') and x != 'Date limite non spécifiée' else np.nan)

# # Supprimer les doublons
# df.drop_duplicates(inplace=True)

# # Connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='opportunities',
#     password='scholarship',
#     database='study_opportunities'
# )

# cursor_postgres = conn.cursor()

# # Charger et exécuter la requête de création de table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()

# # Charger la requête d'insertion depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en liste de tuples
# data = list(df.itertuples(index=False, name=None))

# # Insérer les données dans la base de données
# try:
#     execute_values(cursor_postgres, merge_postgres_query, data)
#     conn.commit()
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()

# # Vérification : Exécuter une requête pour voir toutes les données
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()
# for row in rows:
#     print(row)

# # Fermer la connexion
# cursor_postgres.close()
# conn.close()


# import pandas as pd
# import numpy as np
# from datetime import datetime
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes pour correspondre aux champs de la table SQL (en minuscules)
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Conserver les URLs et les chaînes non valides dans une nouvelle colonne
# df['date_limite_raw'] = df['date_limite']

# # Fonction pour convertir les dates au format datetime
# def parse_date(date_str):
#     if pd.isnull(date_str):
#         return pd.NaT  # Retourner NaT pour les valeurs NaN
#     for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
#         try:
#             return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')  # Format pour la base de données
#         except ValueError:
#             continue
#     return np.nan  # Retourner NaN pour les chaînes non valides

# # Convertir les dates et conserver les chaînes non valides ou les URLs
# df['date_limite'] = df['date_limite'].apply(lambda x: parse_date(x) if pd.notna(x) and not x.startswith('http') and x != 'Date limite non spécifiée' else np.nan)

# # Supprimer les doublons
# df.drop_duplicates(inplace=True)

# # Afficher les données pour déboguer
# print(df.head())
# print(df.columns)

# # Connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='opportunities',
#     password='scholarship',
#     database='study_opportunities'
# )

# cursor_postgres = conn.cursor()

# # Charger et exécuter la requête de création de table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()

# # Charger la requête d'insertion depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en liste de tuples
# data = list(df.itertuples(index=False, name=None))

# # Afficher les données pour déboguer
# print("Data to insert:")
# for row in data[:15]:  # Afficher seulement les 5 premières lignes pour éviter l'encombrement
#     print(row)

# # Insérer les données dans la base de données
# try:
#     execute_values(cursor_postgres, merge_postgres_query, data)
#     conn.commit()
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()

# # Vérification : Exécuter une requête pour voir toutes les données
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()
# for row in rows:
#     print(row)

# # Fermer la connexion
# cursor_postgres.close()
# conn.close()


# import pandas as pd
# import numpy as np
# from datetime import datetime
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes pour correspondre aux champs de la table SQL (en minuscules)
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Fonction pour convertir les dates au format datetime
# def parse_date(date_str):
#     if pd.isnull(date_str):
#         return pd.NaT  # Retourner NaT pour les valeurs NaN
#     for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%d %B %Y'):
#         try:
#             return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')  # Format pour la base de données
#         except ValueError:
#             continue
#     return np.nan  # Retourner NaN pour les chaînes non valides

# # Convertir les dates et conserver les chaînes non valides ou les URLs
# df['date_limite'] = df['date_limite'].apply(lambda x: parse_date(x) if pd.notna(x) and not x.startswith('http') and x != 'Date limite non spécifiée' else np.nan)

# # Supprimer les doublons
# df.drop_duplicates(inplace=True)

# # Afficher les données pour déboguer
# print(df.head())
# print(df.columns)

# # Connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='opportunities',
#     password='scholarship',
#     database='study_opportunities'
# )

# cursor_postgres = conn.cursor()

# # Charger et exécuter la requête de création de table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()

# # Charger la requête d'insertion depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en liste de tuples
# data = list(df.itertuples(index=False, name=None))

# # Afficher les données pour déboguer
# print("Data to insert:")
# for row in data[:5]:  # Afficher seulement les 5 premières lignes pour éviter l'encombrement
#     print(row)

# # Insérer les données dans la base de données
# try:
#     execute_values(cursor_postgres, merge_postgres_query, data)
#     conn.commit()
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()

# # Vérification : Exécuter une requête pour voir toutes les données
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()
# for row in rows:
#     print(row)

# # Fermer la connexion
# cursor_postgres.close()
# conn.close()


# # Importer les bibliothèques nécessaires
# import pandas as pd
# import numpy as np
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV dans un DataFrame Pandas
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes du DataFrame pour qu'elles correspondent aux champs de la table SQL
# # Cette étape facilite l'insertion des données dans la base de données
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Aucun traitement particulier n'est fait sur la colonne 'date_limite' ; elle est conservée telle quelle
# # Les valeurs invalides, telles que les chaînes de caractères non valides ou les URLs, sont conservées

# # Supprimer les doublons du DataFrame pour éviter l'insertion de lignes identiques dans la base de données
# df.drop_duplicates(inplace=True)

# # Afficher les premières lignes du DataFrame et les noms des colonnes pour vérifier les données
# print(df.head())
# print(df.columns)
# print(df.dtypes)


# # Connexion à la base de données PostgreSQL avec les paramètres spécifiés
# conn = psycopg2.connect(
#     host='localhost',      # Adresse du serveur de base de données
#     port=5432,             # Port sur lequel le serveur écoute
#     user='opportunities',  # Nom d'utilisateur pour se connecter à la base de données
#     password='scholarship',# Mot de passe de l'utilisateur
#     database='study_opportunities'  # Nom de la base de données
# )

# # Créer un curseur pour exécuter des requêtes SQL
# cursor_postgres = conn.cursor()

# # Charger et lire la requête SQL pour créer la table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# # Essayer d'exécuter la requête de création de table
# # Si la table existe déjà, l'opération ne posera pas de problème
# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Charger et lire la requête SQL pour insérer ou mettre à jour les données depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en une liste de tuples, où chaque tuple représente une ligne de données
# data = list(df.itertuples(index=None, name=None))

# # Afficher les premières lignes de données pour vérifier avant l'insertion
# print("Data to insert:")
# for row in data[:5]:  # Afficher seulement les 5 premières lignes pour éviter l'encombrement
#     print(row)

# # Essayer d'exécuter la requête d'insertion ou de mise à jour des données dans la base de données
# try:
#     #execute_values(cursor_postgres, merge_postgres_query, data)
#     cursor_postgres.executemany(merge_postgres_query, data)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Vérifier les données insérées en exécutant une requête SELECT pour récupérer toutes les données de la table
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()  # Récupérer toutes les lignes de résultats
# for row in rows:
#     print(row)  # Afficher chaque ligne de résultat

# # Fermer le curseur et la connexion à la base de données
# cursor_postgres.close()
# conn.close()


# # Importer les bibliothèques nécessaires
# import pandas as pd
# import numpy as np
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV dans un DataFrame Pandas
# df = pd.read_csv("opportunities_etudes.csv")

# # Renommer les colonnes du DataFrame pour qu'elles correspondent aux champs de la table SQL
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Fonction pour formater la colonne 'conditions'
# def format_conditions(conditions):
#     if isinstance(conditions, str) and conditions.startswith('[') and conditions.endswith(']'):
#         # Supprimer les crochets et les espaces superflus
#         links = conditions.strip('[]').replace("'", "").split(',')
#         # Joindre les liens avec une délimitation appropriée
#         return ', '.join(link.strip() for link in links)
#     return conditions

# # Appliquer le formatage à la colonne 'conditions'
# df['conditions'] = df['conditions'].apply(format_conditions)

# # Supprimer les doublons du DataFrame pour éviter l'insertion de lignes identiques dans la base de données
# df.drop_duplicates(inplace=True)

# # Afficher les premières lignes du DataFrame et les noms des colonnes pour vérifier les données
# print(df.head())
# print(df.columns)
# print(df.dtypes)

# # Connexion à la base de données PostgreSQL avec les paramètres spécifiés
# conn = psycopg2.connect(
#     host='localhost',      # Adresse du serveur de base de données
#     port=5432,             # Port sur lequel le serveur écoute
#     user='opportunities',  # Nom d'utilisateur pour se connecter à la base de données
#     password='scholarship',# Mot de passe de l'utilisateur
#     database='study_opportunities'  # Nom de la base de données
# )

# # Créer un curseur pour exécuter des requêtes SQL
# cursor_postgres = conn.cursor()

# # Charger et lire la requête SQL pour créer la table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# # Essayer d'exécuter la requête de création de table
# # Si la table existe déjà, l'opération ne posera pas de problème
# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Charger et lire la requête SQL pour insérer ou mettre à jour les données depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en une liste de tuples, où chaque tuple représente une ligne de données
# data = list(df.itertuples(index=None, name=None))

# # Afficher les premières lignes de données pour vérifier avant l'insertion
# print("Data to insert:")
# for row in data[:5]:  # Afficher seulement les 5 premières lignes pour éviter l'encombrement
#     print(row)

# # Essayer d'exécuter la requête d'insertion ou de mise à jour des données dans la base de données
# try:
#     cursor_postgres.executemany(merge_postgres_query, data)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Vérifier les données insérées en exécutant une requête SELECT pour récupérer toutes les données de la table
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()  # Récupérer toutes les lignes de résultats
# for row in rows:
#     print(row)  # Afficher chaque ligne de résultat

# # Fermer le curseur et la connexion à la base de données
# cursor_postgres.close()
# conn.close()


# # Importer les bibliothèques nécessaires
# import pandas as pd
# import numpy as np
# import psycopg2
# from psycopg2.extras import execute_values

# # Charger les données depuis le fichier CSV dans un DataFrame Pandas
# df = pd.read_csv("stages.csv")

# # Renommer les colonnes du DataFrame pour qu'elles correspondent aux champs de la table SQL
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # # Fonction pour formater la colonne 'conditions'
# # def format_conditions(conditions):
# #     if isinstance(conditions, str):
# #         # Vérifier si les conditions sont au format liste entre crochets
# #         if conditions.startswith('[') and conditions.endswith(']'):
# #             # Supprimer les crochets et les guillemets simples, séparer par des virgules
# #             links = conditions.strip('[]').replace("'", "").split(',')
# #             # Nettoyer chaque lien en supprimant les espaces superflus
# #             return ', '.join(link.strip() for link in links)
# #     return conditions

# # # Appliquer le formatage à la colonne 'conditions'
# # df['conditions'] = df['conditions'].apply(format_conditions)

# # Supprimer les doublons du DataFrame pour éviter l'insertion de lignes identiques dans la base de données
# df.drop_duplicates(inplace=True)


# # Afficher les premières lignes du DataFrame et les noms des colonnes pour vérifier les données
# print(df.head())
# df = df.drop(columns=['Unnamed: 0'])

# print(df.columns)
# print(df.dtypes)

# # Connexion à la base de données PostgreSQL avec les paramètres spécifiés
# conn = psycopg2.connect(
#     host='localhost',      # Adresse du serveur de base de données
#     port=5432,             # Port sur lequel le serveur écoute
#     user='opportunities',  # Nom d'utilisateur pour se connecter à la base de données
#     password='scholarship',# Mot de passe de l'utilisateur
#     database='study_opportunities'  # Nom de la base de données
# )

# # Créer un curseur pour exécuter des requêtes SQL
# cursor_postgres = conn.cursor()

# # Charger et lire la requête SQL pour créer la table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# # Essayer d'exécuter la requête de création de table
# # Si la table existe déjà, l'opération ne posera pas de problème
# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Charger et lire la requête SQL pour insérer ou mettre à jour les données depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     merge_postgres_query = file.read()

# # Convertir le DataFrame en une liste de tuples, où chaque tuple représente une ligne de données
# data = list(df.itertuples(index=None, name=None))

# # Afficher les premières lignes de données pour vérifier avant l'insertion
# print("Data to insert:")
# # for row in data[:5]:  # Afficher seulement les 5 premières lignes pour éviter l'encombrement
# #     print(row)

# data = data[:5]

# # Essayer d'exécuter la requête d'insertion ou de mise à jour des données dans la base de données
# try:
#     #execute_values(cursor_postgres, merge_postgres_query, data)
#     print(df.columns)
#     print(len(df.columns))
#     cursor_postgres.executemany(merge_postgres_query, data)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("Les données ont été insérées ou mises à jour avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Vérifier les données insérées en exécutant une requête SELECT pour récupérer toutes les données de la table
# cursor_postgres.execute("SELECT * FROM opportunities_etudes;")
# rows = cursor_postgres.fetchall()  # Récupérer toutes les lignes de résultats
# for row in rows:
#     print(row)  # Afficher chaque ligne de résultat

# # Fermer le curseur et la connexion à la base de données
# cursor_postgres.close()
# conn.close()


# # Importer les bibliothèques nécessaires
# import pandas as pd
# import psycopg2
# from psycopg2 import sql

# # Charger les données depuis le fichier CSV dans un DataFrame Pandas
# df = pd.read_csv("stages.csv")

# # Supprimer la colonne "Unnamed: 0" si elle existe
# if 'Unnamed: 0' in df.columns:
#     df = df.drop(columns=['Unnamed: 0'])

# # Renommer les colonnes du DataFrame pour qu'elles correspondent aux champs de la table SQL
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Vérifier le DataFrame après les transformations
# print(df.head())  # Afficher les premières lignes pour vérifier
# print(df.columns)  # Vérifier les colonnes après renommage
# print(df.dtypes)   # Vérifier les types de données des colonnes

# # Connexion à la base de données PostgreSQL avec les paramètres spécifiés
# try:
#     conn = psycopg2.connect(
#         host='localhost',      # Adresse du serveur de base de données
#         port=5432,             # Port sur lequel le serveur écoute
#         user='opportunities',  # Nom d'utilisateur pour se connecter à la base de données
#         password='scholarship',# Mot de passe de l'utilisateur
#         database='study_opportunities'  # Nom de la base de données
#     )
#     print("Connexion réussie à la base de données.")
# except Exception as e:
#     print(f"Erreur de connexion : {e}")

# # Créer un curseur pour exécuter des requêtes SQL
# cursor_postgres = conn.cursor()

# # Charger et lire la requête SQL pour créer la table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# # Essayer d'exécuter la requête de création de table
# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Préparer la requête d'insertion SQL
# insert_query = sql.SQL("""
#     INSERT INTO opportunities_etudes (
#         pays, titre, type, description, niveau, financement, date_limite,
#         conditions, nombre_de_bourses, domaine_concerne, duree_d_etude, pays_eligibles
#     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     ON CONFLICT (pays, titre)
#     DO UPDATE SET
#         type = EXCLUDED.type,
#         description = EXCLUDED.description,
#         niveau = EXCLUDED.niveau,
#         financement = EXCLUDED.financement,
#         date_limite = EXCLUDED.date_limite,
#         conditions = EXCLUDED.conditions,
#         nombre_de_bourses = EXCLUDED.nombre_de_bourses,
#         domaine_concerne = EXCLUDED.domaine_concerne,
#         duree_d_etude = EXCLUDED.duree_d_etude,
#         pays_eligibles = EXCLUDED.pays_eligibles;

# """)

# # Convertir le DataFrame en une liste de tuples pour l'insertion
# data = list(df.itertuples(index=False, name=None))

# # Insérer les données dans la table PostgreSQL
# try:
#     cursor_postgres.executemany(insert_query, data)  # Utiliser executemany pour insérer plusieurs lignes à la fois
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("Les données ont été insérées avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Fermer le curseur et la connexion à la base de données
# cursor_postgres.close()
# conn.close()


# # Importer les bibliothèques nécessaires
# import pandas as pd
# import psycopg2
# from psycopg2 import sql

# # Charger les données depuis le fichier CSV dans un DataFrame Pandas
# df = pd.read_csv("formations.csv")

# # Supprimer la colonne "Unnamed: 0" si elle existe
# if 'Unnamed: 0' in df.columns:
#     df = df.drop(columns=['Unnamed: 0'])

# # Renommer les colonnes du DataFrame pour qu'elles correspondent aux champs de la table SQL
# df.rename(columns={
#     'Pays': 'pays',
#     'Titre': 'titre',
#     'Type': 'type',
#     'Description': 'description',
#     'Niveau': 'niveau',
#     'Financement': 'financement',
#     'Date Limite': 'date_limite',
#     'Conditions': 'conditions',
#     'Nombre de bourses': 'nombre_de_bourses',
#     'Domaine Conserné': 'domaine_concerne',
#     'Durée d\'étude': 'duree_d_etude',
#     'Pays éligibles': 'pays_eligibles'
# }, inplace=True)

# # Vérifier le DataFrame après les transformations
# print(df.head())  # Afficher les premières lignes pour vérifier
# print(df.columns)  # Vérifier les colonnes après renommage
# print(df.dtypes)   # Vérifier les types de données des colonnes

# # Connexion à la base de données PostgreSQL avec les paramètres spécifiés
# try:
#     conn = psycopg2.connect(
#         host='localhost',      # Adresse du serveur de base de données
#         port=5432,             # Port sur lequel le serveur écoute
#         user='opportunities',  # Nom d'utilisateur pour se connecter à la base de données
#         password='scholarship',# Mot de passe de l'utilisateur
#         database='study_opportunities'  # Nom de la base de données
#     )
#     print("Connexion réussie à la base de données.")
# except Exception as e:
#     print(f"Erreur de connexion : {e}")

# # Créer un curseur pour exécuter des requêtes SQL
# cursor_postgres = conn.cursor()

# # Charger et lire la requête SQL pour créer la table depuis le fichier SQL
# with open('./databases/postgres_create_tables.sql', 'r') as file:
#     create_table_query = file.read()

# # Essayer d'exécuter la requête de création de table
# try:
#     cursor_postgres.execute(create_table_query)
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("La table a été créée ou existe déjà.")
# except Exception as e:
#     print(f"Erreur lors de la création de la table: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur


# # Charger la requête d'insertion depuis le fichier SQL
# with open('./databases/postgres_upsert.sql', 'r') as file:
#     insert_query = file.read()


# # # Préparer la requête d'insertion SQL
# # insert_query = sql.SQL("""
# #     INSERT INTO opportunities_etudes (
# #         pays, titre, type, description, niveau, financement, date_limite,
# #         conditions, nombre_de_bourses, domaine_concerne, duree_d_etude, pays_eligibles
# #     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# #     ON CONFLICT (pays, titre)
# #     DO UPDATE SET
# #         type = EXCLUDED.type,
# #         description = EXCLUDED.description,
# #         niveau = EXCLUDED.niveau,
# #         financement = EXCLUDED.financement,
# #         date_limite = EXCLUDED.date_limite,
# #         conditions = EXCLUDED.conditions,
# #         nombre_de_bourses = EXCLUDED.nombre_de_bourses,
# #         domaine_concerne = EXCLUDED.domaine_concerne,
# #         duree_d_etude = EXCLUDED.duree_d_etude,
# #         pays_eligibles = EXCLUDED.pays_eligibles;

# # """)

# # Convertir le DataFrame en une liste de tuples pour l'insertion
# data = list(df.itertuples(index=False, name=None))

# # Insérer les données dans la table PostgreSQL
# try:
#     cursor_postgres.executemany(insert_query, data)  # Utiliser executemany pour insérer plusieurs lignes à la fois
#     conn.commit()  # Valider les modifications apportées à la base de données
#     print("Les données ont été insérées avec succès.")
# except Exception as e:
#     print(f"Erreur lors de l'insertion des données: {e}")
#     conn.rollback()  # Annuler les modifications en cas d'erreur

# # Fermer le curseur et la connexion à la base de données
# cursor_postgres.close()
# conn.close()


# Importer les bibliothèques nécessaires
import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine


# Charger les données depuis le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("opportunities_etudes.csv")

# Supprimer la colonne "Unnamed: 0" si elle existe
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Renommer les colonnes du DataFrame pour qu'elles correspondent aux champs de la table SQL
df.rename(columns={
    'Pays': 'pays',
    'Titre': 'titre',
    'Type': 'type',
    'Description': 'description',
    'Niveau': 'niveau',
    'Financement': 'financement',
    'Date Limite': 'date_limite',
    'Conditions': 'conditions',
    'Nombre de bourses': 'nombre_de_bourses',
    'Domaine Conserné': 'domaine_concerne',
    'Durée d\'étude': 'duree_d_etude',
    'Pays éligibles': 'pays_eligibles'
}, inplace=True)

# Vérifier le DataFrame après les transformations
print(df.head())  # Afficher les premières lignes pour vérifier
print(df.columns)  # Vérifier les colonnes après renommage
print(df.dtypes)   # Vérifier les types de données des colonnes

# Connexion à la base de données PostgreSQL avec les paramètres spécifiés
try:
    conn = psycopg2.connect(
        host='localhost',      # Adresse du serveur de base de données
        port=5432,             # Port sur lequel le serveur écoute
        user='opportunities',  # Nom d'utilisateur pour se connecter à la base de données
        password='scholarship',# Mot de passe de l'utilisateur
        database='study_opportunities'  # Nom de la base de données
    )
    print("Connexion réussie à la base de données.")
except Exception as e:
    print(f"Erreur de connexion : {e}")

# Créer un curseur pour exécuter des requêtes SQL
cursor_postgres = conn.cursor()

# Charger et lire la requête SQL pour créer la table depuis le fichier SQL
with open('./databases/postgres_create_tables.sql', 'r') as file:
    create_table_query = file.read()

# Essayer d'exécuter la requête de création de table
try:
    cursor_postgres.execute(create_table_query)
    conn.commit()  # Valider les modifications apportées à la base de données
    print("La table a été créée ou existe déjà.")
except Exception as e:
    print(f"Erreur lors de la création de la table: {e}")
    conn.rollback()  # Annuler les modifications en cas d'erreur

# Préparer la requête d'insertion SQL
insert_query = sql.SQL("""
    INSERT INTO opportunities_etudes (
        pays, titre, type, description, niveau, financement, date_limite,
        conditions, nombre_de_bourses, domaine_concerne, duree_d_etude, pays_eligibles
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (pays, titre)
    DO UPDATE SET
        type = EXCLUDED.type,
        description = EXCLUDED.description,
        niveau = EXCLUDED.niveau,
        financement = EXCLUDED.financement,
        date_limite = EXCLUDED.date_limite,
        conditions = EXCLUDED.conditions,
        nombre_de_bourses = EXCLUDED.nombre_de_bourses,
        domaine_concerne = EXCLUDED.domaine_concerne,
        duree_d_etude = EXCLUDED.duree_d_etude,
        pays_eligibles = EXCLUDED.pays_eligibles;

""")

# Convertir le DataFrame en une liste de tuples pour l'insertion
data = list(df.itertuples(index=False, name=None))

# Insérer les données dans la table PostgreSQL
try:
    cursor_postgres.executemany(insert_query, data)  # Utiliser executemany pour insérer plusieurs lignes à la fois
    conn.commit()  # Valider les modifications apportées à la base de données
    print("Les données ont été insérées avec succès.")
except Exception as e:
    print(f"Erreur lors de l'insertion des données: {e}")
    conn.rollback()  # Annuler les modifications en cas d'erreur


# Utiliser SQLAlchemy pour lire les données si nécessaire
engine = create_engine('postgresql+psycopg2://opportunities:scholarship@localhost:5432/study_opportunities')
try:
    df_read = pd.read_sql("SELECT * FROM opportunities_etudes;", con=engine)
    print(df_read.head())
except Exception as e:
    print(f"Erreur lors de la lecture des données : {e}")

# Fermer le curseur et la connexion à la base de données
cursor_postgres.close()
conn.close()