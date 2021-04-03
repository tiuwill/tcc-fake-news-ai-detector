"""Web Scrap Aos Fatos

Este script percorre a página de listagem de notícia, entrando em notícia por notícia,
extrai o conteúdo da notícia, a imagem e a classe da notícia.

O Script para no momento que tomamos um erro 404 de página não encontrada.
Estouramos o número de paginação suportado pelo site pela falta de notícias
para a quantidade páginas que passamos

O endereço do site em que as notícias foram coletadas foi:

* https://www.aosfatos.org/noticias/nas-redes/

"""


import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import urllib.request

# Aqruivo para extrair os dados do site aosfatos.org

def start():
    """Percorre as notícias página por página

    Returns
    -------
    string
        retorna o caminho do arquivo csv criado com as informações coletadas
            * sendo o arquivo coletado possuindo as seguintes colunas:
                - info: descrição da notícia
                - img: imagem associada a notícia
                - link: url da notícia onde a informação foi coletada
                - classification: classe da notícia
    """

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
                """Fazendo a request

                    Abrimos a requisição e passamos a requisição para o BeautifulSoup, para podermos navegar com os elementos
                """  
                main = BeautifulSoup(page, 'lxml')
                cards  = main.find_all('a', class_ = 'card')

                """Lista de links dos cars

                    A listagem de notícias aqui trabalha com o conceito de cards com aproximadamente 15 cards de notícia por página
                """  

                for card in cards: # Para cada card de notícia presente na página
                    
                    ### Extraindo link do card
                    card_path = card['href']
                    card_url = BASE_URL + card_path
                    ###Acessando o link do card e extraindo o html
                    with urllib.request.urlopen(card_url) as card_response:
                        """Fazendo a request para a notícia

                           Agora no lugar de percorrer a listagem de notícias, vamos entrar dentro de uma notícia e extrair seu conteúdo
                           Passamos também a request para o BeautifulSoup para podermos navegar dentro do html da página.

                           A tag article é onde fica o conteúdo da página, ela possui a notícia que queremos coletar,
                           mas também uma série de comentários feitos pelos responsáveis pelo site. No caso precisamos extrair apenas o que seria de fato
                           a notícia que está sendo compartilhada
                        """  
                        card_page = BeautifulSoup(card_response, 'lxml')

                        article = card_page.find('article', {'class': 'ck-article'})

                        """Extraindo a notícia

                            As notícias em si, que são as compartilhadas e averiguadas costumam estar em tags como citação (blockquote), as informações das noticias
                            aqui como imagens textos ficam todas em volta da tag blockquote. O texto pode ficar dentro também da tag parágrafo (p) dentro da tag blockquote.
                            
                            A mesma pagína pode ter mais de uma notícia.

                            Aqui a classifcação da notícia variou de lugares, podendo estar escrita, dentro de alguma tag como p ou pre, ou poderia estar no nome da imagem.
                            Foram feitas várias checagens para obter a classificação
                            
                            * Começamos iniciando os atribuitos da notícia como vazio
                            * Depois percorremos até as tags de citação(blockquote)
                            * Buscamos a imagem da notícia
                            * Por fim buscamos a classificação da notícia
                            * Colocamos a notícia em uma lista de notícias processadas
                            * Reiniciamos as variáveis de atributos da notícia (info, img, classification)
                        """
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
        except urllib.request.HTTPError as e:  # Entra aqui quando obtem erro por tentar acessar uma páginação que não existe
            if e.code == 404:
                print(f'Página não encontrada: {pageIndex}')
                break
        pageIndex+=1


    print('Scrapping finalizado')

    """Exportando

       Após percorrer e coletar todas as notícias, criamos um dataframe a partir da lista de coleta e criamos um data frame
       para a exportação dos dados coletados
    """
    df = pd.DataFrame(dados)
    df.to_csv(FILE_NAME, index = False)
    return FILE_NAME











