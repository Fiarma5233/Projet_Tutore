

# import os
# from flask import Flask, render_template, request
# #from apscheduler.schedulers.background import BackgroundScheduler
# #from scrapping.scheduler import job
# #from flask import Flask, render_template
# from utils.utils import install_python_dependencies, install_chrome_and_chromedriver
# from scrapping.utils import setup_scraping_environment, configure_chrome, load_env_variables
# #from scrapping.scheduler import run_scheduler_in_background
# #from scrapping.scheduler import run_scheduler_in_background
# from livereload import Server
# from databases.db import get_all_bourses  # Importer la fonction qui récupère les données de la base
# from dotenv import load_dotenv
# from users.users_authentification import auth_blueprint, create_users_table  # Assurez-vous que le chemin est correct
# load_dotenv()  # Charge les variables d'environnement à partir du fichier .env

# app = Flask(__name__)
# app.secret_key = os.getenv("SECRET_KEY")  # Charge la clé secrète depuis .env
# #scheduler = BackgroundScheduler()

# create_users_table()
# # Enregistrer le blueprint pour l'authentification
# app.register_blueprint(auth_blueprint)

# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route pour afficher les bourses
# # @app.route('/bourses')
# # def afficher_bourses():
# #     # Appeler la fonction pour récupérer les bourses depuis la base de données
# #     opportunities = get_all_bourses()

# #     # Passer les données au template pour affichage
# #     return render_template('bourses.html', opportunities=opportunities)


# @app.route('/bourses', methods=['GET'])
# def afficher_bourses():
#     search_term = request.args.get('search', '')
#     opportunities = get_all_bourses(search_term)
#     return render_template('bourses.html', opportunities=opportunities)

# @app.route('/about/')
# def about():
#     return render_template("about.html")


# if __name__ == '__main__':
#     #install_python_dependencies()
#     install_chrome_and_chromedriver()
    
    
#     app.run(debug=True)
#     # server = Server(app.wsgi_app)
#     # server.serve()


import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from users.users_authentification import auth_blueprint, create_users_table
load_dotenv()  # Charge les variables d'environnement à partir du fichier .env
from databases.db import get_all_bourses  # Importer la fonction qui récupère les données de la base

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Charge la clé secrète depuis .env

create_users_table()
# Enregistrer le blueprint pour l'authentification
app.register_blueprint(auth_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bourses', methods=['GET'])
def afficher_bourses():
    search_term = request.args.get('search', '')
    # Remplacer par la fonction appropriée pour récupérer les bourses
    opportunities = get_all_bourses(search_term)
    return render_template('bourses.html', opportunities=opportunities)

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
