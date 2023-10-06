import requests
from bs4 import BeautifulSoup

def Scrape(URL):
    try: Response = requests.get(URL)
    except: return []
    Sentences = []
    if Response.status_code == 200:
        Soup = BeautifulSoup(Response.text, 'html.parser')
        # Contents = Soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div', 'li', 'a', 'strong', 'em', 'b', 'i', 'u', 's'])
        Contents = Soup.find_all(['h1', 'h2']) #, 'h3', 'h4', 'h5', 'h6'

        for Content in Contents:
            Sentence = ""
            WordsCount = len(Content.get_text(separator = " ").split())
            if WordsCount:
                for x in Content.get_text(separator = "\n").split():
                    Sentence += x 
                    Sentence += " "

            if Sentence:
                Sentences.append(Sentence)
                    
    return Sentences