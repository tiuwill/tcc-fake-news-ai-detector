import pandas as pd
import numpy as np
import git 
from git import RemoteProgress
import time
import os
import sys

def get_data_from_file_list(files, target, info_directory, meta_directory):
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
    FAKE_DIR = './fakebr/full_texts/fake'
    META_FAKE_DIR = './fakebr/full_texts/fake-meta-information'
    TRUE_DIR = './fakebr/full_texts/true'
    META_TRUE_DIR = './fakebr/full_texts/true-meta-information'
    FILE_NAME = 'fakebr-corpus.csv'

    # print('Cloning Fake.Br-Corpus')
    # git.Repo.clone_from('https://github.com/roneysco/Fake.br-Corpus.git', './fakebr', 
    # branch='master')

    fake_news_files = os.listdir(FAKE_DIR)
    true_news_files = os.listdir(TRUE_DIR)

    fake_data = get_data_from_file_list(fake_news_files, 'Falso', FAKE_DIR, META_FAKE_DIR)
    true_data = get_data_from_file_list(true_news_files, 'Verdadeiro', TRUE_DIR, META_TRUE_DIR)

    all_data = fake_data + true_data

    df = pd.DataFrame(all_data)
    df.to_csv(FILE_NAME, index = False)
    return FILE_NAME

