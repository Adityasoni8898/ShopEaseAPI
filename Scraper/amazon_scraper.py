def flipkart_scraper(search_query):
    from bs4 import BeautifulSoup
    import requests, json
    import math


    Product = []
    url = f"https://www.amazon.in/s?k={search_query}"
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

    

# products:
#     css: 'div[data-component-type="s-search-result"]'
#     xpath: null
#     multiple: true
#     type: Text
#     children:
#         title:
#             css: 'h2 a.a-link-normal.a-text-normal'
#             xpath: null
#             type: Text
#         url:
#             css: 'h2 a.a-link-normal.a-text-normal'
#             xpath: null
#             type: Link
#         rating:
#             css: 'div.a-row.a-size-small span:nth-of-type(1)'
#             xpath: null
#             type: Attribute
#             attribute: aria-label
#         reviews:
#             css: 'div.a-row.a-size-small span:nth-of-type(2)'
#             xpath: null
#             type: Attribute
#             attribute: aria-label
#         price:
#             css: 'span.a-price:nth-of-type(1) span.a-offscreen'
#             xpath: null
#             type: Text