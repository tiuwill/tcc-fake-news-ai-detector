# Proposta de modelo de ML para deteção de fake news

- Trabalho de conclusão da pós graduação de Inteligência Artificial e Aprendizado de Máquina da PUC Minas 

---

## Contextualização

- Este projeto contempla o processo de construção de alguns modelos de machine learning e deep learning para detecção de fake news contemplando o porcesso de coleta dos dados, a limpeza e processamento dos dados (Feature Engeering), a visualização e processo de construção das hipóteses e construção e testes em variados modelos.

---
## Estrutura do projeto

## Scripts:
- A pasta [scripts](https://github.com/tiuwill/tcc-fake-news-ai-detector/tree/main/scritps) contém os scripts python construídos para a coleta de dados.
    - o arquivo [scrap_agencia_lupa.py](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/scrap_agencia_lupa.py) é responsável por fazer a coleta das notícias no site da [Agência Lupa](https://piaui.folha.uol.com.br/lupa/)
    - o arquivo [scrap_aosfatos.py](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/scrap_aosfatos.py) é responsável por fazer a coleta das notícias no site [Aos Fatos](https://www.aosfatos.org/)
    - o arquivo [scrap_github_fakebr_corpus](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/scrap_github_fakebr_corpus.py) é responsável por fazer a coleta das notícias no repositório do git hub do [FakeBr-Corpus](https://github.com/roneysco/Fake.br-Corpus)
    - o arquivo [etl.py](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/etl.py) é responsável por juntar as coletas dos outros arquivos e formatar o dataset final.

## Datasets:

- A pasta [datasets](https://github.com/tiuwill/tcc-fake-news-ai-detector/tree/main/datasets) contém todos os resultados de coletas dos scritps, além do merge das coletas representando o dataset final
    - [agencia_lupa.csv](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/agencia_lupa.csv) arquivo resultante da coleta através do script [scrap_agencia_lupa.py](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/scrap_agencia_lupa.py) 
    - [aosfatos.csv](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/aosfatos.csv) arquivo resultante da coleta através do script  [scrap_aosfatos.py](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/scrap_aosfatos.py)
    - [fakebr-corpus.csv](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/fakebr-corpus.csv) é resultante do processamento do script [scrap_github_fakebr_corpus](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/scrap_github_fakebr_corpus.py)
    - [todos_os_dados.csv](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/todos_os_dados.csv) é resultante do processamento do script [etl.py](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/scritps/etl.py)


## Pesos:
- A pasta [pesos](https://github.com/tiuwill/tcc-fake-news-ai-detector/tree/main/pesos) contém os pesos dos modelos já treinados. Os mesmos podém ser entendidos através da visualização do relatório.

## Estatísticas
- A pasta [estatisticas](https://github.com/tiuwill/tcc-fake-news-ai-detector/tree/main/estatisticas) contem os resultados das avaliações dos modelos. Os mesmos podém ser entendidos através da visualização do relatório.

## Relatório:
- [TCC.ipynb](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/TCC%20Final.ipynb) é o notebook com toda a parte de engenharia de dados, visualizações e construção do modelo.
----
## Requerimentos

- Os requerimentos e bibliotecas necessárias para execução deste projeto podem ser encontrados através do arquivo [requirements.txt](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/requirements.txt)

### Em ambiente novo:
- Você pode criar um ambiente (environment) já com os requerimentos utilizando o [anacoda](https://www.anaconda.com/):
```
conda create --name fakedetector --file requirements.txt
```

- Caso tenha criado o ambiente, ative o mesmo com o [anacoda](https://www.anaconda.com/)

```
conda activate fakedetector
```

### Em ambiente existente:

- Você pode instalar em um ambiente (environment) já existente com o anaconda desta maneira:
```
conda install --name fakedetector --file requirements.txt
```