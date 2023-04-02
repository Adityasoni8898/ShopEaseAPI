def snapdeal_scraper(search_query):
    from bs4 import BeautifulSoup
    import requests, json
    import math

    Product = []

    url = f"https://www.snapdeal.com/search?keyword={search_query}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find_all("div", class_ = "col-xs-6")

    for i in box:
        product_img = ""
        product_link = ""
        product_name = ""
        product_price = ""
        product_rating = ""
        #img
        temp = i.find("source")
        if temp is not None:
            product_img = temp.get("srcset")

        #link
        temp = i.find("a", class_ = "dp-widget-link")
        if temp is not None:
            product_link = temp.get("href")

        #rating
        temp = i.find("div", class_ = "filled-stars")
        if temp is not None:
            temp = temp.get("style")
            length = len(temp)
            temp = float(temp[7:length-1])
            product_rating = int(math.floor(temp))

        #name
        temp = i.find("p", class_ = "product-title")
        if temp is not None:
            product_name = temp.text

        #price
        temp = i.find("span", class_ = "lfloat product-price")
        if temp is not None:
            temp = temp.text
            product_price = temp[5:]

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

        

    return Product
