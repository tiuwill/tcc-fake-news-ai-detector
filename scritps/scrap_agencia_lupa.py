"""Web Scrap Agência lupa

Este script percorre a página de listagem de notícia, entrando em notícia por notícia,
extrai o conteúdo da notícia, a imagem e a classe da notícia.

O Script para no momento que não encontrar mais links de notícias para clicar

O endereço do site em que as notícias foram coletadas foi:

* https://piaui.folha.uol.com.br/lupa/page/

"""

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import urllib.request



def start():
    """Percorre as notícias página por página

    Returns
    -------
    string
        retorna o caminho do arquivo csv criado com as informações coletadas
            * sendo o arquivo coletado possuindo as seguintes colunas:
                - info: descrição da notícia
                - img: imagem associada a notícia
                - source: origem da notícia (rede social, hora de compartilhamento, etc)
                - link: url da notícia onde a informação foi coletada
                - classification: classe da notícia
    """
    page_index = 1
    BASE_URL = 'https://piaui.folha.uol.com.br/lupa/page/'
    FILE_NAME = '../datasets/agencia_lupa.csv'

    dados = []

    class_words = ['VERDADEIRO', 'VERDADEIRO, MAS', 'AINDA É CEDO PARA DIZER', 'EXAGERADO', 'CONTRADITÓRIO', 'SUBESTIMADO', 'INSUSTENTÁVEL', 'FALSO', 'DE OLHO']
    while True:
        URL = BASE_URL + str(page_index)
        
        with urllib.request.urlopen(URL) as page:    
            print(f"Scraping page {page_index}") #mostra o número da página
            main = BeautifulSoup(page, 'lxml')
            """Fazendo a request

                Abrimos a requisição e passamos a requisição para o BeautifulSoup, para podermos navegar com os elementos
            """           
            news_div =  main.find_all('div', {'class': 'internaPGN'}) # Pega a div com toda a listagem do conteúdo da página   
            links = [a['href'] for a in news_div[0].find_all('a')] # Cria uma lista com todos os links presentes na listagem da página
            """Lista de links

               A página retornada é uma lista de notícias, para cada item da lista vamos entrar dentro da notícia e extrair seu conteúdo.
               Se a página de listagem não apresentar mais nenhum link de notícia, o script finaliza a execução. 
            """
            if len(links) > 0:
                for link in set(links): # Para cada link de notícia presente na página
                    with urllib.request.urlopen(link) as new_details:
                        """Fazendo a request para a notícia

                           Agora no lugar de percorrer a listagem de notícias, vamos entrar dentro de uma notícia e extrair seu conteúdo
                           Passamos também a request para o BeautifulSoup para podermos navegar dentro do html da página.

                           A detail_div é a div onde fica o conteúdo da página, ela possui a notícia que queremos coletar,
                           mas também uma série de comentários feitos pelos responsáveis pelo site. No caso precisamos extrair apenas o que seria de fato
                           a notícia que está sendo compartilhada
                        """  
                        detailed_new = BeautifulSoup(new_details, 'lxml') 
                        detail_div = detailed_new.find('div', {'class': 'post-inner'}) 
                    

                        """Extraindo a notícia

                            As notícias em si, que são as compartilhadas e averiguadas costumam estar em tags de destaque, no caso b, strong (para negrito),
                            i para itálico. A imagem da notícia costuma estar na tag img dentro da div de detalhes da notícia. E a classificação fica dentro 
                            de uma div com classe de nome "etiqueta"
                            
                            * Começamos iniciando os atribuitos da notícia como vazio
                            * Depois percorremos até as tags de destaque (i, b, strong)
                            * Buscamos a imagem da notícia
                            * Por fim buscamos a classificação da notícia
                            * Colocamos a notícia em uma lista de notícias processadas
                            * Reiniciamos as variáveis de atributos da notícia (info, source, img)
                        """
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
            else: # Entra aqui quando a listagem de notícias não retornou mas nenhuma notícia
                print('Fim do web scrapping') 
                break
        page_index += 1

    print(f'Total de páginas processadas {page_index-1}')

    """Exportando

       Após percorrer e coletar todas as notícias, criamos um dataframe a partir da lista de coleta e criamos um data frame
       para a exportação dos dados coletados
    """

    df = pd.DataFrame(dados) 
    df.to_csv(FILE_NAME, index=False)
    return FILE_NAME
