# Datasets

Detalhamento e descrição dos arquivos resultantes do web scraping e do dataset completo

---

## [Aos fatos](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/agencia_lupa.csv)

Colunas:

| Coluna | Descrição                                | Tipo   |
| -------|:----------------------------------------:| ------:|
| info   | Texto completo da notícia                | string |
| img    | Url da Imagem vinculada a notícia        | string |
| link   | Url da notícia                           | string |
| classification  | Classificação da notícia        | string |

 
- Total de notícias: 899
- Total de notícias falsas: 830
- Total de notícias distorcidas: 69
- Classes de notícias: falso, verdadeiro, distorcido, impreciso

---

## [Agência Lupa](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/aosfatos.csv)

Colunas:

| Coluna           | Descrição                 | Tipo   |
| -----------------|:-------------------------:| ------:|
| info             | Texto completo da notícia | string |
| source           | Informações relacionadas a compartilhamento da notícia | string |
| link             | Url da notícia | string |
| img              | Url da Imagem vinculada a notícia | string |
| classification   | Classificação da notícia | string |

- Total de notícias: 6577  
- Total de notícias falsas: 3063 
- Total de notícias verdadeiras: 1414 
- Total de notícias de outra categoria: 2100  
- Classes de notícias: VERDADEIRO, "VERDADEIRO, MAS", AINDA É CEDO PARA DIZER, EXAGERADO, CONTRADITÓRIO, SUBESTIMADO, INSUSTENTÁVEL, FALSO, DE OLHO

----
## [Fake.br-Corpus](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/fakebr-corpus.csv)

Colunas:

| Coluna           | Descrição                 | Tipo   |
| -----------------|:-------------------------:| ------:|
| info             | Texto completo da notícia | string |
| link             | Url da notícia | string |
| target           | Classificação da notícia | string |

- Total de notícias: 7200   
- Total de notícias falsas: 3600 
- Total de notícias verdadeiras: 3600 
- Classes de notícias: Falso e Verdadeiro

---
## [Dataset Final](https://github.com/tiuwill/tcc-fake-news-ai-detector/blob/main/datasets/todos_os_dados.csv)

Colunas:

| Coluna           | Descrição                 | Tipo   |
| -----------------|:-------------------------:| ------:|
| info             | Texto completo da notícia | string |
| url             | Url da notícia | string |
| img           | Url da Imagem vinculada a notícia | string |
| target           | Classificação da notícia | string |

- Total de notícias: 12.511   
- Total de notícias falsas: 7497 
- Total de notícias verdadeiras: 5014  
- Classes de notícias: Falso e Verdadeiro