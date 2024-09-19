"""
    Import
"""
import json
import os
from flask import Flask, render_template
from utils.utils import install_python_dependencies, install_chrome_and_chromedriver
# from scrapping.bourses_campusfaso import scraper_bourses_campusfaso
# from scrapping.bourses_greatyop import get_total_pages, generate_page_urls,extract_links_from_pages, extract_bourse_info_from_urls
from scrapping.utils import setup_scraping_environment, configure_chrome, load_env_variables
# Configurer l'environnement de scraping
pd, time, webdriver, By, Service, Options, BeautifulSoup = setup_scraping_environment()

from scrapping.study_opportunities import scrape_and_store_data

"""
Oui
"""
app = Flask(__name__)

###############################Execution  unique du script d'installation de chrome et chrome-driver ###############

# # Chemin vers le fichier de configuration JSON
# CONFIG_FILE = 'config.json'

# def load_config():
#     """Charger la configuration depuis le fichier JSON"""
#     if not os.path.exists(CONFIG_FILE):
#         # Si le fichier n'existe pas, créer une configuration par défaut
#         return {"setup_done": False}
#     # Charger la configuration depuis le fichier JSON
#     with open(CONFIG_FILE, 'r') as f:
#         return json.load(f)

# def save_config(config):
#     """Enregistrer la configuration dans le fichier JSON"""
#     with open(CONFIG_FILE, 'w') as f:
#         json.dump(config, f, indent=4)  # Sauvegarder la configuration formatée

# def setup_once():
#     """Exécuter l'installation une seule fois en utilisant un fichier de configuration JSON"""
#     config = load_config()  # Charger la configuration actuelle
#     if not config.get("setup_done", False):
#         # Si l'installation n'a pas été faite, l'exécuter
#         install_python_dependencies()
#         install_chrome_and_chromedriver()
#         # Mettre à jour la configuration pour indiquer que le setup est fait
#         config["setup_done"] = True
#         save_config(config)  # Sauvegarder la configuration mise à jour

############################### Fin d'Execution  unique du script d'installation de chrome et chrome-driver ###############


@app.route('/')

@app.route('/run_scraping')
def run_scraping():
    result = scrape_and_store_data()
    return result


# @app.route('/scrape_campusfaso')
# def scrape_campusfaso():
#     df_bourses_campusfaso = scraper_bourses_campusfaso()
    
#     # Vérifier que le DataFrame contient des données
#     if not df_bourses_campusfaso.empty:
#         # Sauvegarder le DataFrame dans un fichier CSV
#         df_bourses_campusfaso.to_csv("bourses_campusfaso.csv", index=False)
#         return "Scraping de Campus Faso terminé et fichier CSV créé"
#     else:
#         return "Aucune donnée trouvée lors du scraping"
    


# @app.route('/scrape_opportunities_etudes')
# def scrape_opportunities_etudes():

#     # bourses sur campusfaso
#     df_bourses_campusfaso = scraper_bourses_campusfaso()

#     # Sauvegarder le DataFrame dans un fichier CSV
#     df_bourses_campusfaso.to_csv("bourses_campusfaso.csv", index=False)

#     ############## bourses, stages & formations sur greatyop ##

#     url_bourses = 'https://greatyop.com/category/bourses/'
#     # Appeler la fonction et stocker le nombre total de pages dans la variable 'total_pages_bourses'
#     total_pages_bourses = get_total_pages(url_bourses)

#     url_stages = 'https://greatyop.com/category/stages-emplois/'
#     # Appeler la fonction et stocker le nombre total de pages dans la variable 'total_pages_stages'
#     total_pages_stages = get_total_pages(url_stages)

#     url_formations = 'https://greatyop.com/category/formations/'
#     # Appeler la fonction et stocker le nombre total de pages dans la variable 'total_pages_formations'
#     total_pages_formations = get_total_pages(url_formations)


#     urls_pages_bourses = generate_page_urls(url_bourses, total_pages_bourses)

#     urls_pages_stages = generate_page_urls(url_stages, total_pages_stages)

#     urls_pages_formations = generate_page_urls(url_formations, total_pages_formations)


#     liens_bourses = extract_links_from_pages(urls_pages_bourses)

#     liens_stages = extract_links_from_pages(urls_pages_stages)

#     liens_formations = extract_links_from_pages(urls_pages_formations)


#     bourses = extract_bourse_info_from_urls(liens_bourses)
#     df_bourses = pd.DataFrame(bourses)
#     df_bourses.to_csv('bourses.csv')

#     stages = extract_bourse_info_from_urls(liens_stages)
#     df_stages = pd.DataFrame(stages)
#     df_stages['Type'] = 'Stage'
#     df_stages.to_csv('stages.csv')

#     formations = extract_bourse_info_from_urls(liens_formations)
#     df_formations = pd.DataFrame(formations)
#     df_formations['Type'] = 'Formation'
#     df_formations.to_csv('formations.csv')

#     df = pd.concat([df_bourses_campusfaso,df_bourses, df_stages, df_formations], ignore_index=True)
#     df.to_csv('opportunities_etudes.csv')



# @app.route('/scrape_opportunities_etudes')
# def scrape_opportunities_etudes():
#     try:
#         # Scraping des bourses sur CampusFaso
#         df_bourses_campusfaso = scraper_bourses_campusfaso()
        
#         # Vérifier si le DataFrame n'est pas vide
#         if not df_bourses_campusfaso.empty:
#             df_bourses_campusfaso.to_csv("bourses_campusfaso.csv", index=False)
#         else:
#             print("Le DataFrame df_bourses_campusfaso est vide.")
        
#         # Scraping des bourses, stages et formations sur GreatYop
#         url_bourses = 'https://greatyop.com/category/bourses/'
#         total_pages_bourses = get_total_pages(url_bourses)

#         url_stages = 'https://greatyop.com/category/stages-emplois/'
#         total_pages_stages = get_total_pages(url_stages)

#         url_formations = 'https://greatyop.com/category/formations/'
#         total_pages_formations = get_total_pages(url_formations)

#         urls_pages_bourses = generate_page_urls(url_bourses, total_pages_bourses)
#         urls_pages_stages = generate_page_urls(url_stages, total_pages_stages)
#         urls_pages_formations = generate_page_urls(url_formations, total_pages_formations)

#         liens_bourses = extract_links_from_pages(urls_pages_bourses)
#         liens_stages = extract_links_from_pages(urls_pages_stages)
#         liens_formations = extract_links_from_pages(urls_pages_formations)

#         bourses = extract_bourse_info_from_urls(liens_bourses)
#         df_bourses = pd.DataFrame(bourses)
#         if not df_bourses.empty:
#             df_bourses.to_csv('bourses.csv', index=False)
#         else:
#             print("Le DataFrame df_bourses est vide.")
        
#         stages = extract_bourse_info_from_urls(liens_stages)
#         df_stages = pd.DataFrame(stages)
#         if not df_stages.empty:
#             df_stages['Type'] = 'Stage'
#             df_stages.to_csv('stages.csv', index=False)
#         else:
#             print("Le DataFrame df_stages est vide.")
        
#         formations = extract_bourse_info_from_urls(liens_formations)
#         df_formations = pd.DataFrame(formations)
#         if not df_formations.empty:
#             df_formations['Type'] = 'Formation'
#             df_formations.to_csv('formations.csv', index=False)
#         else:
#             print("Le DataFrame df_formations est vide.")
        
#         # Concaténer tous les DataFrames et sauvegarder en CSV
#         if not df_bourses_campusfaso.empty and not df_bourses.empty and not df_stages.empty and not df_formations.empty:
#             df = pd.concat([df_bourses_campusfaso, df_bourses, df_stages, df_formations], ignore_index=True)
#             df.to_csv('opportunities_etudes.csv', index=False)
#         else:
#             print("Un ou plusieurs DataFrames sont vides. Aucun fichier CSV 'opportunities_etudes.csv' n'a été créé.")
        
#         return "Scraping terminé et fichiers CSV créés"

#     except Exception as e:
#         # Afficher les erreurs éventuelles
#         print(f"Erreur lors du scraping ou de la sauvegarde des fichiers CSV: {str(e)}")
#         return f"Erreur lors du scraping ou de la sauvegarde des fichiers CSV: {str(e)}"

def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    install_python_dependencies()
    install_chrome_and_chromedriver() 
    app.run(debug=True)
