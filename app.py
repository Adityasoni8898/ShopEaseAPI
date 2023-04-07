from flask import *
import json, time, requests
from bs4 import BeautifulSoup
from Scraper.shopclues_scraper import shopclues_scraper
from Scraper.snapdeal_scraper import snapdeal_scraper

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {
        'Page': 'Home', 
        'Message': 'Sucess in loading', 
        'Timestamp' : time.time(),
        'Available Routes': [
            "/snapdeal_search/?search=<search term>",
            "/shopclues_search/?search=<search term>",
            "/flipkart_search/?search=<search term>"
        ]}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/snapdeal_search/', methods=['GET'])
def snapdeal_request_page():
    search_query = str(request.args.get('search')) 
    return snapdeal_scraper(search_query)


@app.route('/shopclues_search/', methods=['GET'])
def shopclues_request_page():
    search_query = str(request.args.get('search')) 
    return shopclues_scraper(search_query)

@app.route('/flipkart_search/', methods=['GET'])
def flipkart_request_page():
    search_query = str(request.args.get('search')) 
    json_return = requests.get(f"https://flipkart.dvishal485.workers.dev/search/{search_query}")
    json_return = json_return.json()
    products = json_return["result"]
    return products


if __name__ == '__main__':
    app.run(debug=True)