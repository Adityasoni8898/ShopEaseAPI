def flipkart_scraper(search_query):
    from bs4 import BeautifulSoup
    import requests, json
    import math


    Product = []
    url = f"https://flipkart.dvishal485.workers.dev/search/{search_query}"
    response = requests.get

    for i in box:
        product_img = ""
        product_link = ""
        product_name = ""
        product_price = ""
        product_rating = ""


        #jsonification
        Product_data = {
            'Product_link' : product_link,
            'Product_name': product_name, 
            'Product_rating': product_rating, 
            'Product_price': product_price,
            'Product_img': product_img,
        }
        print(Product_data)
        
        Product.append(Product_data)

    

flipkart_scraper("saree")