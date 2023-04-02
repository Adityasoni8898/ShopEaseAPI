def shopclues_scraper(search_query):
    from bs4 import BeautifulSoup
    import requests, json

    Product = []

    url = {f"https://www.shopclues.com/search?q={search_query}&sc_z=&z=0&count=8&user_id=&user_segment=default", f"https://www.shopclues.com/ajaxCall/searchProducts?q={search_query}&z=0&page=4&filters=&fl_cal=1&sc_z=&user_id=&user_segment=default"}
    
    for u in url:
        r = requests.get(u)
        print(r)

        soup = BeautifulSoup(r.text, 'lxml')
        box = soup.find_all("div", class_ = "search_blocks")

        for i in box:
            product_img = ""
            product_link = ""
            product_name = ""
            product_price = ""
            product_rating = ""
            #link
            temp = i.find("a")
            if temp is not None:
                product_link = "https:" + temp.get("href")

            #name
            temp = i.find("h2")
            if temp is not None:
                product_name = temp.text

            #rating
            temp = i.find("span", class_ = "star")
            if temp is not None:
                hell = "d"
                temp = temp.find("span")
                temp = temp.get("style")
                #remove the irrelevent chars
                length = len(temp)
                product_rating = temp[6:length-2]
            
            #price
            temp = i.find("a")
            if temp is not None:
                temp = temp.find("span", class_ = "p_price")
                temp = temp.text
                #remove the irrelevent chars
                length = len(temp)
                product_price = temp[1:length-44]

            #img
            temp = i.find("a")
            if temp is not None:
                temp = temp.find("div", class_ = "img_section")
                temp = temp.find("img")
                product_img = temp.get("src")

            #jsonification
            Product_data = {
                'Product_link' : product_link,
                'Product_name': product_name, 
                'Product_rating': product_rating, 
                'Product_price': product_price,
                'Product_img': product_img,
            }
            Product.append(Product_data)


    json_dump = json.dumps(Product)
    print(json_dump)
    return json_dump 