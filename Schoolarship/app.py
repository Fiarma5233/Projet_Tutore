


from flask import Flask, render_template, request
#from apscheduler.schedulers.background import BackgroundScheduler
#from scrapping.scheduler import job
#from flask import Flask, render_template
from utils.utils import install_python_dependencies, install_chrome_and_chromedriver
from scrapping.utils import setup_scraping_environment, configure_chrome, load_env_variables
#from scrapping.scheduler import run_scheduler_in_background
#from scrapping.scheduler import run_scheduler_in_background
from livereload import Server
from databases.db import get_all_bourses  # Importer la fonction qui récupère les données de la base

app = Flask(__name__)

#scheduler = BackgroundScheduler()

@app.route('/')
def index():
    return render_template('index.html')

# Route pour afficher les bourses
# @app.route('/bourses')
# def afficher_bourses():
#     # Appeler la fonction pour récupérer les bourses depuis la base de données
#     opportunities = get_all_bourses()

#     # Passer les données au template pour affichage
#     return render_template('bourses.html', opportunities=opportunities)


@app.route('/bourses', methods=['GET'])
def afficher_bourses():
    search_term = request.args.get('search', '')
    opportunities = get_all_bourses(search_term)
    return render_template('bourses.html', opportunities=opportunities)

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    #install_python_dependencies()
    install_chrome_and_chromedriver()
    
    
    app.run(debug=True)
    # server = Server(app.wsgi_app)
    # server.serve()
