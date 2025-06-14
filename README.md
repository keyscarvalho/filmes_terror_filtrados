# 📁 Análise de Filmes de Terror - Manipulação de Arquivos CSV com Python

Este projeto tem como objetivo principal **praticar e demonstrar habilidades com manipulação de arquivos CSV em Python**, utilizando dados reais da [IMDb](https://developer.imdb.com/non-commercial-datasets/). A análise foca em filmes do gênero **terror**, explorando dados como notas médias, número de votos e ano de lançamento.

---

## 🧠 Habilidades Trabalhadas

Durante o projeto, foram desenvolvidas e aplicadas as seguintes habilidades técnicas:

### 📄 Manipulação de arquivos CSV
- Leitura de arquivos `.tsv` (variação de CSV com tabulação) usando `pandas`
- Uso dos parâmetros:
  - `sep='\t'` para separar colunas por tabulação
  - `na_values='\\N'` para tratar valores ausentes
  - `dtype=str` para evitar problemas com tipos mistos
- Filtragem de colunas e linhas específicas com condições lógicas
- Conversão de tipos de dados (string → float/int)
- Junção de arquivos diferentes com `merge()` (dados de notas e informações básicas)
- Escrita de novos arquivos CSV com `to_csv()` e `index=False` para salvar sem índice

### 🔍 Análise exploratória de dados
- Filtragem de filmes por gênero (terror) e por número mínimo de votos
- Ordenação por nota média (`averageRating`)
- Criação de DataFrames intermediários para validação dos dados

---

## 📁 Estrutura do Projeto

```bash
analise_terror_csv/
├── data/
│ ├── raw/ # Arquivos brutos (.tsv) da IMDb
│ └── processed/ # Arquivos CSV gerados após tratamento
├── src/
│ └── main.py
├── requirements.txt
└── README.md
```
---

## 🗂 Etapas do Projeto

1. **Carregamento dos dados**:
   - Leitura dos arquivos `title.basics.tsv` e `title.ratings.tsv`

2. **Filtragem dos dados**:
   - Apenas filmes (`titleType = movie`)
   - Do gênero **Horror**
   - Com mais de **1000 votos**

3. **Tratamento e junção**:
   - Conversão de colunas para `float` e `int`
   - Junção dos dois arquivos com base na coluna `tconst`

4. **Exportação**:
   - Criação de um novo arquivo CSV com os dados tratados

---

## 🚀 Como executar

1. Instale as dependências com:

```bash
pip install -r requirements.txt
```

2. Baixe os arquivos .tsv da IMDb e salve em data/raw/.

3. Execute o script principal:

```bash
python main.py
```

## 🛠 Bibliotecas utilizadas

`pandas`

## 📌 Fonte dos dados
[IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/)

## 👩‍💻 Sobre o projeto

Este projeto foi desenvolvido com foco no aprendizado e prática da manipulação de arquivos CSV com Python, com dados reais e uma temática que eu amo (filmes de terror 🎃). Ele faz parte do meu portfólio como estudante em transição de carreira para a área de Dados.

## 📬 Contato
[LinkedIn](https://www.linkedin.com/in/keyllascarvalho/)