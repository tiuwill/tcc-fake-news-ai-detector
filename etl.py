import scrap_agencia_lupa
import scrap_aosfatos
import scrap_github_fakebr_corpus
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table


## Extract
# arq_agencia_lupa = scrap_agencia_lupa.start()
# arq_aos_fatos = scrap_aosfatos.start()
# arq_fakebr_corpus = scrap_github_fakebr_corpus.start()

arq_agencia_lupa = 'agencia_lupa.csv' 
arq_aos_fatos = 'aosfatos.csv'
arq_fakebr_corpus = 'fakebr-corpus.csv'


## Transform
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
## Load
todos_os_dados.to_csv('todos_os_dados.csv', index = False)






