import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import urllib.request

# Aqruivo para extrair os dados do site aosfatos.org

def start():
    pageIndex = 1
    BASE_URL = 'https://www.aosfatos.org'
    FILE_NAME = 'aosfatos.csv'

    dados = []
    class_words = ['falso', 'verdadeiro', 'distorcido', 'impreciso']

    while True:
        print(f'Coletando dados da página {pageIndex}')
        URL = 'https://www.aosfatos.org/noticias/nas-redes/?page=' + str(pageIndex)
        try:
            with urllib.request.urlopen(URL) as page:
                main = BeautifulSoup(page, 'lxml')
                cards  = main.find_all('a', class_ = 'card')

                for card in cards:
                    ### Extraindo link do card
                    card_path = card['href']
                    card_url = BASE_URL + card_path
                    ###Acessando o link do card e extraindo o html
                    with urllib.request.urlopen(card_url) as card_response:
                        card_page = BeautifulSoup(card_response, 'lxml')

                        article = card_page.find('article', {'class': 'ck-article'})
                        info,img,classification = '','',''
                        blockquote_count = 0
                        for child in article.descendants:
                            if child.name == 'blockquote' and blockquote_count == 0:
                                info = child.text
                                next_paragrph = child.find_next_sibling('p')
                                if next_paragrph is not None:
                                    info_img = next_paragrph.find('img')
                                    img = info_img['src'] if info_img is not None else ''
                                if info.strip() and classification.strip() and classification.lower().strip() in class_words:
                                    dados.append({'info': info, 'img': img, 'link': card_url, 'classification': classification})
                                    
                                info, img, classification = '','',''
                                blockquote_count += 1
                            elif child.name == 'pre' and child.text.lower().strip() in class_words:
                                classification = child.text 
                            elif child.name == 'p' and child.text.lower() in class_words:
                                classification = child.text 
                            elif child.name == 'img' and child.attrs is not None:
                                classification = child['src'].split('/')[-1].split('.')[0]
                            elif classification not in class_words and child.name == 'figcaption' and child.text.lower() in class_words:
                                classification = child.text
        except urllib.request.HTTPError as e:
            if e.code == 404:
                print(f'Página não encontrada: {pageIndex}')
                break
        pageIndex+=1


    print('Scrapping finalizado')

    df = pd.DataFrame(dados)
    df.to_csv(FILE_NAME, index = False)
    return FILE_NAME











