import dryscrape
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def getwebpage(url):
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    return BeautifulSoup(response, "lxml")

def get_counts(username,soups):
    counts = {}
    for link in soups.find_all('a'): 
        link = str(link)
        beginning = link.find('username')
        if beginning != -1:
            name = link[beginning+9:]
            counts['time'] = datetime.now()
            if name.find(username) != -1:
                name = name[:-4]
                state = name[name.find("state=")+6:name.find(">")-1]
                count = name[name.find(">")+1:]
                counts[state] = int(count)
    counts = pd.DataFrame([counts])
    return counts