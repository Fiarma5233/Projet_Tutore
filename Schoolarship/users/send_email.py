from flask import Flask, request, redirect, url_for, flash
import os
import psycopg2
import smtplib

import requests
from email.mime.text import MIMEText
from dotenv import load_dotenv
from databases.db import get_db_connection, convert_conditions_to_list

# Charger les variables d'environnement
load_dotenv()



# Configuration pour l'envoi d'e-mails
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME")  # Ton adresse Gmail
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Ton mot de passe ou App Password

def get_stages_and_users():
    # Connexion à la base de données PostgreSQL
    conn = get_db_connection()
    
    cur = conn.cursor()
    
    # Récupérer tous les stages
    cur.execute("SELECT * FROM opportunities_etudes WHERE type = 'Stage'")
    stages = cur.fetchall()
    
    # Récupérer les emails et noms des utilisateurs
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return stages, users


from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

# def send_stages_email_to_users():
#     # Récupérer les stages et les utilisateurs
#     stages, users = get_stages_and_users()
    
#     # Configuration de l'environnement Jinja2 pour charger les templates
#     env = Environment(loader=FileSystemLoader('templates'))
#     env.globals['url_for'] = url_for  # Ajoute url_for aux globals de Jinja2

#     template = env.get_template('detail.html')  # Template HTML créé auparavant
    
#     # Connexion au serveur SMTP
#     try:
#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()
#         server.login(SMTP_USERNAME, SMTP_PASSWORD)
#     except smtplib.SMTPException as e:
#         print(f"Erreur lors de la connexion au serveur SMTP : {e}")
#         return
    
   
#     for user in users:
#         email = user[1]  # Assumant que l'email est dans la quatrième colonne (index 3)
#         name = user[2]   # Assumant que le nom est dans la deuxième colonne (index 1)
        
#         # Préparation du sujet et du contenu de l'email
#         subject = "Dernières opportunités de stage disponibles"
        
#         # Rendu du template avec les données utilisateur et stages
#         html_content = template.render(nom=name, stages=stages)
        
#         # Création du message
#         msg = MIMEMultipart("alternative")
#         msg["Subject"] = subject
#         msg["From"] = SMTP_USERNAME
#         msg["To"] = email
        
#         # Attacher le contenu HTML à l'email
#         msg.attach(MIMEText(html_content, 'html'))
        
#         # Envoi de l'email
#         try:
#             server.sendmail(SMTP_USERNAME, email, msg.as_string())
#             print(f"E-mail envoyé avec succès à {email}")
#         except smtplib.SMTPException as e:
#             print(f"Erreur lors de l'envoi de l'e-mail à {email}: {e}")
    
#     # Fermer la connexion SMTP
#     server.quit()



def send_stages_email_to_users():
    # Récupérer les stages et les utilisateurs
    stages, users = get_stages_and_users()
    
    # Configuration de l'environnement Jinja2 pour charger les templates
    env = Environment(loader=FileSystemLoader('templates'))
    env.globals['url_for'] = url_for  # Ajoute url_for aux globals de Jinja2

    template = env.get_template('email.html')  # Template HTML créé auparavant
    
    # Connexion au serveur SMTP
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
    except smtplib.SMTPException as e:
        print(f"Erreur lors de la connexion au serveur SMTP : {e}")
        return
    
    for user in users:
        email = user[1]  # Assumant que l'email est dans la deuxième colonne (index 1)
        name = user[2]   # Assumant que le nom est dans la troisième colonne (index 2)
        
        # Préparation du sujet et du contenu de l'email
        subject = "Dernières opportunités de stage disponibles"
        
        # Rendu du template avec les données utilisateur et stages
        html_content = template.render(nom=name, stages=stages)
        
        # Création du message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = SMTP_USERNAME
        msg["To"] = email
        
        # Attacher le contenu HTML à l'email
        msg.attach(MIMEText(html_content, 'html'))
        
        # Envoi de l'email
        try:
            server.sendmail(SMTP_USERNAME, email, msg.as_string())
            print(f"E-mail envoyé avec succès à {email}")
        except smtplib.SMTPException as e:
            print(f"Erreur lors de l'envoi de l'e-mail à {email}: {e}")
    
    # Fermer la connexion SMTP
    server.quit()


if __name__ == '__main__':
    get_stages_and_users()
    send_stages_email_to_users()