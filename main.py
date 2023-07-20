# flipkart
import requests
from bs4 import BeautifulSoup
def get_url(search_term):
    # template="https://www.amazon.in/s?k={}&sprefix=mo%2Caps%2C301&ref=nb_sb_ss_ts-doa-p_1_2"
    template="https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    search_term=search_term.replace(' ','+')
    url=template.format(search_term)
    url+='&page{}'
    return url
def extract_info(result):
    # res=result.a
    name=result.find('span',{'class':'_4rR01T'}).text
    ram=result.find('span',{'class':'rgWa7D'}).text
    try:
        price=result.find('span',{'class':'_30jeg3_1_WHN1'}).text
    except AttributeError:
        return
    link="https://www.flipkart.com"+result.get('href')
    info=(name,ram,price,link)
    return in

url=get_url('mobiles')
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
r = requests.get(url, headers=headers)
content=r.content
soup=BeautifulSoup(content,'html.parser')
# soup=soup.text()
results = soup.find_all("div", {"class": "col col-7-12"})
results
title=soup.title
print(len(results))