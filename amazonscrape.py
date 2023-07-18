from requests_html import HTMLSession
from bs4 import BeautifulSoup
import flipkart
from flipkart import get_url,extract_info
import re
# import re
s=HTMLSession()
def get_url(search_term):
    template="https://www.amazon.in/s?k={}&page="
    search_term=search_term.replace(' ','+')
    search_term=search_term.replace('(','+')
    search_term=search_term.replace(')','+')
    url=template.format(search_term)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    n=soup.find("span",{"class":"s-pagination-item s-pagination-disabled"}).text
    print(int(n))
    return url,int(n)
def getinfo(soup):
    soup=soup.find("div",{"class":"a-expander-content a-expander-section-content a-section-expander-inner"})
    # print(soup.text)
    # print(soup.text)
    # print(soup.text)
    if(soup is None):
        return
    te=soup.find_all('tr')
    # while(soup.text!="model number"):
    #
    for t in te:
        if(t.text.find("model number")!=-1):
            break
    # print(t.text)
    t=t.find('td').text
    t=t.strip()
    # print(t.strip())
    print("hi")
    # print(te)
    # # te=4soup.find_next_sibling("model number")
    # matched_tags = soup.find(lambda tag: len(tag.find_all()) == 0 and "model number" in tag.text)
    # te.next()
    # print(matched_tags)
    # te=soup.find_all('tr')
    # print(te)
    c=0
    url = flipkart.get_url(t)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title)
    result = soup.find("div", {"class": "_2kHMtA"})
    flipkart.extract_info(result)
    return 1,c
def extract_info(result):
    soup=result.find("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
    name=result.find("span",{"class":"a-size-medium a-color-base a-text-normal"}).text
    # if name.find(')')==-1:
    #     return
    # i=name.index(')')
    # name=name[0:i+1]
    # i=name.find("(")
    # k=name.find(",")
    # if(k==-1):
    #     k=name.find(" ")
    #     k=name.find(" ",k+1)
    # colour=name[i+1:k]
    # j=name.find("GB")
    # ram=name[j-1:j+2]
    # i=name.find("GB",j+1)
    # j=name.find(", ",j+1,i)
    # if(j==-1):
    #     j=i-5
    # rom=name[j+2:i+2]
    # i = name.find("(")
    # name=name[0:i]
    # #
    # # if name.find('RAM') == -1:
    # #     ram=ram+' RAM'
    # # ram=ram+name[j+3:j+17]
    try:
        price=result.find("span",{"class":"a-price-whole"}).text
        price=price.replace(",","")
        price= ''.join(x for x in price if x.isdigit())
        price=int(price)
    except AttributeError:
        return
    for a in soup.find_all('a', href=True):
        ss=a['href']
        break
    link="https://www.amazon.in"+ss
    # info=(name,colour,ram,rom,price,link)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    r = s.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    info=getinfo(soup)
    ff=0
    if(info[1]==1):
        ff=1;
    # print(info)
    return ff
def mai(search_term):
    records=[]
    url,n=get_url(search_term)
    # print(url)
    dddd=0
    check=0
    for i in range(1,n):
        ur=url+str(i);
        # print(ur)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
        r = s.get(ur, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)
        results=soup.find_all("div",{"class":"s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border"})
        for item in results:
            record = extract_info(item)
            dddd=dddd+1
            if record:
                records.append(record)
                check=check+1;
                # print('0hi')
    print(dddd)
    print(check)
names=["lenovo laptops"]
for name in names:
    print(name)
    mai(name)

