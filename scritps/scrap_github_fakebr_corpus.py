"""Extract FakeBrCorpus

Este script percorre clona o repositório do corpus FakeBr.
O script percorre as pastas criadas e lê todos os arquivos e insere nos arquivos
as notícias lidas por arquivos de acordo com a classificação que o mesmo estava.

Os arquivos estão dividios em uma pasta fake e uma pasta true.

* https://github.com/roneysco/Fake.br-Corpus

"""

import pandas as pd
import numpy as np
import git 
from git import RemoteProgress
import time
import os
import sys

def get_data_from_file_list(files, target, info_directory, meta_directory):
    """Executa a leitura de vários arquivos e retorna a lista com o conteúdo
        
    Parameters
    ----------
    files : list(str)
        Lista com os caminhos de arquivos
    target : str
        Classe da notícia lida para ser adicionada à informação da lista
    info_directory : str
        Caminho raiz do arquivo
    meta_directory: str
        Caminho dos meta dados para cada arquivo da lista

    Returns
    -------
    list
        a list of strings used that are the header columns
    """
    data = []
    for f in files:
        with open(info_directory+'/'+f, 'r') as reader:
            info = reader.read()
            file_name = f.split('.')[0]
            with open(f'{meta_directory}/{file_name}-meta.txt') as meta:
                lines = meta.readlines()               
                data.append({'info': info,'link': lines[1], 'target': target})    
    return data

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
    FAKE_DIR = './fakebr/full_texts/fake'
    META_FAKE_DIR = './fakebr/full_texts/fake-meta-information'
    TRUE_DIR = './fakebr/full_texts/true'
    META_TRUE_DIR = './fakebr/full_texts/true-meta-information'
    FILE_NAME = 'fakebr-corpus.csv'

    """Clonando repositório

       Primeiramente é feita a clonagem do repositório com todas as notícias.
    """
    print('Cloning Fake.Br-Corpus')
    git.Repo.clone_from('https://github.com/roneysco/Fake.br-Corpus.git', './fakebr', branch='master')

    """Lista com nome dos arquivo

       Faz a leitura dos dois diretórios e pega todos os nomes de arquivos presentes no mesmo.
    """  
    fake_news_files = os.listdir(FAKE_DIR)
    true_news_files = os.listdir(TRUE_DIR)


    """Executa leitura

       Faz a leitura dos arquivos e recebe o conteúdo de todas as notícias presentes no diretórios.
       As listas retornadas serão concatenadas para exportação
    """  
    fake_data = get_data_from_file_list(fake_news_files, 'Falso', FAKE_DIR, META_FAKE_DIR)
    true_data = get_data_from_file_list(true_news_files, 'Verdadeiro', TRUE_DIR, META_TRUE_DIR)

    all_data = fake_data + true_data

     """Exportando

       Após percorrer e coletar todas as notícias, criamos um dataframe a partir da lista de coleta e criamos um data frame
       para a exportação dos dados coletados
    """
    df = pd.DataFrame(all_data)
    df.to_csv(FILE_NAME, index = False)
    return FILE_NAME

