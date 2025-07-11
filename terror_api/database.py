#%%
import pandas as pd


df = pd.read_csv("../data/processed/filmes_terror_filtrados.csv")
df.head()


# Filtra só os filmes com "Horror" nos gêneros
df = df[df["genres"].str.contains("Horror", na=False)]


# Cria uma coluna de subgêneros, excluindo "Horror"
def extrair_subgeneros(g):
    generos = g.split(",")
    return [gen for gen in generos if gen != "Horror"]

df["subgeneros"] = df["genres"].apply(extrair_subgeneros)

# Ajusta colunas para a API
df["titulo"] = df["primaryTitle"]
df["ano"] = df["startYear"]
df["nota"] = df["averageRating"]
df["votos"] = df["numVotes"]

# Remove colunas que não serão usadas
df_filtrado = df[["titulo", "ano", "nota", "votos", "subgeneros"]]