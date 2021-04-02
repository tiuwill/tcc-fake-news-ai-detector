import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import urllib.request



def start():
    # Aqruivo para extrair os dados do site piaui.folha.uol.com.br
    page_index = 1
    BASE_URL = 'https://piaui.folha.uol.com.br/lupa/page/'
    FILE_NAME = 'agencia_lupa.csv'

    dados = []

    class_words = ['VERDADEIRO', 'VERDADEIRO, MAS', 'AINDA É CEDO PARA DIZER', 'EXAGERADO', 'CONTRADITÓRIO', 'SUBESTIMADO', 'INSUSTENTÁVEL', 'FALSO', 'DE OLHO']
    while True:
        URL = BASE_URL + str(page_index)
        with urllib.request.urlopen(URL) as page:
            print(f"Scraping page {page_index}")
            main = BeautifulSoup(page, 'lxml')
            news_div =  main.find_all('div', {'class': 'internaPGN'})    
            links = [a['href'] for a in news_div[0].find_all('a')]
            if len(links) > 0:
                for link in set(links):
                    with urllib.request.urlopen(link) as new_details:
                        detailed_new = BeautifulSoup(new_details, 'lxml')
                        detail_div = detailed_new.find('div', {'class': 'post-inner'})
                    # print(detail_div)
                        info,source, img = '','',''
                        for child in detail_div.descendants:
                            if child.name == 'b' and child.text not in class_words and 'Lupa' not in child.text:
                                info += child.text + ' '                        
                            if child.name == 'strong':
                                info += child.text + ' '
                            elif child.name == 'i':
                                source += child.text
                            elif child.name == 'img':
                                img = child['src']
                            elif child.name == 'div' and child.get('class') is not None and 'etiqueta' in child.get('class'):
                                if info.strip():
                                    dados.append({'info': info, 'source': source, 'img': img, 'link': link, 'classification': child.text})
                                info,source, img = '','',''
            else:
                print('Fim do web scrapping')
                break
        page_index += 1

    print(f'Total de páginas processadas {page_index-1}')

    df = pd.DataFrame(dados)
    df.to_csv(FILE_NAME, index=False)
    return FILE_NAME




