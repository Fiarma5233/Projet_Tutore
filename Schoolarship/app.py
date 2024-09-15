"""
    Import
"""

from flask import Flask, render_template
from utils.utils import install_python_dependencies, install_chrome_and_chromedriver
#from scrapping.bourses_campusfaso import scraper_bourses_campusfaso
from scrapping.bourses_greatyop import get_total_pages, generate_page_urls,extract_links_from_pages, extract_bourse_info_from_urls
from scrapping.utils import setup_scraping_environment, configure_chrome, load_env_variables
# Configurer l'environnement de scraping
pd, time, webdriver, By, Service, Options, BeautifulSoup = setup_scraping_environment()

"""
Oui
"""
app = Flask(__name__)

@app.route('/')

# @app.route('/scrape_campusfaso')
# def scrape_campusfaso():
#     output_file = "bourses_campusfaso.csv"
#     scraper_bourses_campusfaso(output_file)
#     return "Scraping de Campus Faso terminé"

@app.route('/scrape_bourses_greatyop')
def scrape_bourses_greatyop():

    url_bourses = 'https://greatyop.com/category/bourses/'
    # Appeler la fonction et stocker le nombre total de pages dans la variable 'total_pages_bourses'
    total_pages_bourses = get_total_pages(url_bourses)

    url_stages = 'https://greatyop.com/category/stages-emplois/'
    # Appeler la fonction et stocker le nombre total de pages dans la variable 'total_pages_stages'
    total_pages_stages = get_total_pages(url_stages)

    url_formations = 'https://greatyop.com/category/formations/'
    # Appeler la fonction et stocker le nombre total de pages dans la variable 'total_pages_formations'
    total_pages_formations = get_total_pages(url_formations)


    urls_pages_bourses = generate_page_urls(url_bourses, total_pages_bourses)

    urls_pages_stages = generate_page_urls(url_stages, total_pages_stages)

    urls_pages_formations = generate_page_urls(url_formations, total_pages_formations)


    liens_bourses = extract_links_from_pages(urls_pages_bourses)

    liens_stages = extract_links_from_pages(urls_pages_stages)

    liens_formations = extract_links_from_pages(urls_pages_formations)


    bourses = extract_bourse_info_from_urls(liens_bourses)
    df_bourses = pd.DataFrame(bourses)
    df_bourses.to_csv('bourses.csv')

    stages = extract_bourse_info_from_urls(liens_stages)
    df_stages = pd.DataFrame(stages)
    df_stages['Type'] = 'Stage'
    df_stages.to_csv('stages.csv')

    formations = extract_bourse_info_from_urls(liens_formations)
    df_formations = pd.DataFrame(formations)
    df_formations['Type'] = 'Formation'
    df_formations.to_csv('formations.csv')

    df = pd.concat([df_bourses, df_stages, df_formations], ignore_index=True)
    df.to_csv('bourses_etudes.csv')


def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    install_python_dependencies()
    install_chrome_and_chromedriver() 
    app.run(debug=True)
