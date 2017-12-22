import bs4
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
def recupere():
    my_url = 'https://play.google.com/store/search?q=toutes%20les%20applications%20camerounaise'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    dts = page_soup.find_all("div",{"class":"details"})
    liste = []
    for detail in dts :
        
        title_detail = detail.find_all("a",{"class":"title"})
        title_name = title_detail[0].text

        description_detail = detail.find_all("div",{"class":"description"})
        description = description_detail[0].text
        

        price_detail = detail.find_all("span",{"class":"display-price"}) 
        price = price_detail[0].text.strip()
        descrip = (title_name, description, price)
        liste.append(descrip)
    return liste
