"""ETL

Extract Transform Load (Extrair Transformar Carregar)

Este script faz uso dos scripts de web scraping para coletar as informações
do processo de extração (Extract do ETL).

Também faz a transformação (Transform) dos dados pardronizando o nomes das colunas,
removendo dados que não fazem sentido e mantendo somente as classes de dados:
Verdadeiro, Falso.

Os dados extraídos e transformados são carregados (Load) em um arquivo .csv,
que poderá ser utilizado para análises e construção de modelos de machine learning.
"""

import scrap_agencia_lupa
import scrap_aosfatos
import scrap_github_fakebr_corpus
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table

"""Extract
Rodando web scraping nos sites selecionados

* https://www.aosfatos.org/noticias/nas-redes/
* https://piaui.folha.uol.com.br/lupa/
* https://github.com/roneysco/Fake.br-Corpus

"""
arq_agencia_lupa = scrap_agencia_lupa.start()
arq_aos_fatos = scrap_aosfatos.start()
arq_fakebr_corpus = scrap_github_fakebr_corpus.start()


"""Transform
Executa transformação dos dados.

Padroniza nome das colunas para:

* info - descrição
* url - origem
* img - imagem associada
* target - classe da notícia (Verdadeiro ou Falso)

Realiza o merge dos 3 csvs resultantes do web scraping de cada página

"""
dados_agencia_lupa = pd.read_csv(arq_agencia_lupa)
dados_aos_fatos = pd.read_csv(arq_aos_fatos)
dados_fakebr_corpus = pd.read_csv(arq_fakebr_corpus)

print(dados_agencia_lupa.sample(5))

dados_agencia_lupa.rename(columns={'classification': 'target', 'link':'url'}, inplace=True)
dados_aos_fatos.rename(columns={'classification': 'target', 'link':'url'}, inplace=True)
dados_fakebr_corpus.rename(columns={'link':'url'}, inplace=True)

dados_agencia_lupa.target = dados_agencia_lupa.target.map(lambda target: target.lower() if type(target) is str else '')
dados_aos_fatos.target = dados_aos_fatos.target.map(lambda x: x.lower().replace('\r\n', ''))
dados_fakebr_corpus.target = dados_fakebr_corpus.target.map(lambda x: x.lower())

targets = ['falso', 'verdadeiro']

dados_agencia_lupa_final = dados_agencia_lupa.query("target in {}".format(targets))
dados_aos_fatos_final = dados_aos_fatos.query("target in {}".format(targets))
dados_fakebr_corpus_final = dados_fakebr_corpus.query("target in {}".format(targets))

todos_os_dados = pd.concat([dados_agencia_lupa_final, dados_aos_fatos_final, dados_fakebr_corpus_final])

colunas = ['info', 'url', 'img', 'target']
todos_os_dados = todos_os_dados.reindex(columns = colunas)

"""Load
Carrega os dados para dentro de um arquivo csv

* info - descrição
* url - origem
* img - imagem associada
* target - classe da notícia (Verdadeiro ou Falso)

"""
todos_os_dados.to_csv('todos_os_dados.csv', index = False)






