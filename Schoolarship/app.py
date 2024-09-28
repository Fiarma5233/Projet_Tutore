


import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from users.users_authentification import auth_blueprint, create_users_table
from databases.db import get_all_bourses, get_bourse_by_id  # Importer la fonction qui récupère les données de la base
from utils.utils import install_python_dependencies, install_chrome_and_chromedriver

load_dotenv()  # Charge les variables d'environnement à partir du fichier .env
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Charge la clé secrète depuis .env

create_users_table()
# Enregistrer le blueprint pour l'authentification
app.register_blueprint(auth_blueprint)

def get_paginated_opportunities(opportunities, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return opportunities[start:end]

@app.route('/', methods=['GET'])
def index():
    message = request.args.get('message', None)
    is_error = request.args.get('is_error', False)
    search_term = request.args.get('search', '')
    opportunities = get_all_bourses(search_term)
    # Obtenez le numéro de page à partir des paramètres de la requête, avec 1 comme valeur par défaut
    page = request.args.get('page', 1, type=int)
    per_page = 6

    # Obtenez les bourses paginées
    paginated_bourses = get_paginated_opportunities(opportunities['toutes_les_bourses'], page, per_page)

    return render_template(
        'index.html',
        opportunities=paginated_bourses,
        page=page, 
        per_page=per_page,  # Assurez-vous que cette ligne est ajoutée
        total=len(opportunities['toutes_les_bourses']),
        message=message, 
        is_error=is_error)

@app.route('/details/<int:bourse_id>', methods=['GET'])
def details(bourse_id):
    bourse = get_bourse_by_id(bourse_id)  # Récupère la bourse avec l'ID donné
    if bourse:
        return render_template('detail.html', bourse=bourse)  # Remplace 'detail.html' par ton template
    else:
        return "Bourse non trouvée", 404
    
@app.route('/bourses', methods=['GET'])
def afficher_bourses():
    search_term = request.args.get('search', '')
    opportunities = get_all_bourses(search_term)
    return render_template('bourses.html', opportunities=opportunities)

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    install_chrome_and_chromedriver()
    app.run(debug=True, ssl_context=None)

